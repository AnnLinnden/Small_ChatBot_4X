from datetime import timedelta
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.fsm.storage.redis import RedisStorage
import redis.asyncio as redis


load_dotenv()
TOKEN = getenv("TOKEN")
ADMINS_LIST = getenv("ADMINS")
ADMINS = [int(admin_id) for admin_id in ADMINS_LIST.split(',')]
ADMIN_PANEL_PASS = getenv("ADMIN_PANEL_PASS")
BREAK_BETWEEN_MESSAGES = timedelta(days=1)  # Перерыв между сообщениями
PRODUCT_PRICE = 1  # Стоимость вашего продукта
PRODUCT_NAME = 'Название продукта'
PRODUCT_DESCRIPTION = 'Описание продукта'
PAYMENT_EFFECT = "5044134455711629726"  # Эффект, который увидит пользователь после оплаты. Ниже варианты
# "5104841245755180586",  # 🔥
# "5107584321108051014",  # 👍
# "5044134455711629726",  # ❤️
# "5046509860389126442",  # 🎉

async_redis_client = redis.Redis(host=getenv('HOST_REDIS'),
                                 port=int(getenv('PORT_REDIS')),
                                 decode_responses=True,
                                 username=getenv('USERNAME_REDIS'),
                                 password=getenv('PASSWORD_REDIS'))
redis_storage = RedisStorage(redis=async_redis_client)

bot = Bot(token=TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=redis_storage)


async def set_commands():
    commands_list = [
        BotCommand(command='start', description='Запустить бота заново'),
        BotCommand(command='buy', description='Оформить покупку'),
        BotCommand(command='paysupport', description='Сообщить о проблемах с оплатой')
        ]
    await bot.set_my_commands(commands_list, BotCommandScopeDefault())
