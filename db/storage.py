from sqlite3 import connect


class DatabaseManager:
    def __init__(self, path='db/database.db'):
        self.conn = connect(path)  # подключаемся к базе данных
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()  # сохраняем изменения
        self.cursor = self.conn.cursor()  # Курсор позволяет отправлять SQL-запросы базе данных и получать результаты

    def create_tables(self):
        self.add_new_info(
            'CREATE TABLE IF NOT EXISTS users ('
            'user_id INTEGER PRIMARY KEY,'
            'orders TEXT,'
            'discount BLOB,'
            'buy_date TEXT,'
            'finish_date TEXT)'
        )
        self.add_new_info(
            'CREATE TABLE IF NOT EXISTS questions ('
            'qa_id INTEGER,'
            'user_id INTEGER,'
            'FOREIGN KEY (user_id)  REFERENCES users (user_id)'
            'question TEXT NOT NULL,'
            'answer TEXT)'
        )

    # Пример заполнения: 'INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
    # ('newuser', 'newuser@example.com', 28)
    def add_new_info(self, arg, values=None):
        if values is None:
            self.cursor.execute(arg)
        else:
            self.cursor.execute(arg, values)
        self.conn.commit()

    # Обновляем информацию (например, добавляем наш ответ на вопрос)
    def update_info(self, arg, values=None):  # 'UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser')
        if values is None:
            pass
        else:
            self.cursor.execute(arg, values)
        self.conn.commit()

    # Выбираем первого пользователя
    def fetchone(self, arg, values=None):  # 'SELECT username, age FROM Users WHERE age > ?', (25,)
        if values is None:
            pass
        else:
            self.cursor.execute(arg, values)
        return self.cursor.fetchone()

    # Выбираем всех пользователей
    def fetchall(self, arg, values=None):  # 'SELECT username, age FROM Users WHERE age > ?', (25,)
        if values is None:
            pass
        else:
            self.cursor.execute(arg, values)
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
