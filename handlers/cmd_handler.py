# handler commands

from aiogram import types
from communi_bot import Dispatcher, bot
from keyboard.kb import start_keyboard



async def cmd_start(message: types.Message):
    await message.answer("Привет! Меня зовут Иришка! Я ИИ бот на базе ChatGPT от компании OpenAI. Напишите Ваш запрос!", reply_markup=start_keyboard)

async def cmd_help(message: types.Message):
    await message.answer("Список доступных команд:\n/start - начать диалог с Иришкой.\n/help - получить список доступных команд.\n/info - получить описание бота.\n/donat - поддержать разработку Иришки", reply_markup=start_keyboard)

async def cmd_donat(message: types.Message):
    await message.answer("https://pay.mysbertips.ru/37382224, Спасибо, что решил поддержать разработку Иришки! Нажми на ссылку выше, чтобы перейти на страницу оплаты", reply_markup=start_keyboard)
    await message.answer("Перейдите по ссылке, выберете 'Быстрая оплата в SberPay', "
                         "укажите номер телефона в Сбере и нажмите отправить, после чего вам придет пуш-уведомление в приложение сбербанк")

async def cmd_info(message: types.Message):
    await message.answer("Телеграм-бот ChatGPT - это бот, который работает на базе модели GPT из компании OpenAI, и может проводить диалоги с пользователями, используя нейросеть для генерации текста.\n"
                         "Чтобы начать диалог с ChatGPT, необходимо написать боту в личном сообщении. Бот будет приветствовать пользователя и предложит начать диалог.\n "
                         "Чтобы задать вопрос, нужно отправить сообщение с текстом в чат-бота. После этого, бот сгенерирует ответ на основе заданного текста.\n"
                         "В ответном сообщении бот может предоставить ссылку на дополнительную информацию или ресурсы.\n "
                         "Пользователь может задавать дополнительные вопросы, и бот будет продолжать генерировать ответы на основе нового входного текста.\n"
                         "Для более точного ответа, необходимо задавать вопросы четко и конкретно.\n "
                         "Лучше задавать вопросы, которые можно ответить «Да» или «Нет», либо вопросы, на которые можно ответить числовым значением.\n"
                         "Бот написан энтузиастом, если хотите отблагодарить ботописца Welcom! - /donat")

async def cmd_support(message: types.Message):
    await message.answer("Если у тебя возникли проблемы или вопросы, напиши мне на email rudopan5@gmail.com")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands={"start", "старт"})
    dp.register_message_handler(cmd_help, commands={"help", "помощь"})
    dp.register_message_handler(cmd_donat, commands={"спасибо", "donat"})
    dp.register_message_handler(cmd_support, commands={"support", "поддержка"})
    dp.register_message_handler(cmd_info, commands={"info", "информация"})