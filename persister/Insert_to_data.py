import os
from datetime import datetime
import pymongo

class InsertToData:
    def __init__(self):
        self.mongo_user = os.getenv("MONGODB_USER", "admin")
        self.mongo_password = os.getenv("MONGODB_PASSWORD", "secretpassword")
        self.mongo_db = os.getenv("MONGODB_DATABASE", "mydb")
        # self.collection_name = os.getenv("MONGODB_COLLECTION", "interesting")

        self.client = pymongo.MongoClient(
            f"mongodb://{self.mongo_user}:{self.mongo_password}@mongodb:27017/"
        )

        self.topic = os.getenv("TOPIC", "interesting")
        self.group_id = os.getenv("GROUP_ID", "interesting_id")
        self.db = self.client[self.mongo_db]
        # self.consumer = KafkaConsumerConfigurations().config_consumer(
        #     self.topic, self.group_id
        # )

    def insert_data(self,collection_name):
        collection = self.db[collection_name]
        return list(collection.find({}, {"_id": 0}))


