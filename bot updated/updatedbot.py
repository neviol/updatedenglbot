import telebot

import os
import bot
import random
import smtplib

from telebot import types
from flask import Flask, request

TOKEN = ""
# Token of the Bot

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)

MethodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates'.format(token=TOKEN)

greetings = ["Привет", "Хай!", "Хеллоу", "Greetings"]

@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open("static1/Eng.webp", "rb")
    bot.send_sticker(message.chat.id, sti)
    # Sends sticker of English Flag

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Я Новенький! 😀")
    button2 = types.KeyboardButton("Я Ученик! 😎")

    markup.add(button1, button2)

    bot.send_message(message.chat.id,
                     "{0}, {1.first_name}!\nЯ - <b>{2.first_name}</b> , с моей помощью ты можешь записаться на урок и узнать много полезной информации! 🤟".
                     format(random.choice(greetings), message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup)
    # Greets the user


@bot.message_handler(content_types=["text"])
def lalala(message):
    if message.chat.type == "private":
        if message.text == "Я Новенький! 😀":
            markup_new = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Узнать Больше про Учителя")
            button2 = types.KeyboardButton("Узнать Расценку 💲")
            button3 = types.KeyboardButton("Узнать Больше про Урок 📚")
            button4 = types.KeyboardButton("Записаться на Пробный Урок")
            button5 = types.KeyboardButton("◀️Назад")

            markup_new.add(button1, button2, button3, button4, button5)

            bot.send_message(message.chat.id, "Добро пожаловать будущий ученик!", reply_markup=markup_new)

        if message.text == "Я Ученик! 😎":
            markup_student = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Выбрать Время для Урока 🕔")
            button2 = types.KeyboardButton("Узнать Расценку 💲")
            button3 = types.KeyboardButton("◀️Назад")

            markup_student.add(button1, button2, button3)

            bot.send_message(message.chat.id, "Добро пожаловать мой ученик!", reply_markup=markup_student)

        elif message.text == "Записаться на Пробный Урок":

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Сегодня", callback_data='today')
            item2 = types.InlineKeyboardButton("Завтра", callback_data='tomorrow')
            item3 = types.InlineKeyboardButton("На Неделе", callback_data='week')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, "Когда вам было бы удобно?", reply_markup=markup)

        elif message.text == "Узнать Расценку 💲":

            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Записаться на пробный урок!", callback_data='trial_lesson')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             "<b>Цена за Урок</b>:\n\nДетский(4-14 лет)👶 - <b>250 Грн/час</b> \n\n"
                             "Взрослый (15+ лет)👴 - <b>300 Грн/час</b> \n\n\n<b>Специальные Предложения</b>: \n\n"
                             "10 Детский Занятий (по 60 мин) - <b>2000 грн</b> \n\n"
                             "10 Взрослых Занятий (по 60 мин) - <b>2500 грн</b>",
                             parse_mode="html", reply_markup=markup)

        elif message.text == "Узнать Больше про Урок 📚":

            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Записаться на пробный урок!", callback_data='trial_lesson')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             "<b>Пробный Урок:</b>\nПосле 30 минутного пробного урока учитель выяснит какой у вас уровень и подберет под вас и ваши желания курс обучения. \n\n<b>Детский Полный Урок:</b>\nГлавная задача урока с ребёнком это сделать так чтобы весь урок ему было интересно заниматься на аглийском. Дети очень быстро впитывают информацию, и поэтому весь урок ребёнок будет максмально, на сколько он может говорить на английском, и слушать речь Олега. Урок выстроен в таком формате что подача информации идёт в перемешку с различными играми и интересными заданиями.\n\n<b>Взрослый Полный Урок:</b>\nОдин полноценный урок длиться 60 минут. Главная цель урока это погрузить вас в разговорную атмосферу в которой вы будете общаться на английском и обсуждать актуальные темы, разширять свой словарный запас, и учить различные правила в разных интересных формах.\n\n<b>Бонусы:</b>\nКогда вы начинаете заниматься с Олегом, вы не только приобретаете уроки английского, но и куглосуточную поддержку. <b>Что это значит?</b> - Это значит что если вам нужно будет помочь с чем-то вроде написания или редакции какого-то тескста или вам просто нужен будет совет, то Олег всегда будет рад вам помочь.",
                             parse_mode="html", reply_markup=markup)

        elif message.text == "Узнать Больше про Учителя":

            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Записаться на пробный урок!", callback_data='trial_lesson')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             "<b>Твой учитель Олег.</b>\n\nОн 12 лет своей жизни уделил Английскому языку так как учился в Американской Школе. "
                             "Для обучения взрослых и детей он использует современные технологии и идеи а не устаревшие учебнки и зазубрение информации. "
                             "Он имеет опыт в обучении как детей так и взрослых и сам знает что в изучении языков ученики не любят, так как знает он аж пять языков. "
                             "В свободное от изучения Английского время он занимаеться програмированием и поэтому написал мой код сам. "
                             "Я уверен что он будет рад найти время для того чтобы провести с тобой пробный урок. ",
                             parse_mode="html", reply_markup=markup)
        elif message.text == "Выбрать Время для Урока 🕔":

            markup_time = types.InlineKeyboardMarkup(row_width=4)
            item1 = types.InlineKeyboardButton("13:00", callback_data="13")
            item2 = types.InlineKeyboardButton("14:00", callback_data="14")
            item3 = types.InlineKeyboardButton("15:00", callback_data="15")
            item4 = types.InlineKeyboardButton("16:00", callback_data="16")
            item5 = types.InlineKeyboardButton("17:00", callback_data="17")
            item6 = types.InlineKeyboardButton("18:00", callback_data="18")
            item7 = types.InlineKeyboardButton("19:00", callback_data="19")
            item8 = types.InlineKeyboardButton("20:00", callback_data="20")
            item9 = types.InlineKeyboardButton("Ввести свое время", callback_data="sometime")

            markup_time.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)

            bot.send_message(message.chat.id, "Выбирай Время!", reply_markup=markup_time)

        elif message.text == "◀️Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Я Новенький! 😀")
            button2 = types.KeyboardButton("Я Ученик! 😎")

            markup.add(button1, button2)

            bot.send_message(message.chat.id, "Назад", reply_markup=markup)

        else:
            pass


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:

            if call.data == "13":
                time = "13:00"
                client_name = bot.send_message(call.message.chat.id, "Отправь свое имя латинскими буквами! (Пример: Oleg)")
                bot.register_next_step_handler(client_name, take_name_13)

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="13:00", reply_markup=None)

            elif call.data == "14":
                time = "14:00"
                client_name = bot.send_message(call.message.chat.id, "Отправь свое имя латинскими буквами! (Пример: Oleg)")
                bot.register_next_step_handler(client_name, take_name_14)

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="14:00", reply_markup=None)

            elif call.data == "15":
                time = "15:00"
                client_name = bot.send_message(call.message.chat.id, "Отправь свое имя латинскими буквами! (Пример: Oleg)")
                bot.register_next_step_handler(client_name, take_name_15)

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="15:00", reply_markup=None)

            elif call.data == "16":
                time = "16:00"
                client_name = bot.send_message(call.message.chat.id, "Отправь свое имя латинскими буквами! (Пример: Oleg)")
                bot.register_next_step_handler(client_name, take_name_16)

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="16:00", reply_markup=None)

            elif call.data == "17":
                time = "17:00"
                client_name = bot.send_message(call.message.chat.id, "Отправь свое имя латинскими буквами! (Пример: Oleg)")
                bot.register_next_step_handler(client_name, take_name_17)

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="17:00", reply_markup=None)

            elif call.data == "18":
                time = "18:00"
                client_name = bot.send_message(call.message.chat.id, "Отправь свое имя латинскими буквами! (Пример: Oleg)")
                bot.register_next_step_handler(client_name, take_name_18)

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="18:00", reply_markup=None)

            elif call.data == "19":
                time = "19:00"
                client_name = bot.send_message(call.message.chat.id, "Отправь свое имя латинскими буквами! (Пример: Oleg)")
                bot.register_next_step_handler(client_name, take_name_19)

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="19:00", reply_markup=None)

            elif call.data == "20":
                time = "20:00"
                client_name = bot.send_message(call.message.chat.id, "Отправь свое имя латинскими буквами! (Пример: Oleg)")
                bot.register_next_step_handler(client_name, take_name_20)

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="20:00", reply_markup=None)

            elif call.data == "sometime":
                client_time = bot.send_message(call.message.chat.id, "Отправь мне свое имя латинскими буквами и время так как показано в примере.\n \n <b>Пример:</b> Oleg 13:45", parse_mode="html")
                bot.register_next_step_handler(client_time, take_sometime)

            elif call.data == "today" or "tomorrow" or "week" or "trial_lesson":
                phone_answer = bot.send_message(call.message.chat.id, "Отличненько! Отправьте мне свой номер телефона! ☎")
                bot.register_next_step_handler(phone_answer, take_phone)



    except Exception as e:
        print(repr(e))


