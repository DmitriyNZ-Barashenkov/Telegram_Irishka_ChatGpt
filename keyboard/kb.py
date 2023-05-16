#  все клавиатуры, используемые ботов.
#  В этом файле будут находиться абсолютно все клавиатуры, как статические,
#  так и динамически генерируемые через функции

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, WebAppInfo, KeyboardButtonPollType

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_button = KeyboardButton("/start")
help_button = KeyboardButton("/help")
donate_button = KeyboardButton("/спасибо разработчику")
support_button = KeyboardButton("/Поддержка")

start_keyboard.add(start_button, help_button, donate_button, support_button)