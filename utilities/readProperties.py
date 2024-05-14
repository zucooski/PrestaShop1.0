import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"/configrations/config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get("PrestaShop", "baseurl")
        return url

    @staticmethod
    def getEmail():
        email = config.get("PrestaShop","email")
        return email

    @staticmethod
    def getPassword():
        pwd = config.get("PrestaShop","pwd")
        return pwd
