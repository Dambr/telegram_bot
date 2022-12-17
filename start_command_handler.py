from telebot import types

def handle_start_command(bot, message):
	chat_id = message.chat.id
	out_message = '''
	<b>/start</b> - отобразит возможности бота;
	<b>/sticker</b> - пришлет стикер;
	Если отправить стикер - бот оценит отправленный стикер.

	Можете попытаться начать вести с ботом беседу,
	но он еще очень маленький и только учится разговаривать
	'''

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
	sticker = types.KeyboardButton('/sticker')
	markup.add(sticker)

	bot.send_message(chat_id, out_message, parse_mode='html', reply_markup=markup)