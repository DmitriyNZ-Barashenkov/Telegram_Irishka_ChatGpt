import os
import openai
import datetime

from aiogram import Dispatcher, Bot, types
from dotenv import load_dotenv, find_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from admin_fun.middlewares import LimitedRequestsMiddleware, LimitedRequestsMiddleware_min

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv("TOKEN"), parse_mode=types.ParseMode.HTML)
openai.api_key=token=os.getenv("OPENAI")


dp = Dispatcher(bot, storage=MemoryStorage())

def is_24_hours_passed(last_request_datetime: datetime.datetime) -> bool:
    """Проверяет, прошло ли 24 часа с момента последнего запроса от пользователя."""
    timedelta = datetime.datetime.now() - last_request_datetime
    hours_passed = timedelta.total_seconds() / 3600
    return hours_passed >= 24




if __name__ == "__main__":
    print(openai.api_key)