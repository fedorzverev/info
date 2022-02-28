from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
import sqlite3 as sl


def read(num, tableName):
    try:
        db = sl.connect("project.db")
        cursor = db.cursor()
        query = f"""SELECT path, answer FROM {tableName}
                    ORDER BY RANDOM()
                    LIMIT {num};
                 """
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
    except sl.Error as err:
        print("DB error:", err)
        data = []
    finally:
        if db:
            db.close()
        return data


reply_keyboard = [['/texttasks', '/probability', '/test'], ['/start', '/help']]
reply_keyboard2 = [['/2'], ['/10']]
reply_keyboard3 = [['/start', '/second'], ['/ten', '/eight']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True, resize_keyboard=True)
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=True, resize_keyboard=True)

global c
c = 0
global tasks
tasks = 0


def second1(update, context):
    global tasks
    update.message.reply_text('Сейчас я пришлю Вам пять типовых заданий для тренировки 2 задания из ЕГЭ.',
                              reply_markup=ReplyKeyboardRemove())
    update.message.reply_text('Ответ вводите с использованием десятичной запятой, где это необходимо.',
                              reply_markup=markup3)
    tasks = read(5, 'answerssecond')
    print(len(tasks))
    print(tasks)

    update.message.reply_text(tasks[0][0])

    return 2


def checksecond(update, context):
    global tasks
    global c

    y = update.message.text
    if y == tasks[0][1]:
        c += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(y)
    update.message.reply_text(tasks[1][0])
    return 3


def checksecond2(update, context):
    global tasks, c
    y = update.message.text
    if y == tasks[1][1]:
        c += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(y)
    update.message.reply_text(tasks[2][0])
    return 4


def checksecond3(update, context):
    global tasks, c
    y = update.message.text
    if y == tasks[2][1]:
        c += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(y)
    update.message.reply_text(tasks[3][0])
    return 5


def checksecond4(update, context):
    global tasks, c
    y = update.message.text
    if y == tasks[3][1]:
        c += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(y)
    update.message.reply_text(tasks[4][0])
    return 6


def checksecond5(update, context):
    global tasks, c
    y = update.message.text
    if y == tasks[4][1]:
        c += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(y)
    update.message.reply_text(f"Ваша оценка {c} из 5")
    return ConversationHandler.END


global taskss
taskss= 0
global co

co=0
print(taskss)
def ten(update, context):
    global taskss

    taskss = read(5, 'answerten')
    update.message.reply_text('Сейчас я пришлю Вам пять типовых заданий для тренировки 10 задания из ЕГЭ.',
                              reply_markup=ReplyKeyboardRemove())
    update.message.reply_text('Ответ вводите с использованием десятичной запятой, где это необходимо.',
                              reply_markup=markup3)


    print(taskss)

    update.message.reply_text(taskss[0][0])

    return 2


def checkten(update,context):
    global taskss
    global co
    x = update.message.text
    print('dghjsfjwd')
    print(x)
    if x == taskss[0][1]:
        co += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')


    update.message.reply_text(taskss[1][0])
    return 3


def checkten2(update, context):
    global taskss, co
    x = update.message.text
    if x == taskss[1][1]:
        co += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(x)
    update.message.reply_text(taskss[2][0])
    return 4


def checkten3(update, context):
    global taskss, co
    x = update.message.text
    if x == taskss[2][1]:
        co += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(x)
    update.message.reply_text(taskss[3][0])
    return 5


def checkten4(update, context):
    global taskss, co
    x = update.message.text
    if x == taskss[3][1]:
        co += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(x)
    update.message.reply_text(taskss[4][0])
    return 6


def checkten5(update, context):
    global taskss, co
    x = update.message.text
    if x == taskss[4][1]:
        co += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(x)
    update.message.reply_text(f"Ваша оценка {co} из 5")
    return ConversationHandler.END

global tasksss,cou
tasksss=0
cou=0

def eight(update, context):
    global tasksss

    tasksss = read(5, 'answerseight')
    update.message.reply_text('Сейчас я пришлю Вам пять типовых заданий для тренировки 10 задания из ЕГЭ.',
                              reply_markup=ReplyKeyboardRemove())
    update.message.reply_text('Ответ вводите с использованием десятичной запятой, где это необходимо.',
                              reply_markup=markup3)

    print(tasksss)

    update.message.reply_text(tasksss[0][0])

    return 2

def check81(update,context):
    global tasksss
    global cou
    x = update.message.text
    print('dghjsfjwd')
    print(x)
    if x == tasksss[0][1]:
        cou += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    update.message.reply_text(tasksss[1][0])
    return 3


def check82(update,context):
    global tasksss, cou
    x = update.message.text
    if x == tasksss[1][1]:
        cou += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(x)
    update.message.reply_text(tasksss[2][0])
    return 4

def check83(update,context):
    global tasksss, cou
    x = update.message.text
    if x == tasksss[2][1]:
        cou += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(x)
    update.message.reply_text(tasksss[3][0])
    return 5

