import json
import os

from kafka import KafkaProducer, KafkaConsumer


class KafkaProducerConfigurations:

    @staticmethod
    def producer_connect():
        try:
            producer = KafkaProducer(
                bootstrap_servers=os.getenv("KAFKA_BROKER", "localhost:9095"),
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            return producer
        except Exception as e:
            print(str(e))
            return

    
    @staticmethod
    def consumer_connect(topic):
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers='localhost:9095',
            auto_offset_reset='earliest',
            group_id="my_consumer_group",
            enable_auto_commit=True,
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )
        return consumer





