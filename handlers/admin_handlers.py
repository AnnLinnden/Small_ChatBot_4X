import asyncio
from aiogram import Router, F
from aiogram.types import (Message, BotCommand, CallbackQuery, ReplyKeyboardRemove,
                           BotCommandScopeDefault)
import db
from config import ADMINS

database_manager = db.DatabaseManager()
admin_router = Router()


@admin_router.message((F.text == 'Админка') & (F.from_message.id.in_(ADMINS)))
async def greeting_admin(message: Message):
    await message.reply(f"Здравствуй, {message.from_user.name}!", reply_markup=ReplyKeyboardRemove())


# Можем предложить набор опций (например, посмотреть, сколько человек всего в базе, сколько купили, сколько нет и пр.)
# Подтягиваем функции из storage, обрабатываем и выдаем ответ
@admin_router.message(F.text('Сколько человек в базе'))
async def sfds(message: Message):
    await message.answer('ddd')
