import psycopg2
import redis
from pymongo import MongoClient
from psycopg2.extras import RealDictCursor

class Database(object):

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

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def command(self, psql):
        self.connection.cursor_factory = RealDictCursor
        self.cursor = self.connection.cursor()
        self.cursor.execute(psql)

    def select_one(self, query):
        self.command(query)
        return self.cursor.fetchone()

    def select_all(self, query):
        self.command(query)
        return self.cursor.fetchall()

    def insert_row(self, query):
        self.command(query)


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

class Redis(Database):

    def __init__(self, db_host):
        self.connection = redis.StrictRedis(db_host)

    def get_keys(self):
        return self.connection.keys()

    def get_keys_by_pattern(self, pattern):
        return self.connection.keys(pattern)

class Connection(object):

    def create_db_connection(self, type, host, port = None, user = None, password = None, db_name = None):
        if type == 'postgres':
            return Postgres(host, port, db_name, user, password)
        if type == 'mongo':
            return Mongo(host)
        if type == 'redis':
            return Redis(host)
        else:
            pass