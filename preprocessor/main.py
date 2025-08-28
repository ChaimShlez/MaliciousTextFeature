from data_processing import DataProcessing
from kafka_con import KafkaCon
import time
import pandas as pd

class Main():

    def __init__(self):
        self.kafka_conn = KafkaCon()

    def run(self):
        try:
            while True:
                data = self.kafka_conn.consume_messages()
                data_processing = DataProcessing()
                
                for consumer_record in data:
                    date_dict = {}
                    processed_data = data_processing.processing_list_data(consumer_record.value)
                    if consumer_record.topic.endswith("not_antisemitic"):
                        date_dict["preprocessed_tweets_not_antisemitic"] = processed_data
                    else:
                        date_dict["preprocessed_tweets_antisemitic"] = processed_data    
                    self.kafka_conn.send_data(date_dict)
                    time.sleep(60)
        except Exception as e:
            print("Error: ", str(e))


           
if __name__ == "__main__":
    main = Main()
    main.run()
    