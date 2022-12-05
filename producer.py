from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer = lambda x:dumps(x).encode('utf-8')
    )

while True:
    my_data = {'sr' : round(random.uniform(45, 100), 2), 'rr' : round(random.uniform(16, 30), 2), 't' : round(random.uniform(85, 99), 2), 'lm' : round(random.uniform(4, 19), 2), 'bo' : round(random.uniform(82, 97), 2), 'rem': round(random.uniform(60, 105), 2), 'sr.1' :round(random.uniform(0, 9), 2), 'hr': round(random.uniform(50, 85), 2)}
    my_producer.send('pillow', value = my_data)
    sleep(5)