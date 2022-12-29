from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from create_bot import bot
import sql_db, kb



ID = None
class FSMAdmin(StatesGroup):
    surname = State()
    name = State()
    midlle_name = State()
    number_phone = State()

async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}!', reply_markup=kb.kb)

async def cm_start(message: types.Message):
    await FSMAdmin.surname.set()
    await message.reply('Введи фамилю')

async def load_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь введи имя')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите отчество')

async def load_midlle_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['midlle_name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите номер телефона')


async def load_number_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_phone'] = message.text
    await sql_db.add_sql(state)
    await state.finish()

async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

async def contact(message: types.Message):
    await sql_db.read_sql(message)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'])
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_surname, state=FSMAdmin.surname)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_midlle_name, state=FSMAdmin.midlle_name)
    dp.register_message_handler(load_number_phone, state=FSMAdmin.number_phone)
    dp.register_message_handler(cancel_handler, state="*", commands=['отмена'])
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(contact, commands=['Контакты'])