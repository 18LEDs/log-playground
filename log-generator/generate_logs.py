import time
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

messages = [
    "User login successful",
    "User logout",
    "File uploaded",
    "Database connection error",
    "Cache miss",
    "File not found",
    "Task completed",
]

while True:
    msg = random.choice(messages)
    logging.info(msg)
    time.sleep(0.1)
