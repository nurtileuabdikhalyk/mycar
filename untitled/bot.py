import  COVID19Py
import telebot
covid19=COVID19Py.COVID19()

bot=telebot.TeleBot('1205205785:AAGnrYFjMsX47dvp4ZcpoGvtpmCp3MWcUGU')

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет{message.from_user.first_name}!</b>\nВведите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def mes(message):
    final_message=""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    else:
        location = covid19.getLatest()
        final_message = f"<b>Данные по всему миру:</u>\n<b> Заболевшие:</b>{location['confirmed']}"
    if final_message == "":
        date=location[0]['last updated'].split("T")
        time = date[1].split(".")
        final_message=f"<u>Данные по стране:</u>\nНаселение:{location[0]['country_popular']}" \
                      f"Последнее обновление: {date[0]}{time[0]}Последние данные:\n</b>" \
                      f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\nСмертей:" \
                      f" </b>{location[0]['latest']['deaths']:,}"
        bot.send_message(message.chat.id, final_message,parse_mode='html')



bot.polling(none_stop=True)

