import psycopg2
from pymongo import MongoClient

class Database:

    connection = None

    def __init__(self, db_host, db_port = None, db_name = None, db_user = None, db_password = None):
        pass

    def __del__(self):
        self.connection.close()

    def select_one(self):
        pass

    def select_all(self):
        pass


class Postgres(Database):

    cursor = None

    def __init__(self, db_host, db_port, db_name, db_user, db_password):
        self.connection = psycopg2.connect(host=db_host, port=db_port, database=db_name, user=db_user, password=db_password)

    def command(self, psql):
        self.cursor = self.connection.cursor()
        self.cursor.execute(psql)

    def select_one(self, query):
        self.command(query)
        return self.cursor.fetchone()

    def select_all(self, query):
        self.command(query)
        return self.cursor.fetchall()


class Mongo(Database):

    def __init__(self, db_host):
        self.connection = MongoClient(db_host)

    def select_one(self, query):
        db = self.connection.bss
        collection = db.all_messages
        return collection.find_one(query)

    def select_all(self, query):
        db = self.connection.bss
        collection = db.all_messages
        return list(collection.find(query))