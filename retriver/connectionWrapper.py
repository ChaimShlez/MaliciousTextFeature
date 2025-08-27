import os
import pymongo
class connectionWrapper:


    def __init__(self):

        self.mongo_user = os.getenv("MONGODB_USER","IRGC_NEW")
        self.mongo_password = os.getenv("MONGODB_PASSWORD", "iran135")
        self.mongo_db = os.getenv("MONGODB_DATABASE","IranMalDB")
        self.collection_name = os.getenv("MONGODB_COLLECTION", "tweets")
        self.client = pymongo.MongoClient(f"mongodb+srv://{self.mongo_user}:{self.mongo_password}@cluster0.6ycjkak.mongodb.net/")

        self.db = self.client[self.mongo_db]

    def get_data(self):

        collection = self.db[self.collection_name]
        return(list(collection.find({}, {"_id": 0})))




c=connectionWrapper()
print(c.get_data())