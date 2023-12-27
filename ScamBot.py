import telebot 
from telebot import types 

bot = telebot.TeleBot('') 

@bot.message_handler(commands=['start', 'restart'])
def start(message):
    keyboard_markup = types.ReplyKeyboardMarkup()
    help = types.InlineKeyboardButton('/help')
    keyboard_markup.add(help)
    bot.send_message(message.chat.id, 'Вы запустили нашего бота!\nПропиште /help чтоб получить команды бота', reply_markup=keyboard_markup)

@bot.message_handler(commands=['help'])
def help(message): 
    keyboard_markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('/FreeNitro')
    btn2 = types.InlineKeyboardButton('/restart')
    btn3 = types.InlineKeyboardButton('/info')
    btn4 = types.InlineKeyboardButton('/ad')
    keyboard_markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Конечно! Вот команды бота: (кнопки внизу)', reply_markup=keyboard_markup)

@bot.message_handler(commands=['ad'])
def ad(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Наш партнёр:', callback_data='adven'))
    bot.send_message(message.chat.id, 'Вот наш партнёр', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "adven":
                bot.send_message(call.message.chat.id, "Партнёры не найдены")
    except Exception as e:
        print(repr(e))

@bot.message_handler(commands=['FreeNitro', 'fn', 'FreeN', 'freenitro', 'freen'])
def freenitro(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('1 источник', url='https://telegra.ph/Beslpatnoe-discord-nitro-2023-2024-12-27'))
    markup.add(types.InlineKeyboardButton('2 источник', url='https://discord.gg/uUTuqqc'))
    bot.send_message(message.chat.id, 'Вот источники:', reply_markup=markup)

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Этот бот поможет получить беслпатное нитро в 2023-2024 году, но помните: шанс получить нитро беслпатно очень мал!')

bot.polling(none_stop=True) 