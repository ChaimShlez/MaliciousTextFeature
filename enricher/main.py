from kafka_con import KafkaCon
from data_processing import DataProcessing
from features import Features
import time


class Main:

    def __init__(self):
        self.kafka_conn = KafkaCon()
        self.processing = DataProcessing()
        self.weapons = self.read_file('weapon_list.txt')
        

    def run(self):
        try:
            processed_weapons = self.processing.processing_data_str(self.weapons)
            features = Features(processed_weapons)
            while True:
                data = self.kafka_conn.consume_messages()
                date_dict = {}
                for consumer_record in data:
                    data_with_features = features.add_features(consumer_record.value[0])
                    if consumer_record.topic.endswith("not_antisemitic"):
                        date_dict["enriched_preprocessed_tweets_antisemitic"] = data_with_features
                    else:
                        date_dict["enriched_preprocessed_tweets_not_antisemitic"] = data_with_features    
                    self.kafka_conn.send_data(date_dict)
                    time.sleep(30)
        except Exception as e:
            print("Error: ", str(e))

    def read_file(self, file_name):
        try:
            with open(file_name, 'r', encoding='utf-8-sig') as f:
                data = f.read()
            return data
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    main = Main()
    main.run()
    