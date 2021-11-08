# Import library
from main import bot, dp
from config import admin_id
from aiogram import types
from aiogram.types import *
import csv, datetime
import sqlite3

def stat(user_id, command):
        conn = sqlite3.connect('bot.db')
        cursor = conn.cursor()
        data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
        cursor.execute("INSERT INTO stat(user_id, user_command, date) VALUES ('%s', '%s', '%s')" % (user_id, command, data))
        conn.commit()
        cursor.close()


keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

array_keyboard = [1,2]

# Send message to admin
async def send_to_admin(dp):
	await bot.send_message(chat_id=admin_id, text="Bot start")

#start bot using func
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        print(array_keyboard)
        keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
        statistics(message.chat.id, message.text)
        await message.answer(text='Привет!)', reply_markup=keyboard_markup)
        stat(message.chat.id, message.text)

def statistics(user_id, command):
        data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
        with open('data.csv','a',newline="") as fil:
                wr = csv.writer(fil,delimiter=';')
                wr.writerow([data, user_id, command])
