"""Produce fake mutations"""

import os # env variable
from time import sleep # i like sleep
import json

from kafka import KafkaProducer

from generators import generate_random_transaction

DEBUG = True
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
MUTATIONS_TOPIC = os.environ.get('MUTATIONS_TOPIC')
TRANSACTIONS_PER_SECOND = int(os.environ.get('TPS'))

SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

if __name__ == '__main__':
    print("Starting Kafka Producer...")
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        # json encode
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    print("Ready to Produce!")
    while True:
        mutation: dict = generate_random_transaction()
        producer.send(MUTATIONS_TOPIC, value=mutation)
        if DEBUG:
            print(mutation)
        sleep(SLEEP_TIME)