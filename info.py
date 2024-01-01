from telebot import types

questions = {
    'ml_1': {
        'rus_version': {
            'question': 'Какая главная цель машинного обучения?',
            'options': [
                        'Захватить мир🤖🌐🚀',
                        'Предсказать результат по входным данных📊🔮',
                        'Генерировать прикольные картинки🖼️😊',
                        'Научить компьютер думать как человек🤖✨'
                        ],
            'correct_ans': 'Предсказать результат по входным данных📊🔮'
        },
        'eng_version': {
            'question': 'What is the primary goal of machine learning?',
            'options': [
                        'To conquer the World🤖🌐🚀',
                        'To predict a result given an input data📊🔮',
                        'To generate funny images🖼️😊',
                        "To make computers to think like humans do🤖✨"
                        ],
            'correct_ans': 'To predict a result given an input data📊🔮'
        },
    },
    'ml_2': {
        'rus_version': {
            'question': 'Какая цель у тренировочного набора данных в машинном обучении?',
            'options': [
                        'Оценить работу модели📊👩‍💻',
                        'Обучить модель путем настройки ее параметров🛠️🤖📚',
                        'Обучить набор данных для модели📖🤖🔍',
                        'Набрать тренировку для цели в машинном обучении😵‍💫🌀🤯'
                        ],
            'correct_ans': 'Обучить модель путем настройки ее параметров🛠️🤖📚'
        },
        'eng_version': {
            'question': 'What is the purpose of a training set in machine learning?',
            'options': [
                        'To evaluate the performance of a model📊👩‍💻',
                        'To train a model by adjusting its parameters🛠️🤖📚',
                        'To train a set to feed it into the model📖🤖🔍',
                        "To set a train for an aim in machine learning😵‍💫🌀🤯"
                        ],
            'correct_ans': 'To train a model by adjusting its parameters🛠️🤖📚'
        },
    },
    'ml_3': {
        'rus_version': {
            'question': 'Какие основные типы машинного обучения существуют?',
            'options': [
                        'Обучение с учителем, обучение без учителя и обучение с подкреплением📚👨‍🏫🔄',
                        'Распознавание изображений, обработка естественного языка и распознавание речи🖼️📝🗣️',
                        'Регрессия, классификация и кластеризация📈🏷️🔍',
                        'Пунктуация, маршрутизация, коллаборация📌🛣️🤝'
                        ],
            'correct_ans': 'Обучение с учителем, обучение без учителя и обучение с подкреплением📚👨‍🏫🔄'
        },
        'eng_version': {
            'question': 'What are the main types of machine learning?',
            'options': [
                        'Supervised learning, unsupervised learning, and reinforcement learning📚👨‍🏫🔄',
                        'Image recognition, natural language processing, and speech recognition🖼️📝🗣',
                        'Regression, classification, and clustering📈🏷️🔍',
                        "Punctuation, routing, collaboration📌🛣️🤝"
                        ],
            'correct_ans': 'Supervised learning, unsupervised learning, and reinforcement learning📚👨‍🏫🔄'
        }
    },
    'ml_4': {
        'rus_version': {
            'question': 'Какой алгоритм является базовым для решения задач классификации в машинном обучении',
            'options': [
                        'Линейная регрессия📈🔍',
                        'Бинарный поиск🔍👀🔍',
                        'Логистическая регрессия📈🔍🧐',
                        'Алгоритм Евклида🧮📏'
                        ],
            'correct_ans': 'Логистическая регрессия📈🔍🧐'
        },
        'eng_version': {
            'question': 'What is the most basic algorithm for classification tasks in machine learning?',
            'options': [
                        'Linear regression📈🔍',
                        'Binary search🔍👀🔍',
                        'Logistic regression📈🔍🧐',
                        "Euclid algorithm🧮📏"
                        ],
            'correct_ans': 'Logistic regression📈🔍🧐'
        }
    },
    'ml_5': {
        'rus_version': {
            'question': 'Какой алгоритм является базовым для задач регрессии в машинном обучении?',
            'options': [
                        "Логистическая регрессия📈🔍🧐",
                        "Линейная регрессия📈🔍",
                        "Арифметическая прогрессия🔢🔄",
                        "Великая Депрессия📉😞"
                        ],
            'correct_ans': 'Линейная регрессия📈🔍'
        },
        'eng_version': {
            'question': 'Which algorithm is basic for regression tasks in machine learning?',
            'options': [
                        'Logistic regression📈🔍🧐',
                        'Linear regression📈🔍',
                        'Arithmetic progression🔢🔄',
                        "Great Depression📉😞"
                        ],
            'correct_ans': 'Linear regression📈🔍'
        }
    },
    'dl_6': {
        'rus_version': {
            'question': 'Где используются сверточные нейронные сети в своем большинстве?',
            'options': [
                        'Обработка изображений🖼️🔄👁️',
                        'Обработка языка📝🔄👄',
                        'Обработка звука🔊🔄👂',
                        "В рыболовном деле🎣🤔"
            ],
            'correct_ans': 'Обработка изображений🖼️🔄👁️'
        },
        'eng_version': {
            'question': 'Where convolutional neural networks are used most of all?',
            'options': [
                        'Image processing🖼️🔄👁️',
                        'Language processing📝🔄👄',
                        'Audio processing🔊🔄👂',
                        "Fishing business🎣🤔"
            ],
            'correct_ans': 'Image processing🖼️🔄👁️'
        }
    },
    'dl_7': {
        'rus_version': {
            'question': 'Что лежит в основе архитектуры больших языковых моделей?',
            'options': [
                        'Трансформер🤖🔄',
                        'Мегатрон🤖🚀',
                        'Чудо✨😲',
                        "Язык🗣️📚"
                        ],
            'correct_ans': 'Трансформер🤖🔄'
        },
        'eng_version': {
            'question': 'What is lying in the basis of large language models?',
            'options': [
                'Transformer🤖🔄',
                'Megatron🤖🚀',
                'Miracle✨😲',
                "Language🗣️📚"
                        ],
            'correct_ans': 'Transformer🤖🔄'
        }
    },
    'dl_8': {
        'rus_version': {
            'question': 'Какая цель использования функции-активации в нейронных сетях?',
            'options': [
                'Внести нелинейность в нашу модель🔄📈🤖',
                'Активировать нашу функцию🚀🔛🧠',
                'Увеличить переобучение модели📈📈📈🔄🤖',
                'Уменьшить переобучение модели📉🔄🤖'
            ],
            'correct_ans': 'Внести нелинейность в нашу модель🔄📈🤖'
        },
        'eng_version': {
            'question': 'What is the purpose of an activation function in a neural network?',
            'options': [
                'To introduce non-linearity to the model🔄📈🤖',
                'To activate our function🚀🔛🧠',
                'To increase overfitting of the model📈📈📈🔄🤖',
                "To decrease overfitting of the model📉🔄🤖"
                        ],
            'correct_ans': 'To introduce non-linearity to the model🔄📈🤖'
        }
    },
    'dl_9': {
        'rus_version': {
            'question': 'Какая роль у метода обратного распространения ошибки в обучении нейронной сети?',
            'options': [
                'Обновление весов нейронной сети на основе функции потери🔄🏋️‍♂️🤖',
                'Рассылка ошибок нейронной сети всем друзьям📧❌🤖👫',
                'Регулиризировать нейронную сеть при переобучении📉🔄🤖🔒',
                'Выдать ответ в соответствии с входными данными📤🤖🔄📥'
            ],
            'correct_ans': 'Обновление весов нейронной сети на основе функции потерь🔄🏋️‍♂️🤖'
        },
        'eng_version': {
            'question': 'What is the role of backpropagation in training a neural network?',
            'options': [
                'To update weights of neural network based on loss function🔄🏋️‍♂️🤖',
                'To propagate errors of neural networks straight to our friends',
                'To regularize neural network when it is overfitted📉🔄🤖🔒',
                "To output corresponding to the input data📤🤖🔄📥"
                        ],
            'correct_ans': 'To update weights of neural network based on loss function🔄🏋️‍♂️🤖'
        }
    },
    'dl_10': {
        'rus_version': {
            'question': 'Какова цель рекуррентной нейронной сети (RNN) в глубоком обучении?',
            'options': [
                'Классификация изображений🖼️🏷️🤖',
                'Обработка последовательных данных и улавливание зависимостей🔄📊🤖',
                'Оптимизация параметров модели📈🔍🔧',
                'Кластеризация📊🔄🔍'
            ],
            'correct_ans': 'Обработка последовательных данных и улавливание зависимостей🔄📊🤖'
        },
        'eng_version': {
            'question': 'What is the purpose of a recurrent neural network (RNN) in deep learning?',
            'options': [
                'To classify images🖼️🏷️🤖',
                'To process sequential data and capture dependencies🔄📊🤖',
                'To optimize model parameters📈🔍🔧',
                "To perform clustering📊🔄🔍"
                        ],
            'correct_ans': 'To process sequential data and capture dependencies🔄📊🤖'
        }
    },
    'alg_11': {
        'rus_version': {
            'question': 'Для чего нужно условное обозначение "О" большое?',
            'options': [
                'Выражать удивление, если встречаешь классный алгоритм🤩👾🔮',
                'Обозначение для описания лучшего сценария скорости выполнения алгоритма📈😄',
                'Обозначение для описания среднего сценария скорости выполнения алгоритма⏰📊🤷‍♂',
                'Обозначение для описания худшего сценария скорости выполнения алгоритма📉🤔'
            ],
            'correct_ans': 'Обозначение для описания худшего сценария скорости выполнения алгоритма📉🤔'
        },
        'eng_version': {
            'question': 'What is a big O notation?',
            'options': [
                'To express your wonder when you meet a cool algorithm🤩👾🔮',
                'Notation for describing best case scenario of the running time of an algorithm📈😄',
                'Notation for describing average case scenario of the running time of an algorithm⏰📊🤷‍♂',
                "Notation for describing worst case scenario of the running time of an algorithm📉🤔"
                        ],
            'correct_ans': 'Notation for describing worst case scenario of the running time of an algorithm📉🤔'
        }
    },
    'alg_12': {
        'rus_version': {
            'question': 'Для чего используется алгоритм Дейкстры?',
            'options': [
                'Сортировка элементов в массиве📈🔍🔄',
                'Поиск элемента в связном списке🔍📝🔗',
                'Нет такого алгоритма😠👿',
                'Поиск кратчайшего пути во взвешенном графе🚗🛣️🔍'
            ],
            'correct_ans': 'Поиск кратчайшего пути во взвешенном графе🚗🛣️🔍'
        },
        'eng_version': {
            'question': "What is the purpose of Dijkstra's algorithm?",
            'options': [
                'Sorting elements in an array📈🔍🔄',
                'Searching for an element in a linked list🔍📝🔗',
                "There is no such algorithm, don't confuse me😠👿",
                "Finding the shortest path in a weighted graph🚗🛣️🔍"
                        ],
            'correct_ans': 'Finding the shortest path in a weighted graph🚗🛣️🔍'
        }
    },
    'alg_13': {
        'rus_version': {
            'question': 'Какой алгоритм поиска известен своей эффективностью при поиске в отсортированном массиве путем многократного деления интервала поиска пополам?',
            'options': [
                'Линейный поиск🔍🔄',
                'Поиск в глубину🔍🌲🕵️‍',
                'Бинарный поиск🔍👀🔄',
                'Поиск в ширину🔍🌊🔄'
            ],
            'correct_ans': 'Бинарный поиск🔍👀🔄'
        },
        'eng_version': {
            'question': 'Which searching algorithm is known for its efficiency in searching a sorted array by repeatedly dividing the search interval in half?',
            'options': [
                'Linear Search🔍🔄',
                'Depth-First Search🔍🌲🕵️‍',
                'Binary Search🔍👀🔄',
                "Depth-First Search🔍🌊🔄"
                        ],
            'correct_ans': 'Binary Search🔍👀🔄'
        }
    },
    'alg_14': {
        'rus_version': {
            'question': 'Что такое рекурсия в программировании?',
            'options': [
                'Техника решения проблемы путем использования циклов🔁🛠️',
                'Специальный оператор⚙️🔧',
                'Термин, означающий вызов функции самой себя🔄📞🤖',
                'Термин, означающий смену курса в идее построения программы🔄🛣️🔄'
            ],
            'correct_ans': 'Термин, означающий вызов фунции самой себя🔄📞🤖'
        },
        'eng_version': {
            'question': 'What is recursion in programming?',
            'options': [
                'Technic of solving problems iteratively🔁🛠️',
                'Special operator⚙️🔧',
                'A term which means a function that calls itself🔄📞🤖',
                'A term meaning a change of course in the idea of building a program🔄🛣️🔄'
                        ],
            'correct_ans': 'A term which means a function that calls itself🔄📞🤖'
        }
    },
    'alg_15': {
        'rus_version': {
            'question': 'Дайте определение термину "алгоритм"',
            'options': [
                'Компонент аппаратного обеспечения компьютера🖥️🔧🔍',
                'Язык программирования🗣️‍💻📝',
                'Набор действий для решения определенной проблемы🤔📊🔄',
                'Зашифрованный язык общения с компьютером🔒🤖📡'
            ],
            'correct_ans': 'Набор действий для решения определенной проблемы🤔📊🔄'
        },
        'eng_version': {
            'question': 'What is an algorithm by its definition?',
            'options': [
                'Component of computer software🖥️🔧🔍',
                'Programming language🗣️‍💻📝',
                'Set of actions for solving certain problem🤔📊🔄',
                "Encrypted language for communication with computer🔒🤖📡"
                        ],
            'correct_ans': 'Set of actions for solving certain problem🤔📊🔄'
        }
    },
}

