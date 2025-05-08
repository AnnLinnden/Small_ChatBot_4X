from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard_with_links():
    list_of_links = [
        [InlineKeyboardButton(text="Написать Юле", url='https://t.me/julliru')],
        [InlineKeyboardButton(text="Написать Стасе", url='https://t.me/StasyaSher')],
        [InlineKeyboardButton(text="Написать Ане", url='https://t.me/AnnLinnden')],
        [InlineKeyboardButton(text="Полистать канал агентства", url='https://t.me/agency4x')],
        [InlineKeyboardButton(text="Посмотреть сайт 4X", url='https://agency4x.ru/')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=list_of_links)


def admin_keyboard():
    buttons = [
        [InlineKeyboardButton(text='Сколько человек оплатили?', callback_data='user_amount')],
        [InlineKeyboardButton(text='Кто оплатил?', callback_data='buyers_names')],
        [InlineKeyboardButton(text='Сколько заработали?', callback_data='earned_money')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
