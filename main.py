import asyncio
import logging
from aiogram import Dispatcher
from config import bot
from handlers.user_handlers import user_router
from handlers.admin_handlers import admin_router
from db import DatabaseManager


db = DatabaseManager('db/database.db')
logging.basicConfig(level=logging.INFO)  # Включаем логирование: будем записывать логи событий и ошибок
logger = logging.getLogger(__name__)

# диспетчер - корневой роутер
# регистрирует обработчики, фильтрует события из ТГ и решает, какой обработчик будет включен
dp = Dispatcher()


async def main():
    # регистрация роутеров
    dp.include_routers(user_router, admin_router)

    # запуск бота в режиме long polling при запуске бот очищает все обновления, которые были за его моменты бездействия
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

asyncio.run(main())
