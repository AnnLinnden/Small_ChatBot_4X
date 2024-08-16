from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

# InlineKeyboardMarkup: для разметки инлайн-клавиатуры. Разметка определяет расположение кнопок
# и их взаимодействие с пользователем.
# InlineKeyboardButton: отдельная кнопка на клавиатуре: можем задавать текст кнопки и действие при нажатии
# WebAppInfo: создание кнопок, открывающих веб-приложения внутри ТГ.
# Для интеграции внешних веб-сервисов/приложений с ботом.
# InlineKeyboardBuilder: инструмент для создания инлайн-клавиатур.


def ease_link_kb():  # создает и возвращает инлайн-клавиатуры с кнопками, на которые навешены ссылки
    inline_kb_list = [
        [InlineKeyboardButton(text="Мой хабр", url='https://habr.com/ru/users/yakvenalex/')],
        [InlineKeyboardButton(text="Мой Telegram", url='tg://resolve?domain=yakvenalexx')],
        [InlineKeyboardButton(text="Веб приложение", web_app=WebAppInfo(url="https://tg-promo-bot.ru/questions"))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


def create_qst_inline_kb(questions: dict) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    # Добавляем кнопки вопросов
    for question_id, question_data in questions.items():
        builder.row(
            InlineKeyboardButton(
                text=question_data.get('qst'),
                callback_data=f'qst_{question_id}'
            )
        )
    # Добавляем кнопку "На главную"
    builder.row(
        InlineKeyboardButton(
            text='На главную',
            callback_data='back_home'  # нужно написать обработчик
        )
    )
    # Настраиваем размер клавиатуры
    builder.adjust(1)  # делаем строку из такого количества кнопок, которое указано в скобках
    return builder.as_markup()  # возвращаем готовый объект с клавиатурой


def cmd_random():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    return builder.as_markup()
