from kafka import KafkaConsumer
from json import loads
import json
import threading
import os

import logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")
import configuration

topics = configuration.kafkaTopics()

def takeAction(actionCommand):
    os.system(actionCommand)


def listenToTopic(topic):
    logging.info("martinkarlssonio/python-kafka-eventbus :: Listening on topic '{}'.".format(topic))
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=["localhost:29092"],
        auto_offset_reset="earliest", #Start reading the log from earliest or latest upon restart
        enable_auto_commit=True, #Makes sure the consumer commits its read offset every interval
        group_id="eventbus", #The group that consumes the message
        value_deserializer=lambda x: loads(x.decode("utf-8"))) #Deserializes the data into a common json format

    for message in consumer:
        message = message.value
        logging.info("martinkarlssonio/python-kafka-eventbus :: New event on topic {} : {}".format(topic,message))
        eventName = message['eventName']
        #Take action here
        try:
            with open("eventConfig/{}.json".format(topic)) as topicConfigFile:
                data = json.load(topicConfigFile)
                events = data['events']
                eventsActions = events[eventName]['actions']
                actionThreads = list() #Create a list with action to be taken from the event
                for action in eventsActions:
                    actionType = action["actionType"]
                    actionTarget = action["actionTarget"]
                    actionCommand = configuration.getActionCommand(actionType,actionTarget)
                    logging.info("martinkarlssonio/python-kafka-eventbus :: Execute actionCommand '{}' for eventName : {}".format(actionCommand,eventName))
                    x = threading.Thread(target=takeAction, args=(actionCommand,)) #Execute the action in a seperate thread to not block this one
                    x.start()
        except Exception as e:
            print(e)
            logging.error("martinkarlssonio/python-kafka-eventbus :: No configuration found for topic {}".format(topic))

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
    logging.info("martinkarlssonio/python-kafka-eventbus :: Listener started.")