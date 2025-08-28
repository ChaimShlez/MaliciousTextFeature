from data_processing import DataProcessing
from kafka_con import KafkaCon


class Main():

    def __init__(self):
        self.kafka_conn = KafkaCon()

    def run(self):
        while True:
            data = self.kafka_conn.consume_messages()
            date_dict = {
                "antisemitic": [],
                "not_antisemitic": []
            }

            for consumer_record in data:
                data_processing = DataProcessing(consumer_record.value)
                processed_data = data_processing.processing_text()
                if consumer_record.topic.endswith("not_antisemitic"):
                    date_dict["not_antisemitic"] = processed_data
                else:
                    date_dict["antisemitic"] = processed_data    
            self.kafka_conn.send_data(date_dict)
           
if __name__ == "__main__":
    main = Main()
    main.run()
    