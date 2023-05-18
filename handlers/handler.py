# основной файл, в котором будет содержать почти весь код бота.
# Будет состоять из функций-обработчиков с декораторами (фильтрами)

import os

from communi_bot import openai
from aiogram import types
from communi_bot import Dispatcher, bot
from dotenv import load_dotenv, find_dotenv

from admin_fun.middlewares import LimitedRequestsMiddleware, LimitedRequestsMiddleware_min




model="gpt-3.5-turbo"

messages = [
    {"role": "system",
     "content": "Your name is Irishka, you are female. You are Irishka's assistant, "
                "a very smart chat bot, you help solve problems with Python, Javascript and C++ code."},]


def update(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages



async def send(message: types.Message):
    update(messages, "user", message.text)

    response = openai.ChatCompletion.create(
        model=model,  # Новая модель с контекстом
        messages=messages,  # База данных на основе словаря
    )

    await message.answer(response['choices'][0]['message']['content'], parse_mode="markdown")


def register_handlers(dp : Dispatcher):
    dp.middleware.setup(LimitedRequestsMiddleware(max_requests_per_day=15))
    dp.middleware.setup(LimitedRequestsMiddleware_min(delay_minutes=2))
    dp.register_message_handler(send)

