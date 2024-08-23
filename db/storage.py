from sqlite3 import connect
# Что можно вытащить из сообщения:
# Message.message_id (id сообщения)
# Message.date (дата и время отправки сообщения)
# Message.text (текст сообщения)
# Message.html_text (забираем текст с htm-тегами)
# Message.from_user (username, first_name, last_name, full_name, is_premium и прочее)
# Message.chat (id, type, title, username/channel) То есть мы можем сделать примерно такой словарь:
# data_task = {'user_id': message.from_user.id, 'full_name': message.from_user.full_name,
# 'username': message.from_user.username, 'message_id': message.message_id, 'date': get_msc_date(message.date)}

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
            'tg_id INTEGER,'
            'user_name TEXT,'
            'price INTEGER)'
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
            self.cursor.execute(arg)
        else:
            self.cursor.execute(arg, values)
        self.conn.commit()

    # Выбираем первого пользователя
    def fetchone(self, arg, values=None):  # 'SELECT username, age FROM Users WHERE age > ?', (25,)
        if values is None:
            self.cursor.execute(arg)
        else:
            self.cursor.execute(arg, values)
        return self.cursor.fetchone()

    # Выбираем всех пользователей
    def fetchall(self, arg, values=None):  # 'SELECT username, age FROM Users WHERE age > ?', (25,)
        if values is None:
            self.cursor.execute(arg)
        else:
            self.cursor.execute(arg, values)
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
