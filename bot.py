import json
from random import sample

import telebot
from telebot import types

from info import *

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
        # генерируем случайный список из ключей вопросов из questions из модуля info
        random_questions = sample(list(questions.keys()), len(questions))

        user_data[user_id]['all_questions'] = random_questions # сортируем все вопросы в случайном порядке
        user_data[user_id]['unpopped_questions'] = random_questions.copy() # отсюда мы будем "попать" по одному вопросу
        user_data[user_id]['question_num'] = 0 # здесь мы будем смотреть на каком вопросе мы остановились
        user_data[user_id]['answers'] = {} # здесь мы будем записывать ответ и правльность пользователя по вопросу
        user_data[user_id]['current_question_key'] = None # здесь мы записываем ключ последнего вопроса из questions из info
        user_data[user_id]['finished'] = False # проверяем, завершилась ли программа или нет
        user_data[user_id]['preferred_language'] = 'rus_version' # записываем предпочтительный пользователю язык
        user_data[user_id]['results'] = ['results', 'correct_answers'] # записываем результаты и правильные ответы

        # вступление у нас по умолчанию начинается на русском с возможностью перевода на английский
        markup = markup_func_introduction('rus_version')
        bot.send_message(message.chat.id, msg_intr_rus_version, reply_markup=markup)

        # записываем в файл при вызове команды /start
        with open('data.json', 'w') as file:
            json.dump(user_data, file)
    else:

        # для команды /help, тут мы уже смотрим на предпочтительный язык пользователя и выдаем текст на этом языке
        language = user_data[user_id]['preferred_language']
        markup = help_markup(language)
        text = markup_dict[language]['help_text']
        bot.send_message(chat_id=user_id, text=text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = str(call.message.chat.id)

    # callback для самого перевода на английский/русский для команд /start /help
    if call.data in ['intr_eng_version', 'intr_rus_version', 'help_eng_version', 'help_rus_version']:

        # определяем язык для markup_dict из info
        language = call.data[5:]

        if call.data.startswith('help'):
            text = markup_dict[language]['help_text']
            markup = help_markup(language)
        else:
            text = markup_dict[language]['intr_msg_language']
            markup = markup_func_introduction(language)

        # Если наш пользователь сменил язык в команде /start или /help, то наш язык по умолчанию меняется,
        # все следующие вопросы и команды по умолчанию будут на языке по умолчанию🤔
        user_data[user_id]['preferred_language'] = language

        # Здесь мы меняем сообщение, чтобы оно было на нужном языке
        bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id,
                              text=text,
                              reply_markup=markup)

    # Callback для перевода на английский/русский самого конца программы(когда выводится результат пользователя)
    elif call.data in ['finish_eng_version', 'finish_rus_version']:

        language = call.data[7:]
        markup = final_markup(language)

        # Добавляю исключение для случая, если пользователь завершил тест и начал новый,
        # user_data[user_id]['results'] обновлятся если пользователь в таком случае захочет перевести результат
        # на другой язык, то выдаст ошибку.
        try:
            scores = user_data[user_id]['results'][0]
            correct_results = user_data[user_id]['results'][1]
            bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id,
                                  text=finish_text(language, scores, correct_results), reply_markup=markup)
        except:
            pass

    # Callback для перевода на английский/русский либо вопроса со всеми кнопками выбора варианта ответа,
    # либо перевод на английский/русский уже решенного вопроса.
    elif call.data in ['rus_version', 'redo_rus_version', 'eng_version', 'redo_eng_version',]:

        # внизу мы определяем номер вопроса для пользователя(в первой строке)
        callback_question_num = int(call.message.text[:2]) # т.к. у нас первые символы в сообщении - это номер вопроса
        # определяем ключ вопроса из questions из модуля info
        card_key = user_data[user_id]['all_questions'][len(questions) - callback_question_num] # Мы идем задом наперед,
        # потому что мы используем метод pop для выбора следующего вопроса из user_data[user_id]['unpopped_questions'].

        # Если мы переводим текст уже решенного вопроса.
        if call.data in ['redo_rus_version', 'redo_eng_version']:

            language = call.data[5:]
            redo = True # эта переменная означает, что мы будем переводить на другой язык уже решенный вопрос
            # Определяем выбранный пользователем ответ.
            chosen_option_index = user_data[user_id]['answers'][card_key][1]
            redo_answer = questions[card_key][language]['options'][chosen_option_index]

            # Если мы добрались до последнего вопроса, то наш markup будет отличаться от обычного
            if user_data[user_id]['question_num'] == len(questions):
                markup = markup_func_redo(language, final_question=True)
            else:
                markup = markup_func_redo(language)

        # Если мы переводим обычный нерешенный вопрос.
        else:
            redo = False
            redo_answer = False
            language = call.data

            # Если наш вопрос последний, то наш markup будет отличаться от обычного
            if user_data[user_id]['question_num'] == len(questions):
                markup = markup_func(call.data, final_question=True)
            else:
                markup = markup_func(call.data)

        # Этот блок нужен для определенной фичи: если пользователь перевел свой текущий вопрос на другой язык, то
        # мы запоминаем его выбор и следующие вопросы по умолчанию будут на предпочтительном ему языке
        # если же пользователь перевел уже пройденный им вопрос на другой язык, то язык по умолчанию не меняется.
        if card_key == user_data[user_id]['current_question_key']:
            user_data[user_id]['preferred_language'] = language
        user_data[user_id]['language_of_question'] = language

        bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id,
                              text=making_question(language, card_key, callback_question_num,
                                                   redo, redo_answer),
                              reply_markup=markup)

    # Если наш пользователь завершил тест, то он не сможет пользоваться следующими кнопками.
    if not user_data[user_id]['finished']:

        # Кнопка следующего вопроса.
        if call.data == 'next_question':
            if user_data[user_id]['unpopped_questions']: # Если у нас остались еще вопросы.

                user_data[user_id]['question_num'] += 1
                user_data[user_id]['current_question_key'] = user_data[user_id]['unpopped_questions'].pop()
                current_question_key = user_data[user_id]['current_question_key']
                preferred_language = user_data[user_id]['preferred_language']

                if user_data[user_id]['question_num'] == len(questions):
                    markup = markup_func(preferred_language, final_question=True)
                else:
                    markup = markup_func(preferred_language)

                bot.send_message(chat_id=user_id,
                                 text=making_question(preferred_language, current_question_key,
                                                      user_data[user_id]['question_num']), reply_markup=markup)

        # Кнопки ответов.
        elif call.data in ['0','1','2','3']:

            callback_question_num = int(call.message.text[:2])
            card_key = user_data[user_id]['all_questions'][len(questions)-callback_question_num]
            # определяем язык сообщения
            current_language = 'eng_version' if 'c' in call.message.text[1:4] else 'rus_version'
            user_answer = int(call.data)
            correct_ans_idx = correct_answers_idxs[card_key]
            # текст выбранного ответа
            redo_answer = questions[card_key][current_language]['options'][int(call.data)]

            if user_answer == correct_ans_idx:
                user_data[user_id]['answers'][card_key] = [1, user_answer]
            else:
                user_data[user_id]['answers'][card_key] = [0, user_answer]

            if callback_question_num == len(questions):
                markup = markup_func_redo(current_language, final_question=True)
            else:
                markup = markup_func_redo(current_language)

            bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id,
                                  text=making_question(current_language, card_key, callback_question_num, redo=True,
                                                       redo_answer=redo_answer),
                                  reply_markup=markup)

        # Кнопки для отката вопроса(возможность пользователя перерешать вопрос, если он уже выбрал ответ).
        elif call.data in ['redo_callback_eng_version', 'redo_callback_rus_version']:

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

            # Если мы использовали кнопку "Решить заново" для вопроса, то мы удаляем прошлый ответ пользователя.
            del user_data[user_id]['answers'][card_key]

        # Кнопки для вывода результата теста
        elif call.data in ['finish_callback_rus_version', 'finish_callback_eng_version']:

            user_data[user_id]['finished'] = True
            language = call.data[16:]
            answers = user_data[user_id]['answers']
            scores = counting_results(answers)
            correct_results = correct_answers(user_data[user_id]['all_questions'], user_data[user_id]['answers'])
            user_data[user_id]['results'] = [scores, correct_results]

            markup = final_markup(language)
            bot.send_message(chat_id=user_id, text=finish_text(language, scores, correct_results), reply_markup=markup)

        with open('data.json', 'w') as file:
            json.dump(user_data, file)


bot.polling()