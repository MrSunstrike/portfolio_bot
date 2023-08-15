import logging
from config import LOG_FORMAT

def setup_logger(name):
    logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)

    file_handler = logging.FileHandler(name + ".log")
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    file_handler.setLevel(logging.INFO)

    logger = logging.getLogger()
    logger.addHandler(file_handler)

    return logger