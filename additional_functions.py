import telebot
from telebot import types
from info import *

markup_dict = {'eng_version': {
                    'translate_name': 'Перевести на русский',
                    'translate_callback': 'rus_version',
                    'translate_redo_callback': 'redo_rus_version',
                    'redo_name': 'try again',
                    'redo_callback': 'redo_callback_eng_version',
                    'next_question_name': 'Next question',
                    'next_question_callback': 'next_question',
                    'introduction_starting': 'Start testing',
                    'introduction_callback': 'intr_rus_version',
                    'card': 'card',
                    'redo_sentence': 'Your answer:',
                    'intr_msg_language': msg_intr_eng_version,
                    'finishing': 'finish the test',
                    'finish_callback': 'finish_callback_eng_version',
                    'callback_finish_translate': 'finish_rus_version',
                    'help_text': help_cmd_eng_version,
                    'help_callback': 'help_rus_version'
},
                'rus_version': {
                    'translate_name': 'Translate to english',
                    'translate_callback': 'eng_version',
                    'translate_redo_callback': 'redo_eng_version',
                    'redo_name': 'Попробовать заново',
                    'redo_callback': 'redo_callback_rus_version',
                    'next_question_name': 'Следующий вопрос',
                    'next_question_callback': 'next_question',
                    'introduction_starting': 'Начать тестирование',
                    'introduction_callback': 'intr_eng_version',
                    'card': 'билет',
                    'redo_sentence': 'Ваш ответ:',
                    'intr_msg_language': msg_intr_rus_version,
                    'finishing': 'завершить тест',
                    'finish_callback': 'finish_callback_rus_version',
                    'callback_finish_translate': 'finish_eng_version',
                    'help_text': help_cmd_rus_version,
                    'help_callback': 'help_eng_version'
                }
}


def making_question(language_vers, key, question_num, redo=False, redo_answer=False):
    output = f'''{question_num} {markup_dict[language_vers]["card"]}\n\n'''
    output += questions[key][language_vers]['question'] + '\n\n'
    letters = ['A)', 'B)', 'C)', 'D)']
    options = questions[key][language_vers]['options']
    for l, o in zip(letters, options):
        output += f'{l} {o}\n'
    if redo == True:
        output += f'\n{markup_dict[language_vers]["redo_sentence"]} {redo_answer}'

    return output


def markup_func(language_vers, final_question=False):
    markup = types.InlineKeyboardMarkup()
    translate_button = types.InlineKeyboardButton(markup_dict[language_vers]['translate_name'],
                                                  callback_data=markup_dict[language_vers]['translate_callback'])
    a_button = types.InlineKeyboardButton('A', callback_data='0')
    b_button = types.InlineKeyboardButton('B', callback_data='1')
    c_button = types.InlineKeyboardButton('C', callback_data='2')
    d_button = types.InlineKeyboardButton('D', callback_data='3')

    markup.row(a_button, b_button)
    markup.row(c_button, d_button)
    markup.add(translate_button)
    if final_question==False:
        next_question_button = types.InlineKeyboardButton(markup_dict[language_vers]['next_question_name'],
                                                          callback_data=markup_dict[language_vers][
                                                              'next_question_callback'])
        markup.add(next_question_button)
    else:
        finish_button = types.InlineKeyboardButton(markup_dict[language_vers]['finishing'],
                                                   callback_data=markup_dict[language_vers]['finish_callback'])
        markup.add(finish_button)
    return markup


def markup_func_introduction(language_vers):
    markup = types.InlineKeyboardMarkup()
    translate_button = types.InlineKeyboardButton(markup_dict[language_vers]['translate_name'],
                                        callback_data=markup_dict[language_vers]['introduction_callback'])
    starting_button = types.InlineKeyboardButton(markup_dict[language_vers]['introduction_starting'],
                                                 callback_data=markup_dict[language_vers]['next_question_callback'])
    markup.add(translate_button)
    markup.add(starting_button)
    return markup


