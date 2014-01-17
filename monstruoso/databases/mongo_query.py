from database import Mongo

class MongoQuery:

    #data from config
    db_host = 'uran.qa.test'

    db = Mongo(db_host)

    def getDataByUser(self, user):
        query = {"user":"%s"%user}
        return self.db.select_all(query)

    def getDataByIp(self, ip):
        query = {"ip":"%s"%ip}
        return self.db.select_one(query)