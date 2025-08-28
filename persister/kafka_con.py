from KafkaConfigurations import KafkaProducerConfigurations


class KafkaCon:
    def __init__(self):

        self.con_consumer=KafkaProducerConfigurations().consumer_connect(
            "enriched_preprocessed_tweets_antisemitic",
            "enriched_preprocessed_tweets_not_antisemitic",
            "group_id")


    def consume_messages(self):
        return self.con_consumer