# Внизу мы создаем словарь, где каждому вопросу будет соответствовать индекс правильного ответа из questions.
correct_answers_idxs = {}
for key, value in questions.items():
    correct_answers_idxs[key] = value['eng_version']['options'].index(value['eng_version']['correct_ans'])

# Вступление
msg_intr_rus_version = '''🤖Добро пожаловать машинно-обученческую бот-анкету!🧠🤖

Приготовьтесь проверить свои знания в увлекательном мире искусственного интеллекта. В этой викторине вас ждут вопросы по различным темам, включая Машинное Обучение, Глубокое Обучение и Алгоритмы. Независимо от того, являетесь ли вы новичком или энтузиастом искусственного интеллекта, испытайте себя!🧠💡'''
msg_intr_eng_version = '''🤖Welcome to the Machine learning Quiz Bot!🧠🤖

Get ready to challenge your knowledge in the fascinating world of artificial intelligence. This quiz covers a range of topics, including Machine Learning, Deep Learning, and Algorithms. Whether you're a beginner or an AI enthusiast, let me try you!🧠💡'''

# Командa /help
help_cmd_eng_version = f'''The test consists of {len(questions)} questions on the topics of "Machine Learning," "Deep Learning," and "Algorithms." At the end of the test, you will receive a message with the results.

The features of the bot are as follows:

📍 Interact using the buttons below each question.
⌨️ No typing required; just click your answers.
🌐 Questions presented in English and Russian for your convenience.
🔄 Feel free to review and change your answers as you go.
📝 User data recorded to enhance your quiz experience.

Good luck!'''
help_cmd_rus_version = f'''Тест включает в себя {len(questions)} вопросов на темы: "Машинное обучение", "Глубокое обучение", "Алгоритмы". В конце теста вам будет выведено сообщение с результатами.
Особенности бота представлены ниже:

 📍 Взаимодействуйте с помощью кнопок под каждым вопросом.
⌨ Никакого ввода с клавиатуры, просто кликайте на ваши ответы.
🌐 Вопросы представлены на английском и русском для вашего удобства.
🔄 Возможность пересматривать и изменять ответы в процессе.
📝 Данные пользователя записываются для улучшения вашего опыта викторины.

Удачи!
'''

