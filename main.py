import telebot
import requests
import json

bot = telebot.TeleBot('6969856818:AAEnhPpCSiFSYe6ED6WTsdlST_3m-vAnLD8')
API = 'ccfad80a7b7e7139160879a78a7ab01f'

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Привет, я покажу тебе погоду в твоем городе. Напиши название города.")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message, f'Сейчас погода: {data["main"]["temp"]}')

bot.polling(none_stop=True)

