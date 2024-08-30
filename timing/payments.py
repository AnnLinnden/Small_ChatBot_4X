from aiogram import types, F
from aiogram.types import LabeledPrice, Message
from aiogram.filters.command import Command
from config import CHANNEL_USERNAME, PRODUCT_PRICE, PRODUCT_NAME, PRODUCT_DESCRIPTION, bot, dp
from handlers.messages import Messages

prices = [LabeledPrice(label='XTR', amount=PRODUCT_PRICE)]  # XTR автоматически заменится за иконку Telegram Star
messages = Messages()


# Обработчик команды /buy. Когда пользователь отправляет команду /buy, бот отправляет инвойс на оплату
@dp.message(Command('buy'))
async def buy(message: Message):
    await message.answer(messages.payment_explanation)
    await bot.send_invoice(
        chat_id=CHANNEL_USERNAME,  # Идентификатор чата (пользователя), куда отправляется инвойс
        title=PRODUCT_NAME,  # Название продукта или услуги, 1-32 characters
        description=PRODUCT_DESCRIPTION,  # Описание продукта или услуги, 1-255 characters
        payload='subscription_payload',  # Идентификатор заказа для нас, клиент его не видит
        currency='XTR',
        provider_token='',  # Оставляем пустым для ТГ Звезд
        prices=prices,  # Must contain exactly one item for payments in Telegram Stars.
    )

@dp.message(Command('paysupport'))
async def pay_support(message: Message):
    await message.answer(messages.pay_support_message)

@dp.message(Command('refund'))


# Обработчик для pre_checkout_query. Этот этап происходит перед подтверждением оплаты
# Здесь бот проверяет валидность данных и подтверждает оплату
@dp.pre_checkout_query(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    try:
        # Подтверждаем, что все данные верны, и бот готов принять оплату
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    except Exception as e:
        # Если произошла ошибка, бот отправляет сообщение с объяснением ошибки
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=False, error_message=str(e))
        print(f"Ошибка при обработке pre_checkout_query: {e}")


# Обработчик успешного платежа. Вызывается, когда пользователь успешно завершает оплату
@dp.message(F.successful_payment)
async def successful_payment(message: types.Message):
    payment_info = message.successful_payment  # Данные об успешном платеже, которые отправляются Telegram
    # Ответ пользователю с подтверждением успешного платежа и указанием суммы
    await message.reply(
        f"Оплата прошла успешно! Спасибо за покупку {payment_info.total_amount / 100:.2f} {payment_info.currency}."
    )


