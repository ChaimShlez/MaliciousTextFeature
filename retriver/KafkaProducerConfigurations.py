import json
import os

from kafka import KafkaProducer

class KafkaProducerConfigurations:
    def __init__(self):
        self.producer = self.get_producer_config()


    def get_producer_config(self):

        producer = KafkaProducer(
            bootstrap_servers=os.getenv("KAFKA_BROKER", "kafka_service:9092"),
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        return producer








