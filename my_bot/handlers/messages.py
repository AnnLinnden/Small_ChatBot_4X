from asyncio import sleep

from aiogram.types import FSInputFile, InputMediaPhoto

from my_bot.config import bot


class Messages:
    def __init__(self):
        self.starting_message = (
            "Стартовое сообщение\n"
            "Кстати, вот наши контакты (все кнопки работают, попробуй):"
        )
        self.message_before_pay = (
            "Сообщение перед покупкой. Пожалуйста, нажмите /buy =)"
        )
        self.payment_explanation = (
            "Вы можете купить Stars в Telegram с помощью стандартных покупок "
            "в приложениях Apple и Google или через @PremiumBot. Если у вас нет звезд, "
            "Telegram предложит их купить перед оформлением заказа"
        )
        self.message_after_pay = (
            "Сообщение после оплаты.\n"
            "ID покупки: (подставится автоматически, он нужен для возврата средств)"
        )
        self.pay_support_message = (
            "Сообщение о том, что делать, если с платежом возникли проблемы"
        )
        self.payment_error = (
            "Наш бот утверждает, что вы уже оплачивали этот продукт. "
            "Нажмите /paysupport, разберемся вместе!"
        )
        # self.money_refund_message = 'Для тех, кто запрашивает возврат денег'

    @staticmethod
    async def send_file(
        chat_id, file_id, file_path, caption
    ):  # отправка файла: .pdf, .png, .docx, .jpg и пр.
        try:
            await bot.send_photo(chat_id=chat_id, photo=file_id, caption=caption)
        except Exception:
            file = FSInputFile(file_path)
            await bot.send_photo(chat_id=chat_id, photo=file, caption=caption)

    @staticmethod
    async def send_album(
        chat_id, files_id: list, files_path: list, caption
    ):  # отправка альбома с .jpg | .png
        album_builder = []
        for idx, (file_id, _) in enumerate(zip(files_id, files_path)):
            try:
                photo = InputMediaPhoto(media=file_id)
                album_builder.append(photo)
            except Exception:
                photo_file = FSInputFile(files_path[files_id.index(file_id)])
                photo = InputMediaPhoto(media=photo_file)
                album_builder.append(photo)
            if idx == 0:
                album_builder[0].caption = caption

        await bot.send_media_group(chat_id=chat_id, media=album_builder)

    @staticmethod
    async def send_text(chat_id, text):  # отправка текста
        try:
            await bot.send_message(chat_id=chat_id, text=text)
        except Exception:
            await sleep(10)
            await bot.send_message(chat_id=chat_id, text=text)
        #  Бот использует HTML для форматирования текста. Напомню теги:
        # <b>Жирный</b>
        # <i>Курсив</i>
        # <u>Подчеркнутый</u>
        # <s>Зачеркнутый</s>
        # <tg-spoiler>Спойлер (скрытый текст)</tg-spoiler>
        # <a href="http://www.example.com/">Ссылка в тексте</a>
        # <code>Код с копированием текста при клике</code>
        # <pre>Спойлер с копированием текста</pre>

    async def message_day_1(self, chat_id):
        await self.send_text(
            chat_id=chat_id,
            text="Это первая цепочка. В функцию можно добавить сколько угодно "
            "сообщений, в том числе с фото, ссылками, файлами, видео и пр.",
        )
        await self.send_file(
            chat_id=chat_id,
            file_id="AgACAgIAAxkBAAKlZlEoZiQyNnZmM4Q8MjU5Y1Y3ZjNlMmE3NzUwMD",
            file_path="screens/1.jpg",
            caption="Это подпись к картинке/файлу. Можно оставить пустой",
        )
        await self.send_album(
            chat_id=chat_id,
            files_id=[
                "AgACAgIAAxkBAAKlZlEoZiQyNnZmM6Q8MjU5Y1Y3ZjNlMmE3NzUwMD",
                "AgACAgIAAxkBAAKlZlEoZiQyNnZmM4Q8MjU5Y1Y9ZjNlMmE3NzUwMD",
            ],
            files_path=["screens/4.png", "screens/5.png"],
            caption="Подпись к альбому. Можно оставить пустой",
        )

    async def message_day_2(self, chat_id):
        await self.send_text(chat_id=chat_id, text="Это вторая цепочка.")

    async def message_day_3(self, chat_id):
        await self.send_text(chat_id=chat_id, text="Третья цепочка.")

    async def message_day_4(self, chat_id):
        await self.send_text(chat_id=chat_id, text="Четвертая цепочка.")

    async def message_day_5(self, chat_id):
        await self.send_text(chat_id=chat_id, text="Пятая цепочка.")

    async def message_day_6(self, chat_id):
        await self.send_text(chat_id=chat_id, text="Шестая цепочка.")

    async def message_day_7(self, chat_id):
        await self.send_text(chat_id=chat_id, text="Седьмая цепочка.")

    async def message_day_8(self, chat_id):
        await self.send_text(chat_id=chat_id, text="Восьмая цепочка.")

    async def message_day_9(self, chat_id):
        await self.send_text(chat_id=chat_id, text="Девятая цепочка.")

    async def message_day_10(self, chat_id):
        await self.send_text(chat_id=chat_id, text="Десятая цепочка.")

    def message_chain(self):
        return [
            self.message_day_1,
            self.message_day_2,
            self.message_day_3,
            self.message_day_4,
            self.message_day_5,
            self.message_day_6,
            self.message_day_7,
            self.message_day_8,
            self.message_day_9,
            self.message_day_10,
        ]
