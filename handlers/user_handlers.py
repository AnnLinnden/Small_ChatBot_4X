import asyncio
from aiogram.utils.chat_action import ChatActionSender
from aiogram import Router, F, types, Bot
from aiogram.filters.command import Command
from aiogram.types import (Message, BotCommand, CallbackQuery, ReplyKeyboardRemove,
                           BotCommandScopeDefault)  # команды работают для всех в чате
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from config import bot
from keyboards.keyboard_with_buttons import main_keyboard
from keyboards.inline_keys import ease_link_kb, create_qst_inline_kb, cmd_random
from timing.time_functions import get_next_weekday
from messages import messages

user_router = Router()

job_storage = {'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')}
scheduler = AsyncIOScheduler(jobstores=job_storage)
scheduler.start()


async def send_message(user_id, text):
    await bot.send_message(chat_id=user_id, text=text)


def schedule_messages(user_id, start_date):
    for i, message in enumerate(messages):
        send_date = get_next_weekday(start_date, i)
        scheduler.add_job(
            send_message,
            trigger=DateTrigger(run_date=send_date),
            args=(user_id, message)
        )


# Что можно вытащить из сообщения:
# Message.message_id (id сообщения)
# Message.date (дата и время отправки сообщения)
# Message.text (текст сообщения)
# Message.html_text (забираем текст с htm-тегами)
# Message.from_user (username, first_name, last_name, full_name, is_premium и прочее)
# Message.chat (id, type, title, username/channel) То есть мы можем сделать примерно такой словарь:
# data_task = {'user_id': message.from_user.id, 'full_name': message.from_user.full_name,
# 'username': message.from_user.username, 'message_id': message.message_id, 'date': get_msc_date(message.date)}

# Декоратор регистрирует функцию как обработчик.
# Вариант без декоратора: dp.message.register(cmd_test2, Command("test2"))
# Команда - та, которую вызывает пользователь в боте. Например, /start, /list_orders, /help и так далее.
# Эти команды для бота ты прописываешь сам - любые, хоть /lalala
@user_router.message(Command("start"))  # реагирует на команду /start
async def cmd_start(message: Message):
    await message.answer('Привет! Оплати доступ и начни получать сообщения.',
                         reply_markup=main_keyboard(message.from_user.id))  # привязываем основную клавиатуру


@user_router.message(Command("pay"))
async def pay_command(message: Message):
    # Предположим, что пользователь оплатил доступ
    user_id = message.from_user.id
    start_date = datetime.now()

    # Планируем отправку сообщений
    schedule_messages(user_id, start_date)

    await message.reply("Оплата получена! Вы начнёте получать сообщения.")


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