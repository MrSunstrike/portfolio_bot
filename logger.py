import logging

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
file_handler = logging.FileHandler("global.log")
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
file_handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.addHandler(file_handler)

def setup_logger(name):
    file_handler = logging.FileHandler(name + ".log")
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    file_handler.setLevel(logging.INFO)

    local_logger = logging.getLogger(name)
    local_logger.addHandler(file_handler)

    return local_logger