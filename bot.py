import telebot
import json
from info import *
from telebot import types
from additional_functions import *
import random

token = '6797511487:AAET4vGng_8X8bYIHDtocZN_vvQuKIMEnKw'

bot = telebot.TeleBot(token=token)


with open('data.json', 'r') as file:
    try:
        user_data = json.load(file)
    except:
        user_data = {}







@bot.message_handler(commands=['start', 'help'])
def start(message):
    user_id = str(message.from_user.id)
    if message.text == '/start':

        user_data[user_id] = {}
        random_questions = random.sample(list(questions.keys()), len(questions))
        user_data[user_id]['all_questions'] = random_questions
        user_data[user_id]['unpopped_questions'] = random_questions.copy()
        user_data[user_id]['question_num'] = 0
        user_data[user_id]['answers'] = {}
        user_data[user_id]['current_question_key'] = None
        user_data[user_id]['finished'] = False
        user_data[user_id]['preferred_language'] = 'rus_version'
        user_data[user_id]['results'] = None

        markup = markup_func_introduction('rus_version')
        bot.send_message(message.chat.id, msg_intr_rus_version, reply_markup=markup)
        with open('data.json', 'w') as file:
            json.dump(user_data, file)
    else:
        language = user_data[user_id]['preferred_language']
        markup = help_markup(language)
        text = markup_dict[language]['help_text']
        bot.send_message(chat_id=user_id, text=text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = str(call.message.chat.id)

    if call.data in ['intr_eng_version', 'intr_rus_version', 'help_eng_version', 'help_rus_version']:
        language = call.data[5:]
        if call.data.startswith('help'):
            print('dfkajkdlsajfklsd')
            text = markup_dict[language]['help_text']
            markup = help_markup(language)
        else:
            text = markup_dict[language]['intr_msg_language']
            markup = markup_func_introduction(language)
        user_data[user_id]['preferred_language'] = language
        bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id,
                              text=text,
                              reply_markup=markup)

    elif call.data in ['finish_eng_version', 'finish_rus_version']:
        language = call.data[7:]
        redo = False
        markup = final_markup(language)
        try:
            scores = user_data[user_id]['results'][0]
            correct_results = user_data[user_id]['results'][1]
            bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id,
                                  text=finish_text(language, scores, correct_results), reply_markup=markup)
        except:
            pass




    elif call.data in ['rus_version', 'redo_rus_version', 'eng_version',
                       'redo_eng_version', 'finish_eng_version', 'finish_rus_version']:
        callback_question_num = int(call.message.text[:2])
        card_key = user_data[user_id]['all_questions'][len(questions) - callback_question_num]
        print(card_key)
        if call.data in ['redo_rus_version', 'redo_eng_version']:
            language = call.data[5:]
            redo = True
            chosen_option_index = user_data[user_id]['answers'][card_key][1]
            redo_answer = questions[card_key][call.data[5:]]['options'][chosen_option_index]
            if user_data[user_id]['question_num'] == len(questions):
                markup = markup_func_redo(language, final_question=True)
            else:
                markup = markup_func_redo(language)
        else:
            redo = False
            redo_answer = False
            markup = markup_func(call.data)
            language = call.data
            if user_data[user_id]['question_num'] == len(questions):
                markup = markup_func(call.data, final_question=True)
            else:
                markup = markup_func(call.data)
        if card_key == user_data[user_id]['current_question_key']:
            user_data[user_id]['preferred_language'] = language
        user_data[user_id]['language_of_question'] = language

        bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id,
                              text=making_question(language, card_key, callback_question_num,
                                                   redo, redo_answer),
                              reply_markup=markup)

    if not user_data[user_id]['finished']:
        if call.data == 'next_question':
            if user_data[user_id]['unpopped_questions']:
                user_data[user_id]['question_num'] += 1
                user_data[user_id]['current_question_key'] = user_data[user_id]['unpopped_questions'].pop()
                current_question_key = user_data[user_id]['current_question_key']
                preferred_language = user_data[user_id]['preferred_language']
                if user_data[user_id]['question_num'] == len(questions):
                    markup = markup_func(preferred_language, final_question=True)
                else:
                    markup = markup_func(preferred_language)
                bot.send_message(chat_id=user_id,
                                 text=making_question(preferred_language, current_question_key, user_data[user_id]['question_num']),
                                 reply_markup=markup)

        elif call.data in ['0','1','2','3']:
            callback_question_num = int(call.message.text[:2])
            card_key = user_data[user_id]['all_questions'][len(questions)-callback_question_num]
            current_language = 'eng_version' if 'c' in call.message.text[1:4] else 'rus_version'
            user_answer = int(call.data)
            correct_ans_idx = correct_answers_idxs[card_key]

            if user_answer == correct_ans_idx:
                user_data[user_id]['answers'][card_key] = [1, user_answer]
            else:
                user_data[user_id]['answers'][card_key] = [0, user_answer]
            if callback_question_num == len(questions):
                markup = markup_func_redo(current_language, final_question=True)
            else:
                markup = markup_func_redo(current_language)
            bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id,
                                  text=making_question(current_language, card_key, callback_question_num,
                                  True, questions[card_key][current_language]['options'][int(call.data)]), reply_markup=markup)

        elif call.data in ['redo_callback_eng_version', 'redo_callback_rus_version']:
            if user_data[user_id]['finished'] == False:
                callback_question_num = int(call.message.text[:2])
                card_key = user_data[user_id]['all_questions'][len(questions) - callback_question_num]
                language = call.data[14:]
                if callback_question_num == len(questions):
                    markup = markup_func(language, final_question=True)
                else:
                    markup = markup_func(language)
                bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id,
                                      text=making_question(call.data[14:], card_key, callback_question_num),
                                      reply_markup=markup)
                del user_data[user_id]['answers'][card_key]

        elif call.data in ['finish_callback_rus_version', 'finish_callback_eng_version']:
            user_data[user_id]['finished'] = True
            language = call.data[16:]
            markup = final_markup(language)
            answers = user_data[user_id]['answers']
            scores = counting_results(answers)
            correct_results = correct_answers(user_data[user_id]['all_questions'], user_data[user_id]['answers'])
            user_data[user_id]['results'] = [scores, correct_results]
            bot.send_message(chat_id=user_id, text=finish_text(language, scores, correct_results), reply_markup=markup)
        with open('data.json', 'w') as file:
            json.dump(user_data, file)




bot.polling()