import telebot 
import time
import datetime


bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])


def send_welcome(message):
	bot.reply_to(message, "welcome! use /help to explore")


@bot.message_handler(commands=['help'])


def send_help(message):
	bot.reply_to(message, 'To use this bot, send /months and /days to know the python2 month and days left to come to an end')


@bot.message_handler(commands=['months'])


def send_months_left(message):
	days_left = ((datetime.datetime(2020,1,1) - datetime.datetime.now()).days) 
	months_left = days_left / 30
	string_form = repr(months_left)
	splitted = string_form.split('.')
	result = float ("0."+ splitted [1]) 

	bot.reply_to(message, string_form[0])
@bot.message_handler(commands=['days'])


def send_days_left(message):
	days_left = ((datetime.datetime(2020,1,1) - datetime.datetime.now()).days) 
	months_left = days_left / 30
	string_form = repr(months_left)
	splitted = string_form.split('.')
	result = float ("0."+ splitted [1]) 


	bot.reply_to(message, days_left)


while True:
	try:
		bot.polling()
	except Exception:
		time.sleep(15)
		




