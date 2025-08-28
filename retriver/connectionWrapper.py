import os
import pymongo
from datetime import datetime


class MongoClient:
    
    def __init__(self):
        self.mongo_user = os.getenv("MONGODB_USER","IRGC_NEW")
        self.mongo_password = os.getenv("MONGODB_PASSWORD", "iran135")
        self.mongo_db = os.getenv("MONGODB_DATABASE","IranMalDB")
        self.collection_name = os.getenv("MONGODB_COLLECTION", "tweets")
        self.client = pymongo.MongoClient(f"mongodb+srv://{self.mongo_user}:{self.mongo_password}@cluster0.6ycjkak.mongodb.net/")

        self.db = self.client[self.mongo_db]

        self.start_date = datetime.strptime("1900-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")

    def get_data(self):
        collection = self.db[self.collection_name]
        data = list(collection.find({"CreateDate" : {"$gt" : self.start_date}},{'_id':0}).sort({'CreateDate' : 1}).limit(100))
        self.start_date = data[-1]['CreateDate']
        return data

