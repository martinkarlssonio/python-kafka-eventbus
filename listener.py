#pip3 install kafka-python
from kafka import KafkaConsumer
from json import loads
import threading

import logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")
import configuration

topics = configuration.kafkaTopics()

def listenToTopic(topic):
    logging.info("martinkarlssonio/python-kafka-eventbus :: Listening on topic '{}'.".format(topic))
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=["localhost:29092"],
        auto_offset_reset="earliest", #Start reading the log from earliest or latest upon restart
        enable_auto_commit=True, #Makes sure the consumer commits its read offset every interval
        group_id="eventbus",
        value_deserializer=lambda x: loads(x.decode("utf-8"))) #Deserializes the data into a common json format

    for message in consumer:
        message = message.value
        logging.info("martinkarlssonio/python-kafka-eventbus :: New event on topic {} : {}".format(topic,message))

def startThreads():
    threads = list()
    for topic in topics:
        logging.info("martinkarlssonio/python-kafka-eventbus :: Adding topic {}".format(topic))
        x = threading.Thread(target=listenToTopic, args=(topic,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()

if __name__ == "__main__":
    logging.info("martinkarlssonio/python-kafka-eventbus :: Listner started.")