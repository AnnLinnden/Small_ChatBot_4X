from datetime import timedelta
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

load_dotenv()
TOKEN = getenv("TOKEN")
ADMINS_LIST = getenv("ADMINS")
ADMINS = [int(admin_id) for admin_id in ADMINS_LIST.split(',')]
BREAK_BETWEEN_MESSAGES = timedelta(seconds=10)
CHANNEL_USERNAME = '@recharge_SMM_bot'
PRODUCT_PRICE = 500
PRODUCT_NAME = 'Тетрадушка'
PRODUCT_DESCRIPTION = '10 дней = 10 постов для кайфовой зарядки'

bot = Bot(token=TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# Сюда нужно вписать хранилище! storage=
dp = Dispatcher()
