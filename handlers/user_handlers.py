import time
from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import (Message, BotCommand, CallbackQuery, ReplyKeyboardRemove,
                           BotCommandScopeDefault)  # команды работают для всех в чате

from keyboards.inline_keys import keyboard_with_links, button_for_pay
from timing.time_functions import ScheduleMessages
from handlers.messages import Messages

user_router = Router()
messages = Messages()


@user_router.message(Command("start"))  # реагирует на команду /start
async def cmd_start(message: Message):
    await message.answer(messages.starting_message, reply_markup=keyboard_with_links())
    time.sleep(7)
    await message.answer(messages.message_before_pay)


@user_router.message(Command("pay"))
async def pay_command(message: Message):
    # Проверим факт оплаты. Если прошла:
    await message.answer(messages.message_after_pay)
    chat_id = message.from_user.id
    scheduler = ScheduleMessages()
    send_dates = scheduler.create_list_of_send_dates(count_of_days=len(messages.message_chain()))
    for function, date in zip(messages.message_chain(), send_dates):
        scheduler.schedule_messages(function, date, chat_id=chat_id)
    scheduler.check()

# .callback_query cрабатывает на сообщения, содержащие callback дату
# (т. е. информацию о событии - какую кнопку нажали, что написали в чате и пр.)
# F.text – обычное текстовое сообщение (уже такое делали)
# F.photo – cообщение с фото
# F.video – сообщение с видео
# F.animation – сообщение с анимацией (гифки)
# F.contact – сообщение с отправкой контактных данных (очень полезно для FSM)
# F.document – сообщение с файлом (тут может быть и фото, если оно отправлено документом)
# F.data – сообщение с CallData
# F.text == 'Привет' - текст сообщения == Привет. Если != - любое, кроме Привет
# F.text.contains('Привет') - содержит "привет". Можно использовать F.text.lower() для единого регистра
# F.text.startswith('Привет') - начинается со слова
# F.text.endswith('дружище') - заканчивается словом
# ~F.text.startswith('spam') - инвертирование, т. е. сообщение НЕ начинается со spam
# F.text.upper().in_({'ПРИВЕТ', 'ПОКА'}) - сообщение - один из вариантов в множестве
# F.chat.type.in_({"group", "supergroup"}) - относится к одному из типов
# f.content_type.in_({'text', 'sticker', 'photo'}) - сообщение относится к одному из перечисленных типов контента
# F.text.len() == 5 - длина сообщения равна 5


# Что можно вытащить из сообщения:
# Message.message_id (id сообщения)
# Message.date (дата и время отправки сообщения)
# Message.text (текст сообщения)
# Message.html_text (забираем текст с htm-тегами)
# Message.from_user (username, first_name, last_name, full_name, is_premium и прочее)
# Message.chat (id, type, title, username/channel) То есть мы можем сделать примерно такой словарь:
# data_task = {'user_id': message.from_user.id, 'full_name': message.from_user.full_name,
# 'username': message.from_user.username, 'message_id': message.message_id, 'date': get_msc_date(message.date)}