def take_phone(message):
    if "+380" in message.text or "380" in message.text or "0" in message.text:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("ole.nevidomskyi@gmail.com", "fjpbphzbfdzhdzxg")
        server.sendmail("ole.nevidomskyi@gmail.com", "ole.nevidomskyi@gmail.com",
                        "You Have a New Client\n His Phone Number: " + message.text + "\n")
        server.quit()

        bot.send_message(message.chat.id, "Олег свяжется с вами в течении часа. ☺")
    else:
        bot.send_message(message.chat.id, "Номер должен быть в формате <b>+380*********</b> или <b>0*********</b>.\n\nПопробуй записаться еще раз!", parse_mode="html")

def take_name_13(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("ole.nevidomskyi@gmail.com", "fjpbphzbfdzhdzxg")
    server.sendmail("ole.nevidomskyi@gmail.com", "ole.nevidomskyi@gmail.com",
                    "You Have a New Client\n His Name: " + message.text + "\n His Time: 13:00")
    server.quit()

    bot.send_message(message.chat.id, "Ты записан на 13:00 ☺")

def take_name_14(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("ole.nevidomskyi@gmail.com", "fjpbphzbfdzhdzxg")
    server.sendmail("ole.nevidomskyi@gmail.com", "ole.nevidomskyi@gmail.com",
                    "You Have a New Client\n His Name: " + message.text + "\n His Time: 14:00")
    server.quit()

    bot.send_message(message.chat.id, "Ты записан на 14:00 ☺")

def take_name_15(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("ole.nevidomskyi@gmail.com", "fjpbphzbfdzhdzxg")
    server.sendmail("ole.nevidomskyi@gmail.com", "ole.nevidomskyi@gmail.com",
                    "You Have a New Client\n His Name: " + message.text + "\n His Time: 15:00")
    server.quit()

    bot.send_message(message.chat.id, "Ты записан на 15:00 ☺")


def take_name_16(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("ole.nevidomskyi@gmail.com", "fjpbphzbfdzhdzxg")
    server.sendmail("ole.nevidomskyi@gmail.com", "ole.nevidomskyi@gmail.com",
                    "You Have a New Client\n His Name: " + message.text + "\n His Time: 16:00")
    server.quit()

    bot.send_message(message.chat.id, "Ты записан на 16:00 ☺")


def take_name_17(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("ole.nevidomskyi@gmail.com", "fjpbphzbfdzhdzxg")
    server.sendmail("ole.nevidomskyi@gmail.com", "ole.nevidomskyi@gmail.com",
                    "You Have a New Client\n His Name: " + message.text + "\n His Time: 17:00")
    server.quit()

    bot.send_message(message.chat.id, "Ты записан на 17:00 ☺")


def take_name_18(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("ole.nevidomskyi@gmail.com", "fjpbphzbfdzhdzxg")
    server.sendmail("ole.nevidomskyi@gmail.com", "ole.nevidomskyi@gmail.com",
                    "You Have a New Client\n His Name: " + message.text + "\n His Time: 18:00")
    server.quit()

    bot.send_message(message.chat.id, "Ты записан на 18:00 ☺")


def take_name_19(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("ole.nevidomskyi@gmail.com", "fjpbphzbfdzhdzxg")
    server.sendmail("ole.nevidomskyi@gmail.com", "ole.nevidomskyi@gmail.com",
                    "You Have a New Client\n His Name: " + message.text + "\n His Time: 19:00")
    server.quit()

    bot.send_message(message.chat.id, "Ты записан на 19:00 ☺")


def take_name_20(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("ole.nevidomskyi@gmail.com", "fjpbphzbfdzhdzxg")
    server.sendmail("ole.nevidomskyi@gmail.com", "ole.nevidomskyi@gmail.com",
                    "You Have a New Client\n His Name: " + message.text + "\n His Time: 20:00")
    server.quit()

    bot.send_message(message.chat.id, "Ты записан на 20:00 ☺")

def take_sometime(message):

    name = bot.send_message(message.chat.id, message.text)
    name = name.text
    name = name.split()
    name.append("Student")
    if name[1] == "Student":
        bot.send_message(message.chat.id, "Упс, ты что-то не правильно написал. 😅\nИмя и время должны быть в одном сообщении, как в примере. Попробуй еще раз!\n\n<b>Пример:</b> Oleg 13:45", parse_mode="html")
    else:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("ole.nevidomskyi@gmail.com", "fjpbphzbfdzhdzxg")
        server.sendmail("ole.nevidomskyi@gmail.com", "ole.nevidomskyi@gmail.com",
                        "You Have a New Client\n His Name: " + str(name[0]) + "\n His Time: " + str(name[1]))
        server.quit()

        bot.send_message(message.chat.id, "Ты записан на " + str(name[1]) + " ☺")


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://salty-scrubland-00388.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
