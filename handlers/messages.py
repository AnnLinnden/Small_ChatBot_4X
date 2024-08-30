import asyncio
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.chat_action import ChatActionSender
from config import bot



class Messages:
    def __init__(self):
        self.starting_message = ('Привет! У нас тут классный бот. Пока он мало что может, но в будущем здесь появится '
                                 'охренительный контент, честное слово\n'
                                 'Кстати, вот наши контакты (все кнопки работают, попробуй):')
        self.message_before_pay = ('Посмотрел первое сообщение? '
                                   '<tg-spoiler>Ну наверняка, прошло-то несколько секунд всего.</tg-spoiler>\n'
                                   'Короче, тут такое дело. <b>Мы бы очень хотели денег.</b> '
                                   'Поэтому, пожалуйста, нажми /buy '
                                   '(тут будет красивая кнопочка с ценой и финтифлюшками, но позже)')
        self.payment_explanation = ('Пользователи могут приобретать Stars в Telegram с помощью стандартных покупок '
                                    'в приложениях Apple и Google или через @PremiumBot, а затем использовать их'
                                    'для покупки цифровых товаров и услуг у вас. Если у тебя нет звезд, не переживай, '
                                    'телега предложит их купить прямо перед оформлением заказа')
        self.message_after_pay = ('Благодарим за оплату нихуя (ибо ничего пока и нет) и говорим: '
                                  'первое сообщение ты получишь уже сегодня (прям щас вот), '
                                  'а дальше по одному каждый <s>божий</s> будний день будет прилетать. '
                                  'Удачи, юный падаван.\n'
                                  'Ебашь. \nНо помни. \nУпарываться не обязательно.')
        self.pay_support_message = 'Здесь про то, куда бежать, если с платежом проблемы'

    async def message_day_1(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Это первая цепочка. Она прилетит через минутку '
                                                     'после оплаты. Ну или секунд через 30, как решим\n'
                                                     'Не уходи, я настроила так, чтобы каждая следующая цепочка '
                                                     'падала секунд через 10 после предыдущей. Ща всё будет.')

    async def message_day_2(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Это вторая цепочка. В каждой цепочке сможем кидать столько '
                                                     'сообщений, сколько надо.')

    async def message_day_3(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Третья цепочка. Файлы и голосовые тоже можем кидать, но это '
                                                     'немного проблемно, поэтому я бы искренне предпочла давать '
                                                     'ссылки. Но не обязательно, конечно.')

    async def message_day_4(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Четвертая цепочка. Уруру.')

    async def message_day_5(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Пятая цепочка. Ляляля')

    async def message_day_6(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Шестая цепочка. '
                                                     'Нам еще надо решить, как будем деньги принимать. ')

    async def message_day_7(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Седьмая цепочка. '
                                                     'Звезды - это модно, конечно, но можно и на сбер ')

    async def message_day_8(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Восьмая цепочка. И надо для бота красивое описание, название '
                                                     'и картиночку восхитительную')

    async def message_day_9(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Девятая цепочка. Картиночку можно нейросеткам заказать, '
                                                     'пусть работают.')

    async def message_day_10(self, chat_id):
        await bot.send_message(chat_id=chat_id, text='Десятая цепочка. Последняя (но если надо больше, я без проблем '
                                                     'нафигачу). Надо еще решить, что после этого сообщения будет. '
                                                     'Или может, в самом конце этой цепочки благодарность какая-то '
                                                     'должна быть')

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
