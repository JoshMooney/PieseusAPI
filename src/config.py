import os
import json

DATA_DIR = os.getenv('DATA_DIR' , '/home/api')

FLASK = {
    "host": "127.0.0.1",
    "port": "5000"
}

DEFAULT_PORT = "5000"
LOCAL_ADDRESS = "127.0.0.1"
EXTERNAL_IP = "80.111.5.9"
DOMAIN_NAME = "http://www.Theseus.tk"

FLASH_DOWNLOAD_DIR_NAME = "flash_downloads"
FLASH_DOWNLOAD_DIR = "./{}".format(FLASH_DOWNLOAD_DIR_NAME)