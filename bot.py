﻿import telebot
from config import TOKEN

# создаем объект бота, передав в него токен вашего бота
bot = telebot.TeleBot(TOKEN)

# создаем кнопку с надписью "#профориентация"
prof_button = telebot.types.KeyboardButton('#профориентация')
advice_button = telebot.types.KeyboardButton('#дайсовет')
offer_button = telebot.types.KeyboardButton('#предложение')

# создаем клавиатуру и добавляем в нее кнопки
markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(prof_button)
markup.row(advice_button, offer_button)


# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
     bot.send_message(message.chat.id, 'Привет, я бот! Напиши мне что-нибудь!', reply_markup=markup)

# обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '#профориентация':

        text = '🎯 *Моя цель — помочь тебе определиться с будущей профессией и подобрать подходящую специальность в нашем университете.*\n\nДавай начнем с того, что ты расскажешь мне о своих увлечениях, хобби и тех предметах в школе, которые тебе больше всего нравились. Кроме того, я бы хотел узнать, какие навыки тебе было бы интересно развивать в будущей профессии 💼🚀\n\nИ ещё, это твоё первое высшее образование?🎓'

        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)
    
    elif message.text == '#дайсовет':

        text = '🤔 *О чём ты бы хотел услышать?*\n\nЯ с радостью дам совет, если это поможет тебе!'

        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup) 

    elif message.text == '#предложение':

        text = '💡*Будет здорово, если ты поделишься с нами своими идеями!*\n\nНаша команда с удовольствием выслушает все, что придёт тебе на ум.'

        bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)  

# запускаем бота
bot.polling()