def markup_func_redo(language_vers, final_question=False):
    markup = types.InlineKeyboardMarkup()
    translate_button = types.InlineKeyboardButton(markup_dict[language_vers]['translate_name'],
                                                  callback_data=markup_dict[language_vers]['translate_redo_callback'])
    redo_button = types.InlineKeyboardButton(markup_dict[language_vers]['redo_name'],
                                             callback_data=markup_dict[language_vers]['redo_callback'])

    markup.add(translate_button)
    markup.add(redo_button)
    if final_question == False:
        next_question_button = types.InlineKeyboardButton(markup_dict[language_vers]['next_question_name'],
                                                      callback_data=markup_dict[language_vers]['next_question_callback'])
        markup.add(next_question_button)
    else:
        finish_button = types.InlineKeyboardButton(markup_dict[language_vers]['finishing'],
                                                   callback_data=markup_dict[language_vers]['finish_callback'])
        markup.add(finish_button)
    return markup


def help_markup(language_vers):
    markup = types.InlineKeyboardMarkup()
    translate_button = types.InlineKeyboardButton(markup_dict[language_vers]['translate_name'],
                                                  callback_data=markup_dict[language_vers]['help_callback'])
    markup.add(translate_button)
    return markup


def counting_results(answers):
    machine_learning = 0
    deep_learning = 0
    algorithms = 0
    all_machine_learning = 0
    all_deep_learning = 0
    all_algorithms = 0

    for key, value in answers.items():
        if key.startswith('ml'):
            machine_learning += value[0]
        elif key.startswith('dl'):
            deep_learning += value[0]
        elif key.startswith('alg'):
            algorithms += value[0]

    for key in questions.keys():
        if key.startswith('ml'):
            all_machine_learning += 1
        elif key.startswith('dl'):
            all_deep_learning += 1
        elif key.startswith('alg'):
            all_algorithms += 1

    machine_learning = 100 / all_machine_learning * machine_learning
    deep_learning = 100 / all_deep_learning * deep_learning
    algorithms = 100 / all_algorithms * algorithms
    return (machine_learning, deep_learning, algorithms)

def correct_answers(all_questions, answers):
    output = ''''''
    letters = ['A)', 'B)', 'C)', 'D)']
    for i, key in enumerate(all_questions[::-1]):
        if key in answers and answers[key][0] == 1:
            output += f'{i+1}: {letters[correct_answers_idxs[key]]}     ✔\n'
        else:
            output += f'{i+1}: {letters[correct_answers_idxs[key]]}     ❌\n'
    return output



def final_markup(language_vers):
    translate_button = types.InlineKeyboardButton(markup_dict[language_vers]['translate_name'],
                                callback_data=markup_dict[language_vers]['callback_finish_translate'])
    markup = types.InlineKeyboardMarkup()
    markup.add(translate_button)
    return markup

def finish_text(language_vers, results, correct_answers):
    machine_learning, deep_learning, algorithms = results
    if language_vers == 'rus_version':
        output = f'''Вы завершили тестирование, вот ваши результаты:
        
По теме "машинное обучение"🤖📚✨ вы набрали {machine_learning}%
По теме "глубокое обучение"🤖🧠🌐🚀 вы набрали {deep_learning}%
По теме "алгоритмы"🔄🤖📊 вы набрали {algorithms}%

Внизу представлен номер вопроса и правильный ответ:\n'''
        output += correct_answers
    elif language_vers == 'eng_version':
        output = f'''You have finished testing, your results:
        
On the subject "machine learning"🤖📚✨ you got {machine_learning}%
On the subject "deep learning"🤖🧠🌐🚀 you got {deep_learning}%
On the subject "algorithms"🔄🤖📊 you got {algorithms}%

Below presented number of question and correct answer:\n'''
        output += correct_answers
    return output


