from datetime import timedelta
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

load_dotenv()
TOKEN = getenv("TOKEN")
ADMINS_LIST = getenv("ADMINS")
ADMINS = [int(admin_id) for admin_id in ADMINS_LIST.split(',')]
BREAK_BETWEEN_MESSAGES = timedelta(seconds=10)

bot = Bot(token=TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # форматирование всех сообщений через HTML
