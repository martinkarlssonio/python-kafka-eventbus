"""
Starts the Kafka container and python listener.
"""
import os
import logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")
import listener

if __name__ == "__main__":
    logging.info("martinkarlssonio/python-kafka-eventbus :: Starting Kafka containers..")
    os.system("cd kafkaContainer && docker-compose up -d --no-recreate")
    logging.info("martinkarlssonio/python-kafka-eventbus :: Start listening to topic")
    listener.startThreads()
    