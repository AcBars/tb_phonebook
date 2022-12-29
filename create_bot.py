from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

token = input('Введите токен бота: ')
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)