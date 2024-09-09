from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
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


@admin_router.callback_query(F.data == "user_amount")
async def show_user_amount(callback: CallbackQuery):
    user_amount = await database_manager.check_user_amount()
    await callback.message.answer(f'{user_amount}')
    await callback.answer()  # Чтобы не висели часики


@admin_router.callback_query(F.data == 'buyers_names')
async def show_buyers_names(callback: CallbackQuery):
    buyers_usernames = await database_manager.get_usernames()
    if buyers_usernames == []:
        await callback.message.answer(f'Пока никто не оплатил')
    else:
        await callback.message.answer(f'Покупку оформили: {buyers_usernames}')
    await callback.answer()


@admin_router.callback_query(F.data == 'earned_money')
async def show_earned_money(callback: CallbackQuery):
    earned_money = await database_manager.get_earned_money()
    if not earned_money:
        await callback.message.answer('Пока мы ничего не заработали')
    else:
        await callback.message.answer(f'Мы заработали {earned_money} ★')
    await callback.answer()