def check84(update,context):
    global tasksss, cou
    x = update.message.text
    if x == tasksss[3][1]:
        cou += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(x)
    update.message.reply_text(tasksss[4][0])
    return 6

def check85(update,context):
    global tasksss, cou
    x = update.message.text
    if x == tasksss[4][1]:
        co += 1
        update.message.reply_text('Верно!')
    else:
        update.message.reply_text('Ошибка')

    print(x)
    update.message.reply_text(f"Ваша оценка {cou} из 5")
    return ConversationHandler.END







def test(update, context):
    update.message.reply_text('Этот раздел '
                              'создан для проверки изученных Вами тем.'
                              'Для проверки по второму заданию пропишите /second, для проверки по десятому заданию пропишите /ten '
                              '  для проверки по заданию 8(текстовые задачи) отправьте команду /eight',
                              reply_markup=markup3)


def help(update, context):
    update.message.reply_text('Бот находится на стадии постоянного совершенствования и доработки,на данный момент '
                              'доступны эти темы: Теория вероятностей(/probability) и Текстовые задачи(/texttasks ).'
                              'В разделе(/test) Вы можете найти задания для проверки усвоенного материала.')


def start(update, context):
    update.message.reply_text('Привет, я бот, который создан помочь тебе подготовиться к профильному ЕГЭ по '
                              'математике, напиши /help, чтобы получить инструкцию по пользованию мной.',
                              reply_markup=markup)


def choose3(update, context):
    s = update.message.text
    if s == '2':
        update.message.reply_text('https://www.youtube.com/watch?v=ROGuFprkRNc  '
                                  'https://www.youtube.com/watch?v=5wOUgudXFR0  '
                                  'https://www.youtube.com/watch?v=EtURAiGhll4   '
                                  'https://www.youtube.com/watch?v=-NacMT9bw2Q  '
                                  'https://www.youtube.com/watch?v=JToApxdNXns   '
                                  'https://www.youtube.com/watch?v=jjJMxRsy_Nc')
    elif s == '1':
        update.message.reply_text('https://disk.yandex.ru/i/4hFcBT7nmLHWrQ')
    elif s == '3':
        update.message.reply_text('https://disk.yandex.ru/i/joOoh7TJt6i2mg '
                                  'https://disk.yandex.ru/i/j5FMHDc7MUfiXw')
    elif s == '4':
        update.message.reply_text('https://disk.yandex.ru/i/joOoh7TJt6i2mg '
                                  'https://disk.yandex.ru/i/j5FMHDc7MUfiXw')
        update.message.reply_text('https://disk.yandex.ru/i/4hFcBT7nmLHWrQ')
        update.message.reply_text('https://www.youtube.com/watch?v=ROGuFprkRNc  '
                                  'https://www.youtube.com/watch?v=5wOUgudXFR0  '
                                  'https://www.youtube.com/watch?v=EtURAiGhll4   '
                                  'https://www.youtube.com/watch?v=-NacMT9bw2Q  '
                                  'https://www.youtube.com/watch?v=JToApxdNXns   '
                                  'https://www.youtube.com/watch?v=jjJMxRsy_Nc')

    update.message.reply_text('После ознакомления с теорией, рекомендуем попрактиковаться на этих заданиях.'
                              ' https://learningapps.org/view7471561 \n'
                              'https://learningapps.org/view7471358', reply_markup=markup)

    return ConversationHandler.END


def texttasks(update, context):
    update.message.reply_text('В данном разделе вы научитесь решать 8 задание из ЕГЭ, а именно текстовые задачи.Если '
                              'вы хотите получить теорию в виде текстового файла, отправьте боту 1,если в виде '
                              'youtube ролика-2, презентацию бот выдаст по цифре 3. Для получения и видеороликов,'
                              'и презентации, и текстового файла отправьте боту цифру 4.',
                              reply_markup=ReplyKeyboardRemove())
    return 2


def probability(update, context):
    update.message.reply_text('В данном разделе вы научитесь решать 2 и 10 задания из ЕГЭ, ориентированные на '
                              'классическое определение вероятности(2 задание(/2)) и на вероятности сложных событий(10 '
                              'задание(/10)).Если Вы не знакомы с данной темой, рекомендую начать со 2 задания.',
                              reply_markup=ReplyKeyboardRemove())
    update.message.reply_text('Выберите задание на клавиатуре:', reply_markup=markup2)


def choose1(update, context):
    t = update.message.text
    if t == '2':
        update.message.reply_text('https://www.youtube.com/watch?v=EIjvQrNJt9Y')
    elif t == '1':
        update.message.reply_text("https://disk.yandex.ru/i/qeoEYsr-3JI_kQ")
    elif t == '3':
        update.message.reply_text('https://disk.yandex.ru/i/W7uI-83BEreA6Q')
    elif t == '4':
        update.message.reply_text('https://www.youtube.com/watch?v=EIjvQrNJt9Y')
        update.message.reply_text('https://disk.yandex.ru/i/W7uI-83BEreA6Q')
        update.message.reply_text("https://disk.yandex.ru/i/qeoEYsr-3JI_kQ")

    update.message.reply_text('После ознакомления с теорией, рекомендуем попрактиковаться на этих заданиях.'
                              ' https://learningapps.org/watch?v=prbt4pbbk22 \n'
                              , reply_markup=markup)

    return ConversationHandler.END


