import aiosqlite


class DatabaseManager:
    def __init__(self):
        self.path = 'db/database.db'

    async def initialize_database(self):
        async with aiosqlite.connect(self.path) as db:
            await db.execute(
                'CREATE TABLE IF NOT EXISTS users ('
                'user_telegram_id INTEGER PRIMARY KEY,'
                'username TEXT,'
                'price INTEGER)'
            )
            await db.commit()

    async def check_user_not_paid_before(self, user_telegram_id: int):
        async with aiosqlite.connect(self.path) as db:
            cursor = await db.execute("SELECT * FROM users WHERE user_telegram_id = ?", (user_telegram_id, ))
            row = await cursor.fetchone()
            if row is None:
                return True
            else:
                return False

    async def add_user(self, user_telegram_id: int, username: str, price: int):
        async with aiosqlite.connect(self.path) as db:
            await db.execute(
                'INSERT INTO users (user_telegram_id, username, price)'
                'VALUES (?, ?, ?)',
                (user_telegram_id, username, price))
            await db.commit()

    async def check_user_amount(self):
        async with aiosqlite.connect(self.path) as db:
            cursor = await db.execute("SELECT * FROM users")
            rows = await cursor.fetchall()
            return len(rows)

    async def get_usernames(self):
        async with aiosqlite.connect(self.path) as db:
            cursor = await db.execute("SELECT username FROM users")
            usernames = await cursor.fetchall()
            return usernames

    async def get_earned_money(self):
        async with aiosqlite.connect(self.path) as db:
            cursor = await db.execute("SELECT SUM (price) FROM users")
            earned_money = await cursor.fetchone()
            return earned_money[0]