# Словарь с названиями кнопок и их callback'ами, а также русскими и английскими текстами для нашего бота.
markup_dict = {'eng_version': {
                    'translate_name': 'Перевести на русский',
                    'translate_callback': 'rus_version',
                    'translate_redo_callback': 'redo_rus_version',
                    'redo_name': 'Answer differently',
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
                    'redo_name': 'Ответить иначе',
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

# Дальше идут функции, относящиеся к генерации текста

# Подсчет результатов пользователя.
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


# Создание текста, где будет показан вопрос, правильный ответ и галочка либо крестик,
# в зависимости от правильности ответа.
def correct_answers(all_questions, answers):

    output = ''''''
    letters = ['A)', 'B)', 'C)', 'D)']

    for i, key in enumerate(all_questions[::-1]):
        if key in answers and answers[key][0] == 1:
            output += f'{i+1}: {letters[correct_answers_idxs[key]]}     ✔\n'
        else:
            output += f'{i+1}: {letters[correct_answers_idxs[key]]}     ❌\n'

    return output


# Создание текста вопроса
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


# Генерируем финальный текст
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
        output = f'''You have finished testing, your results are:

On the subject "machine learning"🤖📚✨ you got {machine_learning}%
On the subject "deep learning"🤖🧠🌐🚀 you got {deep_learning}%
On the subject "algorithms"🔄🤖📊 you got {algorithms}%

Below presented number of question and correct answer:\n'''
        output += correct_answers

    return output


# Дальше идут функции для создания markup'ов.


# Создание markup'a для команды /start.
# Состоит из кнопок "перевести текст" и "начать тест" для русской и английской версии.
def markup_func_introduction(language_vers):
    markup = types.InlineKeyboardMarkup()
    translate_button = types.InlineKeyboardButton(markup_dict[language_vers]['translate_name'],
                                        callback_data=markup_dict[language_vers]['introduction_callback'])
    starting_button = types.InlineKeyboardButton(markup_dict[language_vers]['introduction_starting'],
                                                 callback_data=markup_dict[language_vers]['next_question_callback'])
    markup.add(translate_button)
    markup.add(starting_button)

    return markup


# Markup для команды /help.
# Тут есть только кнопка "перевести текст".
def help_markup(language_vers):

    markup = types.InlineKeyboardMarkup()
    translate_button = types.InlineKeyboardButton(markup_dict[language_vers]['translate_name'],
                                                  callback_data=markup_dict[language_vers]['help_callback'])
    markup.add(translate_button)

    return markup


# Markup для вопроса
# Состоит из кнопок вариантов ответа, перевода вопроса на другой язык и кнопки следующего вопроса.
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

    #  Если наш вопрос последний, то вместо кнопки "следующий вопрос" у нас кнопка "завершить тестирование"
    if not final_question:
        next_question_button = types.InlineKeyboardButton(markup_dict[language_vers]['next_question_name'],
                                                          callback_data=markup_dict[language_vers][
                                                              'next_question_callback'])
        markup.add(next_question_button)
    else:
        finish_button = types.InlineKeyboardButton(markup_dict[language_vers]['finishing'],
                                                   callback_data=markup_dict[language_vers]['finish_callback'])
        markup.add(finish_button)

    return markup


# Markup для сообщения, когда пользователь уже ответил на вопрос.
# У нас есть кнопка "ответить иначе", "перевести вопрос" и "следующий вопрос" или "завершить тестирование"
def markup_func_redo(language_vers, final_question=False):

    markup = types.InlineKeyboardMarkup()
    translate_button = types.InlineKeyboardButton(markup_dict[language_vers]['translate_name'],
                                                  callback_data=markup_dict[language_vers]['translate_redo_callback'])
    redo_button = types.InlineKeyboardButton(markup_dict[language_vers]['redo_name'],
                                             callback_data=markup_dict[language_vers]['redo_callback'])

    markup.add(translate_button)
    markup.add(redo_button)

    # Если наш вопрос последний, то вместо кнопки "следующий вопрос" у нас кнопка "завершить тестирование".
    if not final_question:
        next_question_button = types.InlineKeyboardButton(markup_dict[language_vers]['next_question_name'],
                               callback_data=markup_dict[language_vers]['next_question_callback'])
        markup.add(next_question_button)
    else:
        finish_button = types.InlineKeyboardButton(markup_dict[language_vers]['finishing'],
                                                   callback_data=markup_dict[language_vers]['finish_callback'])
        markup.add(finish_button)

    return markup


# Финальный markup для перевода результатов тестирования.
def final_markup(language_vers):

    translate_button = types.InlineKeyboardButton(markup_dict[language_vers]['translate_name'],
                                callback_data=markup_dict[language_vers]['callback_finish_translate'])
    markup = types.InlineKeyboardMarkup()

    markup.add(translate_button)

    return markup