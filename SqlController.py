import psycopg2


class SqlController:

    def __init__(self):
        self.db_params = {
            'host': 'localhost',
            'database': 'zipdb',
            'user': 'daniel',
            'password': '1324'
        }

        self.connection = psycopg2.connect(**self.db_params)

        self.cursor = self.connection.cursor()

    def get_users(self):
        self.cursor.execute("SELECT name, password FROM \"user\";")

        rows = self.cursor.fetchall()

        return rows

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def add_user(self, name, password):
        self.cursor.execute("INSERT INTO \"user\" (name, password) VALUES (%s, %s);", (name, password))

        self.connection.commit()

    def delete_user(self, user_name):
        self.cursor.execute("DELETE FROM \"user\" WHERE name = %s;", (user_name,))

        self.connection.commit()
