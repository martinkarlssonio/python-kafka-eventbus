#pip3 install kafka-python

#Ensure zookeper and kafka broker is started

from time import sleep
from datetime import datetime
from json import dumps
from kafka import KafkaProducer

import logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

import configuration
topics = configuration.kafkaTopics()

producer = KafkaProducer(bootstrap_servers=['localhost:29092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for topic in topics:
    data = {"eventType" : "someEventThatHappened", "timestamp" : str(datetime.now())}
    producer.send(topic, value=data)
    sleep(1)