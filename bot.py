import telebot
import json

key_file = open("key.json")
key_json = json.load(key_file)
key = key_json["key"]
key_file.close()

bot = telebot.TeleBot(key)

