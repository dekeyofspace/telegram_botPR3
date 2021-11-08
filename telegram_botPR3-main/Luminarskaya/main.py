import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor
import csv, datetime, sqlite3

API_TOKEN = '2037710159:AAGxUqF7bw_kHzXYG1QODsHN7zZ5d-8TS7Q'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

loop = asyncio.get_event_loop()
bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handler import dp
    executor.start_polling(dp)    
