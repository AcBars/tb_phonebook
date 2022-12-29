import sqlite3 as sq
import create_bot

def db_start():
    global cur, base
    base =sq.connect('phone_book.db')
    cur =base.cursor()
    if base:
        print('База данных подключена.')
    base.execute("CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY AUTOINCREMENT, surname TEXT,"
                 "name TEXT, midlle_name TEXT, phone_number TEXT)")
    base.commit()
async def add_sql(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO person (surname, name, midlle_name, phone_number) VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit()

async def read_sql(message):
    for ret in cur.execute("SELECT * FROM person").fetchall():
        await create_bot.bot.send_message(message.from_user.id, f'Фамилия: {ret[1]}\nИмя: {ret[2]}\nОтчество: {ret[3]}\nНомер телефона: {ret[4]}')