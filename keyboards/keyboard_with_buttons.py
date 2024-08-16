from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import ADMINS


def main_keyboard(user_telegram_id: int):  # принимает на вход ID пользователя в тг, чтобы узнавать админа
    # создает набор кнопок (обязательно в списке списков)
    if user_telegram_id in ADMINS:  # вот тут функция как раз узнает админа
        buttons = [KeyboardButton(text="Админка")]  # добавляем еще одну кнопку
    else:
        buttons = []

    # с помощью ReplyKeyboardMarkup создаем клаву, которую можно привязать к обработчику
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,  # указываем, откуда брать кнопки (список)
        resize_keyboard=True,  # кнопки будут автоматически менять размер
        one_time_keyboard=True,  # клава скроется после нажатия на кнопку
        input_field_placeholder="Выбирай тему, котичек =)"  # заменяет «Написать сообщение...»
    )
    return keyboard

