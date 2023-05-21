import os

from communi_bot import openai
from aiogram import types
from communi_bot import Dispatcher, bot
from dotenv import load_dotenv, find_dotenv

# Обработчик команды /image


async def send_image(message: types.Message):
    response = openai.Image.create(
        prompt=message.text,
        n=1,
        size="1024x1024",
    )
    await message.answer_photo(response["data"][0]["url"])

def register_handlers(dp : Dispatcher):
    dp.register_message_handler(send_image, commands=['dalle'])
