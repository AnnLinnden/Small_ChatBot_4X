from aiogram.utils.chat_action import ChatActionSender
from config import bot


class Messages:
    def __init__(self):
        self.starting_message = ('Стартовое сообщение\n'
                                 'Кстати, вот наши контакты (все кнопки работают, попробуй):')
        self.message_before_pay = 'Сообщение перед покупкой. Пожалуйста, нажмите /buy =)'
        self.payment_explanation = ('Вы можете купить Stars в Telegram с помощью стандартных покупок '
                                    'в приложениях Apple и Google или через @PremiumBot. Если у вас нет звезд, '
                                    'Telegram предложит их купить перед оформлением заказа')
        self.message_after_pay = ('Сообщение после оплаты.\n'
                                  'ID покупки: (подставится автоматически)')
        self.pay_support_message = 'Сообщение о том, что делать, если с платежом возникли проблемы'
        self.payment_error = ('Наш бот утверждает, что вы уже оплачивали этот продукт. '
                              'Нажмите /paysupport, разберемся вместе!')
        # self.money_refund_message = 'Для тех, кто запрашивает возврат денег'

    async def message_day_1(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Это первая цепочка. В функцию можно добавить сколько угодно '
                                                     'сообщений, в том числе с фото, ссылками, файлами, видео и пр.')

    async def message_day_2(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Это вторая цепочка.')

    async def message_day_3(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Третья цепочка.')

    async def message_day_4(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Четвертая цепочка.')

    async def message_day_5(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Пятая цепочка.')

    async def message_day_6(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Шестая цепочка.')

    async def message_day_7(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Седьмая цепочка.')

    async def message_day_8(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Восьмая цепочка.')

    async def message_day_9(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Девятая цепочка.')

    async def message_day_10(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Десятая цепочка.')

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
