#Основной файл запуска frequency_penalty=0.0,, presence_penalty=0.6, temperature=0.5, max_tokens=1024, top_p=1.0, stop=None

import logging
#from communi_bot import os

from aiogram import types
from aiogram.utils import executor
from aiogram.bot.bot import Bot
from communi_bot import load_dotenv, find_dotenv, bot
#from aiogram.contrib.fsm_storage.memory import MemoryStorage


from communi_bot import dp
from handlers import handler, cmd_handler, image_handler

load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logging.info("Отладочная информация")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#async def on_startup(dp):
#    await bot.set_webhook(os.getenv("HOST_DOMEN"))

#async def on_shotdawn(dp):
#    await bot.delete_webhook()



cmd_handler.register_handlers(dp)
image_handler.register_handlers(dp)
handler.register_handlers(dp)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    #executor.start_webhook(dispatcher=dp, webhook_path="", on_startup=on_startup, on_shutdown=on_shotdawn, skip_updates=True, host='0.0.0.0', port=int(os.environ.get('PORT',3001)))