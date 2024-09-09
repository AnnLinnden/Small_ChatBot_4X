import time
from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

from keyboards.inline_keys import keyboard_with_links
from handlers.messages import Messages

user_router = Router()
messages = Messages()


@user_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(messages.starting_message, reply_markup=keyboard_with_links())
    time.sleep(3)
    await message.answer(messages.message_before_pay)

