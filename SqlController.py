import psycopg2
import datetime
import os
from dotenv import load_dotenv


class SqlController:

    def __init__(self):
        self.host = os.getenv("HOST")
        self.database = os.getenv("DATABASE")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")

        self.db_params = {
            'host': 'localhost',
            'database': 'zipdb-docker',
            'user': 'postgres',
            'password': 'postgres'
        }

        self.connection = psycopg2.connect(**self.db_params)

        self.cursor = self.connection.cursor()

    def get_users(self):
        self.cursor.execute("SELECT name, password, company, customer_code, type, created_at FROM \"user\" ORDER BY name;")

        rows = self.cursor.fetchall()

        return rows

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def add_user(self, name, password, company, customer_code, entry_type):
        self.cursor.execute(
            "INSERT INTO \"user\" (name, password, company, customer_code, type, created_at) VALUES (%s, %s, %s, %s, %s, %s);",
            (name, password, company, customer_code, entry_type, datetime.datetime.now()))

        self.connection.commit()

    def delete_user(self, user_name):
        self.cursor.execute("DELETE FROM \"user\" WHERE name = %s;", (user_name,))

        self.connection.commit()
