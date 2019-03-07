"""Consumes and print"""

import json
import os

from kafka import KafkaConsumer

PRINT_GROUP = os.environ.get('CONSUMER_GROUP')
DEBUG = True
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
MUTATIONS_TOPIC = os.environ.get('MUTATIONS_TOPIC')

def is_rich(mutation: dict) -> bool:
    return mutation['amount'] >= 600

if __name__ == '__main__':
    consumer = KafkaConsumer(
        MUTATIONS_TOPIC,
        auto_offset_reset='earliest',
        bootstrap_servers=KAFKA_BROKER_URL,
        enable_auto_commit=True,
        group_id=PRINT_GROUP,
        value_deserializer=lambda value: json.loads(value)
    )

    total_mutation = 0
    total_rich_mutation = 0
    for message in consumer:
        mutation: dict = message.value
        if is_rich(mutation):
            total_rich_mutation += 1
            print("NEW VICTIM, I MEAN CONSUMER DETECTED: {}".format(mutation))
        total_mutation += 1

    print("found {} out of {} probable consumer".format(total_rich_mutation, total_mutation))