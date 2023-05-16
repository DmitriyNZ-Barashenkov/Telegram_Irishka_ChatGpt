#Основной файл запуска frequency_penalty=0.0,, presence_penalty=0.6, temperature=0.5, max_tokens=1024, top_p=1.0, stop=None

import logging


from aiogram import types
from aiogram.utils import executor
#from aiogram.contrib.fsm_storage.memory import MemoryStorage


from communi_bot import dp
from handlers import handler, cmd_handler


logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logging.info("Отладочная информация")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



cmd_handler.register_handlers(dp)
handler.register_handlers(dp)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
