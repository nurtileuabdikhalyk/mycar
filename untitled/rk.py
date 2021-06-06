import telebot

bot=telebot.TeleBot('1115254666:AAHKcbSEu_X04CQ5-zdr7S6_oHrOUaFwV3s')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет{message.from_user.first_name}{message.from_user.last_name}!"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def mes(message):
    final_message = ""
    i=1;
    sum = 0
    while(i<=3):
        get_message_bot =int(input("Введите РК",i)) #message.text.strip().lower()
        i+=1
        if 0<=get_message_bot<=100:
            sum+=get_message_bot
        else: print("Неверный РК")
    sum*=0.2
    point=100-sum

    if final_message == "":
        final_message=f"<u>Вам набрать:{point} баллов"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
bot.polling(none_stop=True)



