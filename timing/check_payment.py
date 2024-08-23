from aiogram import Bot, Dispatcher, types, F
from aiogram.types import LabeledPrice

# Замените на токен вашего бота, который вы получили от BotFather
API_TOKEN = '7392751106:AAGmJiQH98HaeL-T4AChTJIKPF3uCyt3ObY'

# Токен вашего платежного провайдера, полученный от BotFather после настройки платежей
PAYMENT_PROVIDER_TOKEN = 'YOUR_PAYMENT_PROVIDER_TOKEN_HERE'

# Создание объекта бота с использованием API-токена
bot = Bot(token=API_TOKEN)

# Создание диспетчера для управления обработчиками событий
dp = Dispatcher()

# Список цен для инвойса. В данном случае это один продукт (подписка на 1 месяц) за 100 рублей (10000 копеек)
prices = [
    LabeledPrice(label='Подписка на 1 месяц', amount=10000),  # 100 рублей
]

# Обработчик команды /start. Когда пользователь отправляет команду /start, ему будет отправлено приветственное сообщение
@dp.message(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Нажмите /buy для покупки подписки.")

# Обработчик команды /buy. Когда пользователь отправляет команду /buy, бот отправляет инвойс на оплату
@dp.message(commands=['buy'])
async def buy(message: types.Message):
    await bot.send_invoice(
        chat_id=message.chat.id,  # Идентификатор чата (пользователя), куда отправляется инвойс
        title='Подписка на бота',  # Название продукта или услуги
        description='Оплата за подписку на 1 месяц',  # Описание продукта или услуги
        payload='subscription_payload',  # Уникальный идентификатор заказа. Нужен для сопоставления платежа с заказом
        provider_token=PAYMENT_PROVIDER_TOKEN,  # Токен платежного провайдера
        currency='RUB',  # Валюта, в которой происходит оплата (например, RUB для российских рублей)
        prices=prices,  # Список цен, которые включены в инвойс
    )


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


