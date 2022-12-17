import telebot
import json

key_file = open('key.json')
key_json = json.load(key_file)
key = key_json['key']
key_file.close()

bot = telebot.TeleBot(key)

@bot.message_handler(commands = ['start'])
def start(message):
	print('Получено сообщение по команде start')
	chat_id = message.chat.id
	from_user = message.from_user
	user_first_name = from_user.first_name
	user_last_name = from_user.last_name
	
	out_message = '''
		<b>Hellp</b>{0},{1}
	'''.format(user_first_name, user_last_name)

	bot.send_message(chat_id, out_message, parse_mode='html')

print('Бот запущен')
bot.polling(none_stop=True)