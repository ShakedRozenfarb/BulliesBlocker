from pymongo import MongoClient


class MongoHandler(object):
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 27018
        self.mongo_client = MongoClient(host=self.host, port=self.port)["bullyblocker"]

    def get_mongo_client(self):
        return self.mongo_client

    def get_caching_mongo_client(self):
        return self.get_mongo_client()["cache"]
