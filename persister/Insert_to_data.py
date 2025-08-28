import os
import pymongo

class InsertToData:
    def __init__(self):
        self.mongo_user = os.getenv("MONGODB_USER", "admin")
        self.mongo_password = os.getenv("MONGODB_PASSWORD", "secretpassword")
        self.mongo_db = os.getenv("MONGODB_DATABASE", "mydb")

        self.client = pymongo.MongoClient(
            f"mongodb://{self.mongo_user}:{self.mongo_password}@localhost:27017/"
        )
        self.db = self.client[self.mongo_db]



    def get_data(self, collection_name):
        collection = self.db[collection_name]
        return list(collection.find({}, {"_id": 0}))