def easyprobability(update, context):


    update.message.reply_text('Если вы хотите получить теорию в виде текстового файла, отправьте боту 1,если в '
                              'виде youtube ролика-2, презентацию бот выдаст по цифре 3. Для получения и презентации,'
                              'и текстового файла отправьте боту цифру 4.', reply_markup=ReplyKeyboardRemove())

    return 2


def choose2(update, context):
    z = update.message.text
    if z == '2':
        update.message.reply_text('https://www.youtube.com/watch?v=0_1SDDW032c')
    elif z == '1':
        update.message.reply_text("https://disk.yandex.ru/d/LYHNYbMIUvEeUQ ")
    elif z == '3':
        update.message.reply_text('https://disk.yandex.ru/i/W7uI-83BEreA6Q')

    elif z == '4':
        update.message.reply_text('https://disk.yandex.ru/i/W7uI-83BEreA6Q')
        update.message.reply_text("https://disk.yandex.ru/d/LYHNYbMIUvEeUQ ")
        update.message.reply_text('https://www.youtube.com/watch?v=0_1SDDW032c')

    update.message.reply_text('После ознакомления с теорией, рекомендуем попрактиковаться на этих заданиях.'
                              ' https://learningapps.org/watch?v=pujpfz61t22 \n'
                              , reply_markup=markup)

    return ConversationHandler.END


def hardprobability(update, context):
    update.message.reply_text('Если вы хотите получить теорию в виде текстового файла, отправьте боту 1, а если в '
                              'виде youtube ролика-2, презентацию бот выдаст по цифре 3. Для получения и презентации, '
                              'и текстового файла отправьте боту цифру 4.', reply_markup=ReplyKeyboardRemove())
    x = update.message.text

    return 2


def main(DELETE=None):
    updater = Updater('', use_context=True)
    dp = updater.dispatcher

    conv_handler5 = ConversationHandler(
        entry_points=[CommandHandler('ten', ten)],
        states={1: [MessageHandler(Filters.text, ten)], 2: [MessageHandler(Filters.text, checkten)],
                3: [MessageHandler(Filters.text, checkten2)], 4: [MessageHandler(Filters.text, checkten3)],
                5: [MessageHandler(Filters.text, checkten4)], 6: [MessageHandler(Filters.text, checkten5)]},
        fallbacks=[CommandHandler('stop', start)]

    )

    conv_handler6=ConversationHandler(
        entry_points=[CommandHandler('eight', eight)],
        states={1: [MessageHandler(Filters.text, eight)], 2: [MessageHandler(Filters.text, check81)],
                3: [MessageHandler(Filters.text, check82)], 4: [MessageHandler(Filters.text, check83)],
                5: [MessageHandler(Filters.text, check84)], 6: [MessageHandler(Filters.text, check85)]},
        fallbacks=[CommandHandler('stop', start)]

    )

    conv_handler4 = ConversationHandler(
        entry_points=[CommandHandler('second', second1)],
        states={1: [MessageHandler(Filters.text, second1)], 2: [MessageHandler(Filters.text, checksecond)],
                3: [MessageHandler(Filters.text, checksecond2)], 4: [MessageHandler(Filters.text, checksecond3)],
                5: [MessageHandler(Filters.text, checksecond4)], 6: [MessageHandler(Filters.text, checksecond5)]},
        fallbacks=[CommandHandler('stop', start)]

    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('2', easyprobability)],
        states={1: [MessageHandler(Filters.text, easyprobability)], 2: [MessageHandler(Filters.text, choose1)]},
        fallbacks=[CommandHandler('stop', start)]

    )
    conv_handler3 = ConversationHandler(
        entry_points=[CommandHandler('texttasks', texttasks)],
        states={1: [MessageHandler(Filters.text, texttasks)], 2: [MessageHandler(Filters.text, choose3)]},
        fallbacks=[CommandHandler('stop', start)]
    )
    conv_handler2 = ConversationHandler(
        entry_points=[CommandHandler('10', hardprobability)],
        states={1: [MessageHandler(Filters.text, hardprobability)], 2: [MessageHandler(Filters.text, choose2)]},
        fallbacks=[CommandHandler('stop', start)]
    )
    dp.add_handler(conv_handler6)
    dp.add_handler(conv_handler5)
    dp.add_handler(conv_handler4)
    dp.add_handler(conv_handler3)

    dp.add_handler(conv_handler2)
    dp.add_handler(conv_handler)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("texttasks", texttasks))
    dp.add_handler(CommandHandler("probability", probability))
    dp.add_handler(CommandHandler("2", easyprobability))
    dp.add_handler(CommandHandler("10", hardprobability))
    dp.add_handler(CommandHandler('ten', ten))
    dp.add_handler(CommandHandler('eight', eight))
    dp.add_handler(CommandHandler('second', second1))
    dp.add_handler(CommandHandler('test', test))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
