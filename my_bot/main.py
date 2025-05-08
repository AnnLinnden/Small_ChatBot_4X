import asyncio
import logging
from config import bot, dp, set_commands
from handlers.user_handlers import user_router
from handlers.admin_handlers import admin_router
from timing.payments import payment_router
from db.storage import DatabaseManager

database_manager = DatabaseManager()
logging.basicConfig(level=logging.INFO)  # Включаем логирование: будем записывать логи событий и ошибок
logger = logging.getLogger(__name__)


async def main():
    dp.include_routers(user_router, admin_router, payment_router)

    # запуск в режиме long polling: при запуске бот очищает все обновления, прилетевшие, пока он не работал
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await database_manager.initialize_database()
        await dp.start_polling(bot, skip_updates=True)
        await set_commands()
    finally:
        await bot.session.close()

asyncio.run(main())
