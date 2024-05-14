import inspect
import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + "/logs/automation.log"
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler(path)
        format = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.DEBUG)
        return logger