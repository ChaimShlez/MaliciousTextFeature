from KafkaConfigurations import KafkaProducerConfigurations


class Producer:

    def __init__(self):
        self.config = KafkaProducerConfigurations().producer_connect()
        # self.group_id = os.getenv("group_id", "interesting_id")

    def send_data(self, data_dict):
        self.publish_message("raw_tweets_antisemitic", data_dict["antisemitic"])
        self.publish_message("raw_tweets_not_antisemitic", data_dict["not_antisemitic"])

    def publish_message(self,topic, message):
        self.config.send(topic, message)
        self.config.flush()
        

            



