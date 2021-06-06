import telebot
import sqlite3

bot = telebot.TeleBot("1879312067:AAHIZKqeV48iwQufOVFJAxGkDoxlSfD_FLk")

global rk1, rk2, rk3


@bot.message_handler(commands=['start'])
def start(message):

    send_mess = f"Салем {message.from_user.first_name} {message.from_user.last_name}!"
    bot.send_message(message.chat.id, send_mess)
    bot.send_message(message.chat.id, f"Баллды есептеу үшін /help сөзін жібер: ")
    bot.register_next_step_handler(message, help)

@bot.message_handler(content_types=['text'])
def help(message):
    if message.text == "/help":
        bot.send_message(message.chat.id, f"РК1 баллы: ")
        bot.register_next_step_handler(message, function_rk1)
    else:
        bot.send_message(message.chat.id, f"Мен сізді түсінбедім, /help сөзін жібер: ")
def function_rk1(message, point=0):
    try:
        rk1 = int(message.text)
        if 0 <= rk1 <= 100:
            point += rk1
            bot.send_message(message.chat.id, f"РК2 баллы: ")
            bot.register_next_step_handler(message, function_rk2, point, rk1)

        else:
            bot.send_message(message.chat.id, f"РК1 баллы дұрыс енгізілмеді, /help қайта жібер")

    except Exception:
        bot.send_message(message.from_user.id, "Санмен енгізші), /help қайта жібер")



def function_rk2(message, point,rk1):
    try:
        rk2 = int(message.text)
        if 0 <= rk2 <= 100:

            point += rk2
            bot.send_message(message.chat.id, f"РК3 баллы: ")
            bot.register_next_step_handler(message, function_rk3, point, rk1, rk2)
        else:
            bot.send_message(message.chat.id, f"РК2 баллы дұрыс енгізілмеді, /help қайта жібер")

    except Exception:
        bot.send_message(message.from_user.id, "Санмен енгізші), /help қайта жібер")



def function_rk3(message, point, rk1,rk2, final_message=""):
    try:
        rk3 = int(message.text)
        if 0 <= rk3 <= 100:
            point += rk3
            point_stipendia = int((70 - (point * 0.2)) / 0.4)
            point_povyshka = int((90 - (point * 0.2)) / 0.4)
            if point_stipendia < 50.4:
                final_message = f"Стипендияға: 50-ақ балл, повышкаға {point_povyshka} балл қажет)"
            elif point_stipendia < 50.4 and point_povyshka < 100:
                final_message = f"Стипендияға: {point_stipendia} балл, повышкаға {point_povyshka} балл қажет)"
            elif 50.5<=point_stipendia <=100 and point_povyshka > 100:
                final_message = f"Стипендияға:{point_stipendia} балл қажет), стипендияға Шүкір де повышкаға жетпейсің xD"
            else:
                final_message = f"Өкінішке орай, стипендияға жетпейсің("
            connect = sqlite3.connect("users.db")
            cursor = connect.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               userid INT,
               first_name TEXT,
               last_name TEXT,
               RK1 INT,
               RK2 INT, RK3 INT);
            """)
            connect.commit()
            cursor.execute(f"""INSERT INTO users(userid, first_name, last_name, RK1,RK2,RK3)
               VALUES('{message.from_user.id}', '{message.from_user.first_name}', '{message.from_user.last_name}', '{rk1}','{rk2}','{rk3}');""")
            connect.commit()
            bot.send_message(message.chat.id, final_message)


        else:
            bot.send_message(message.chat.id, f"РК3 баллы дұрыс енгізілмеді, /help қайта жібер")
    except Exception:
        bot.send_message(message.from_user.id, "Санмен енгізші), /help қайта жібер")
    bot.send_message(message.chat.id,"Басқа пәндерді де есептеу үшін, /help сөзін жібер")



bot.polling(none_stop=True, interval=0)