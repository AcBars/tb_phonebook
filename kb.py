from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start = KeyboardButton('/start')
b1 = KeyboardButton('/Загрузить')
b2 = KeyboardButton('/Контакты')


kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(start).add(b1).add(b2)