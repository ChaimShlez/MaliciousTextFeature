import json

import pandas as pd
from bson import ObjectId
from kafka_con import KafkaCon
from datetime import datetime
from persister.Insert_to_data import InsertToData


class Main:

    def __init__(self):
        self.kafka_conn = KafkaCon()

    def run(self):
        try:
            while True:
                data = self.kafka_conn.consume_messages()
                data_from_db = InsertToData()
                for consumer_record in data:
                    topic=consumer_record.topic
                    consumer_record = consumer_record.value
                    print(consumer_record)
                    consumer_record=pd.DataFrame(consumer_record[0])
                    print(consumer_record)
                    # consumer_record['_id'] = consumer_record['_id'].apply(lambda x: ObjectId(x))
                    consumer_record['CreateDate'] = consumer_record['CreateDate'].apply(
                        lambda x: pd.to_datetime(x)
                    )

                    # consumer_record['CreateDate'] = pd.to_datetime(consumer_record['CreateDate'])

                    record = self.rename_col(consumer_record)

                    if topic.endswith("not_antisemitic"):
                        data_from_db.insert_data("not_antisemitic",record)
                    else:
                        data_from_db.insert_data("antisemitic",record)

        except Exception as e:
            print("Error: ", str(e))

    def rename_col(self,consumer_record):


        consumer_record.rename(columns={'TweetID': 'id', 'text': 'original_text',
                'CreateDate': 'createdate','Antisemitic': 'antisemietic'},inplace=True)
        return consumer_record.to_dict(orient='records')




if __name__ == "__main__":
    main = Main()
    main.run()
