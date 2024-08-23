import asyncio
from aiogram import Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.chat_action import ChatActionSender
from config import bot



class Messages:
    def __init__(self):
        self.starting_message = ('Привет! Это первое сообщение. Тут мы расскажем, что это за бот, что он может.'
                                 'Ну и так далее. А еще - вот наши контакты:')
        self.message_before_pay = ('Мы бы очень хотели денег. Поэтому, пожалуйста, нажми /pay '
                                   '(это будет красивая кнопочка с ценой и финтифлюшками, но позже')
        self.message_after_pay = ('Благодарим за оплату и повторяем коротко: '
                                  'первое сообщение ты получишь уже сегодня, '
                                  'а дальше по одному каждый <s>божий</s> будний день будет прилетать. '
                                  'Удачи, юный падаван')

    async def message_day_1(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Это первая цепочка. Она прилетит через минутку '
                                                     'после оплаты. Ну или секунд через 30, как решим')

    async def message_day_2(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Вторая цепочка')

    async def message_day_3(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Третья цепочка')

    async def message_day_4(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Четвертая цепочка')

    async def message_day_5(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Пятая цепочка')

    async def message_day_6(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Шестая цепочка')

    async def message_day_7(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Седьмая цепочка')

    async def message_day_8(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Восьмая цепочка')

    async def message_day_9(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Девятая цепочка')

    async def message_day_10(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Десятая цепочка')

    def message_chain(self):
        return [self.message_day_1, self.message_day_2, self.message_day_3, self.message_day_4, self.message_day_5,
                self.message_day_6, self.message_day_7, self.message_day_8, self.message_day_9, self.message_day_10]

# <b>Жирный</b>
# <i>Курсив</i>
# <u>Подчеркнутый</u>
# <s>Зачеркнутый</s>
# <tg-spoiler>Спойлер (скрытый текст)</tg-spoiler>
# <a href="http://www.example.com/">Ссылка в тексте</a>
# <code>Код с копированием текста при клике</code>
# <pre>Спойлер с копированием текста</pre>
