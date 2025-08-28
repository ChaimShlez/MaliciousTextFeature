from KafkaConfigurations import KafkaProducerConfigurations


class KafkaCon:
    def __init__(self):
        self.con_producer = KafkaProducerConfigurations().producer_connect()
        self.con_consumer=KafkaProducerConfigurations().consumer_connect(
            "raw_tweets_not_antisemitic",
            "raw_tweets_antisemitic", 
            "group_id")

    def send_data(self, data_dict):
        self.publish_message(str(list(data_dict.keys())[0]), list(data_dict.values()))
    

    def publish_message(self, topic, message):
        self.con_producer.send(topic, message)
        self.con_producer.flush()

    def consume_messages(self):
        return self.con_consumer




