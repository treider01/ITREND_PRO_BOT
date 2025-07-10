from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import start, catalog, order



API_TOKEN = "7789414834:AAET8zsZ4GYz_jZC8cVhaHCN3XNB86lGipY"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

start.register_handlers(dp)
catalog.register_handlers(dp)
order.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
