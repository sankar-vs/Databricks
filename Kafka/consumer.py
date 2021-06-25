'''
@Author: Sankar
@Date: 2021-06-22 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-06-25 12:35:49
@Title : Kafka Consumer
'''
from kafka import KafkaConsumer

consumer = KafkaConsumer('demo',bootstrap_servers=['localhost:9092'], api_version=(0,10,1))
for msg in consumer:
    print (msg.value)