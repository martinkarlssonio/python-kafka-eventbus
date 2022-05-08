import json

import logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


if __name__ == "__main__":
    logging.info("martinkarlssonio/python-kafka-eventbus :: Listner started.")