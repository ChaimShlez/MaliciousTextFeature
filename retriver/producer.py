import os

from retriver.KafkaProducerConfigurations import KafkaProducerConfigurations


class Producer:

    def __init__(self):
        self.config = KafkaProducerConfigurations()
        self.topic = os.getenv("topic", "interesting")
        # self.group_id = os.getenv("group_id", "interesting_id")



    def send_data(self, data_dict):

        self.run_producer("raw_tweets_antisemitic", data_dict["antisemitic"])
        self.run_producer("raw_tweets_not_antisemitic", data_dict["not_antisemitic"])

                 


    def publish_message(self,topic, message):
        self.config.producer.send(topic, message)

    def run_producer(self,topic,data):

            self.publish_message(topic,data)
            self.config.producer.flush()



