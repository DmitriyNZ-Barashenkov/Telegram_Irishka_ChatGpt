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

def analytics (func: callable):
    total_message = 0
    users = set()
    total_users = 0
    def analytics_wrapper(message):
        nonlocal total_message, total_users
        total_message += 1

        if message.chat.id not in users:
            users.add(message.chat.id)
            total_users += 1

        print("New message: ", message.text, "Total: ", total_message, "Total users: ", total_users)
        return func(message)
    return analytics_wrapper

@ analytics
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

