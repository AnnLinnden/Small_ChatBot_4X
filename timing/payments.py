from aiogram import F, Router
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery
from aiogram.filters.command import Command
from timing.time_functions import ScheduleMessages
from config import PRODUCT_PRICE, PRODUCT_NAME, PRODUCT_DESCRIPTION, PAYMENT_EFFECT, bot
from handlers.messages import Messages
from db.storage import DatabaseManager

prices = [LabeledPrice(label='XTR', amount=PRODUCT_PRICE)]  # XTR автоматически заменяется на иконку Telegram Star
payment_router = Router()
messages = Messages()
database = DatabaseManager()


@payment_router.message(Command('buy'))
async def buy(message: Message):
    await message.answer(messages.payment_explanation)
    await bot.send_invoice(
        chat_id=message.chat.id,
        title=PRODUCT_NAME,  # Название продукта или услуги, 1-32 символа
        description=PRODUCT_DESCRIPTION,  # Описание продукта или услуги, 1-255 символов
        payload=f'payload_{message.chat.id}',  # Идентификатор заказа для нас, клиент его не видит
        currency='XTR',
        provider_token='',  # Оставляем пустым для ТГ Звезд
        prices=prices,  # Must contain exactly one item for payments in Telegram Stars.
    )


@payment_router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    user_id = pre_checkout_query.from_user.id
    if database.check_user_not_paid_before(user_telegram_id=user_id) is True:
        await pre_checkout_query.answer(ok=True)
    else:
        await pre_checkout_query.answer(
            ok=False,
            error_message=messages.payment_error
        )


@payment_router.message(F.successful_payment)
async def successful_payment(message: Message):
    await message.answer(
        f"{messages.message_after_pay} {message.successful_payment.telegram_payment_charge_id}",
        message_effect_id=PAYMENT_EFFECT
    )
    await database.add_user(user_telegram_id=message.from_user.id,
                            username=message.from_user.username,
                            price=PRODUCT_PRICE)
    scheduler = ScheduleMessages()
    send_dates = scheduler.create_list_of_send_dates(count_of_days=len(messages.message_chain()))
    for function, date in zip(messages.message_chain(), send_dates):
        scheduler.schedule_messages(function, date, chat_id=message.from_user.id)
    # scheduler.check()


@payment_router.message(Command('paysupport'))
async def pay_support(message: Message):
    await message.answer(messages.pay_support_message)

