from aiogram import Router, F
from aiogram.types import (Message, BotCommand, CallbackQuery, ReplyKeyboardRemove,
                           BotCommandScopeDefault)
import db
from config import ADMINS
from keyboards.inline_keys import admin_keyboard

database_manager = db.DatabaseManager()
admin_router = Router()


@admin_router.message(F.text.lower() == 'админка')
async def greeting_admin(message: Message):
    user_id = message.from_user.id
    if user_id in ADMINS:
        await message.reply(
            f"Здравствуй, {message.from_user.full_name}!\nВыбирай, что тебе надо узнать",
            reply_markup=admin_keyboard()
        )


# Можем предложить набор опций (например, посмотреть, сколько человек всего в базе, сколько купили, сколько нет и пр.)
# Подтягиваем функции из storage, обрабатываем и выдаем ответ
@admin_router.callback_query(F.data == "user_amount")
async def show_user_amount(callback: CallbackQuery):
    await callback.message.answer('сюда - вывод функции, которая забирает инфу из хранилища')
    await callback.answer()  # Чтобы не висели часики


@admin_router.callback_query(F.data == 'buyers_names')
async def show_buyers_names(callback: CallbackQuery):
    await callback.message.answer('вывод функции')
    await callback.answer()


@admin_router.callback_query(F.data == 'earned money')
async def show_earned_money(callback: CallbackQuery):
    await callback.message.answer('вывод функции')
    await callback.answer()
