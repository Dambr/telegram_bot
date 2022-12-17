def handle_text_content(bot, message):
	chat_id = message.chat.id
	message_text = message.text
	reserved_texts = {
		'Привет': 'Здравствуйте',
		'Кто ты?': 'Я бот',
		'Как дела?': 'Нахожусь в процессе разработки'
	}
	out_message = ''
	if message_text in reserved_texts:
		out_message = reserved_texts[message_text]
	else:
		out_message = 'Не понимаю вас'
	bot.send_message(chat_id, out_message, parse_mode='html')