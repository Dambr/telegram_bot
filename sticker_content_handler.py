def handle_sticker_content(bot, message):
	chat_id = message.chat.id
	out_message = '<b>Очень красивый стикер</b>'
	bot.send_message(chat_id, out_message, parse_mode='html')