def handle_sticker_command(bot, message):
	chat_id = message.chat.id
	sticker_id = 'CAACAgIAAxkBAANNY54bQ4CVoeh6HmQhMAy-VVWkqecAAlgJAAIYQu4IXcTz0pvf0kIsBA'
	bot.send_sticker(chat_id, sticker_id)