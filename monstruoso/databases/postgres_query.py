from monstruoso.databases.database import Postgres

class PostgresQuery:

    #data from config
    db_name = 'catalogDB'
    db_user = 'pgsql'
    db_password= 'pgsql'
    db_host = 'localhost'
    db_port = 5432

    db = Postgres(db_host, db_port, db_name, db_user, db_password)

    def getDataById(self, id):
        query = 'SELECT * FROM firm_1 WHERE id = %s'%id
        return self.db.select_one(query)