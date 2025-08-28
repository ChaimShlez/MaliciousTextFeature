import os

from utils.KafkaConfigurations import KafkaProducerConfigurations


class KafkaCon:
    def __init__(self):

        self.con_consumer=KafkaProducerConfigurations().consumer_connect(
            "preprocessed_tweets_antisemitic","preprocessed_tweets_not_antisemitic","group_id")


    def consume_messages(self):
        return self.con_consumer




