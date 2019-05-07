import telebot 
import time
import datetime


bot_token = "892091673:AAHKMSkPLX7xKdQr4aoVx-BOKvYJnhp5_DE"


bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])


def send_welcome(message):
	bot.reply_to(message, "welcome!")


@bot.message_handler(commands=['help'])


def send_help(message):
	bot.reply_to(message, 'To use this bot, send the username')


@bot.message_handler(commands=['months'])


def send_months_left(message):
	days_left = ((datetime.datetime(2020,1,1) - datetime.datetime.now()).days) - 3
	months_left = days_left / 30
	string_form = repr(months_left)
	splitted = string_form.split('.')
	result = float ("0."+ splitted [1]) 

	bot.reply_to(message, string_form[0])
@bot.message_handler(commands=['days'])


def send_days_left(message):
	days_left = ((datetime.datetime(2020,1,1) - datetime.datetime.now()).days) - 3
	months_left = days_left / 30
	string_form = repr(months_left)
	splitted = string_form.split('.')
	result = float ("0."+ splitted [1]) 


	bot.reply_to(message, int (result * 30))


while True:
	try:
		bot.polling()
	except Exception:
		time.sleep(15)
		




	bot.reply_to(message, 'https')






while True:
	try:
		bot.polling()		
	except Exception:
		time.sleep(15)
