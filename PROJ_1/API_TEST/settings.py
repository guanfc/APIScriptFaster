import os
from loguru import logger

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logger.add(
    sink=os.path.join(BASE_DIR, 'logs/runtime_{time}.log'),
    encoding='utf-8'
)

BASIC_URI = "https://mch.test.p.thinkinpower.net"


if __name__ == '__main__':
    print("BASE_DIR:", BASE_DIR)
