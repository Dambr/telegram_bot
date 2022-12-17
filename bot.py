import telebot
import json
from start_command_handler import handle_start_command
from sticker_command_handler import handle_sticker_command
from text_content_handler import handle_text_content
from sticker_content_handler import handle_sticker_content

key_file = open('key.json')
key_json = json.load(key_file)
key = key_json['key']
key_file.close()

bot = telebot.TeleBot(key)

@bot.message_handler(commands = ['start'])
def start(message):
	handle_start_command(bot, message)

@bot.message_handler(commands = ['sticker'])
def start(message):
	handle_sticker_command(bot, message)

@bot.message_handler(content_types=['text'])
def get_message(message):
	handle_text_content(bot, message)

@bot.message_handler(content_types=['sticker'])
def get_sticker(message):
	handle_sticker_content(bot, message)

print('Бот работает')
bot.polling(none_stop=True)