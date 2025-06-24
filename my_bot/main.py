import asyncio
import logging
from logging.handlers import RotatingFileHandler

from config import bot, dp, set_commands
from db.storage import DatabaseManager
from handlers.admin_handlers import admin_router
from handlers.user_handlers import user_router
from timing.payments import payment_router

database_manager = DatabaseManager()
logging.basicConfig(
    level=logging.INFO,
    filename="app.log",  # Логи будут сохраняться в этот файл
    filemode="a",  # логи будут дозаписываться в файл
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)
handler = RotatingFileHandler(  # если файл с логами заполнится, создастся новый
    "app.log",
    maxBytes=5 * 1024 * 1024,  # размер файла логов - 5 MB
    backupCount=3,  # бот будет хранить 3 резервные копии
)
logger.addHandler(handler)


async def main():
    dp.include_routers(user_router, admin_router, payment_router)

    # запуск в режиме long polling: при запуске бот очищает все обновления, прилетевшие, пока он не работал
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await database_manager.initialize_database()
        await set_commands()
        await dp.start_polling(bot, skip_updates=True)

    finally:
        await bot.session.close()


asyncio.run(main())
