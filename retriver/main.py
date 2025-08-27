from connectionWrapper import MongoClient
from producer import Producer
from dataSplitter import DataSplitter
import time

class Main():

    def __init__(self):
        self.mongo_client = MongoClient()
        self.kafka_producer = Producer() 

    def get_100_doc(self):
        return self.mongo_client.get_data()
    
    def run(self):
        while True:
            try: 
                data = self.get_100_doc()
                data_splitted = DataSplitter.split_by_col(data)
                self.kafka_producer.send_data(data_splitted)
                time.sleep(60)
            except Exception as e:
                print(str(e))
                return {"Error" : str(e)}

   
    
if __name__ == "__main__":
    main = Main()
    main.run()
    





