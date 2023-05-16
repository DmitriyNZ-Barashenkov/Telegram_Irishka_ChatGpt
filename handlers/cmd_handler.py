# handler commands

from aiogram import types
from communi_bot import Dispatcher, bot
from keyboard.kb import start_keyboard



async def cmd_start(message: types.Message):
    await message.answer("Привет! Меня зовут Иришка! Я ИИ бот на базе ChatGPT от компании OpenAI. Напиши твой запрос!", reply_markup=start_keyboard)

async def cmd_help(message: types.Message):
    await message.answer("Список доступных команд:\n/start - начать диалог с Иришкой\n/help - получить список доступных команд\n/donate - поддержать разработку Иришки", reply_markup=start_keyboard)

async def cmd_donat(message: types.Message):
    await message.answer("https://pay.mysbertips.ru/37382224, Спасибо, что решил поддержать разработку Иришки! Нажми на ссылку выше, чтобы перейти на страницу оплаты", reply_markup=start_keyboard)
    await message.answer("Перейдите по ссылке, выберете 'Быстрая оплата в SberPay', "
                         "укажите номер телефона в Сбере и нажмите отправить, после чего вам придет пуш-уведомление в приложение сбербанк")


async def cmd_support(message: types.Message):
    await message.answer("Если у тебя возникли проблемы или вопросы, напиши мне на email rudopan5@gmail.com")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands={"start", "старт"})
    dp.register_message_handler(cmd_help, commands={"help", "помощь"})
    dp.register_message_handler(cmd_donat, commands={"donate", "оплата подписки"})
    dp.register_message_handler(cmd_support, commands={"support", "поддержка"})