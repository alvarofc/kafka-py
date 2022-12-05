from json import loads
from kafka import KafkaConsumer
import pickle
import pandas as pd
import json
my_consumer = KafkaConsumer(
    'pillow',
    bootstrap_servers=['localhost : 9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
loaded_model = pickle.load(open("model.sav", 'rb'))

for message in my_consumer:
    print(message.value)
    message = pd.DataFrame([message.value])
    result = loaded_model.predict(message)
    if result >= 4:
        print(f"User is very stressed. Result: {result}")
    elif result >= 3:
        print(f"User is stressed. Result: {result}")
    else:
        print(f"User is resting correctly. Result: {result}")
