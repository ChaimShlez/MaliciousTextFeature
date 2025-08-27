import os

from utils.KafkaConfigurations import KafkaProducerConfigurations


class KafkaCon:
    def __init__(self):
        self.con_producer = KafkaProducerConfigurations().producer_connect()
        self.con_consumer=KafkaProducerConfigurations().consumer_connect("preprocessed_tweets_antisemitic","preprocessed_tweets_not_antisemitic")

    def send_data(self, data_dict):
        self.publish_message(os.getenv("TOPIC_A","enriched_preprocessed_tweets_antisemitic"), data_dict["antisemitic"])
        self.publish_message(os.getenv("TOPIC_B","enriched_preprocessed_tweets_not_antisemitic"), data_dict["not_antisemitic"])


    def publish_message(self, topic, message):
        self.con_producer.send(topic, message)
        self.con_producer.flush()

    def consume_messages(self):
        return self.con_consumer




