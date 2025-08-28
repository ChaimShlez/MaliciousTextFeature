import json
import os

from kafka import KafkaProducer, KafkaConsumer


class KafkaProducerConfigurations:

    @staticmethod
    def producer_connect():

        producer = KafkaProducer(
            bootstrap_servers=os.getenv("KAFKA_BROKER", "localhost:9095"),
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        return producer
    @staticmethod
    def consumer_connect(topic_one,topic_two, group_id):
        consumer = KafkaConsumer(
            topic_one,topic_two,
            bootstrap_servers='localhost:9095',
            auto_offset_reset='earliest',
            group_id=group_id,
            enable_auto_commit=True,
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            consumer_timeout_ms=10000
        )
        return consumer





