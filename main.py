from aiogram.utils import executor
from create_bot import dp
import sql_db
import tele_bot

async def on_startup(_):
    print('Бот вышел в онлайн.')
    sql_db.db_start()

tele_bot.register_handlers(dp)



executor.start_polling(dp, skip_updates = True, on_startup=on_startup)