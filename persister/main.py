from data_processing import DataProcessing
from kafka_con import KafkaCon
import time
import pandas as pd

from persister.Insert_to_data import InsertToData


class Main():

    def __init__(self):
        self.kafka_conn = KafkaCon()

    def run(self):
        try:
            while True:
                data = self.kafka_conn.consume_messages()
                data_from_db = InsertToData()

                for consumer_record in data:


                    if consumer_record.topic.endswith("not_antisemitic"):
                        data_from_db.insert_data("not_antisemitic")
                    else:
                        data_from_db.insert_data("antisemitic")

        except Exception as e:
            print("Error: ", str(e))


if __name__ == "__main__":
    main = Main()
    main.run()
