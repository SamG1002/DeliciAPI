from pymongo import MongoClient

class Database:
    _db = None

    @classmethod
    def connect(cls, connection_string, db_name):
        cls._db = MongoClient(connection_string)[db_name]

    @classmethod
    def disconnect(cls):
        cls._db.client.close()

    @classmethod
    def get_collection(cls, collection_name):
        return cls._db[collection_name]
