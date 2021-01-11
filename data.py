import os
import sqlite3
from sqlite3 import Error
import logging
from traceback import format_exc

logger = logging.getLogger('astro')

class Data:
    def __init__(self, db_path):
        logger.info('Class DataManager init')

        self.db_name = db_path

        try:
            self.conn = sqlite3.connect(os.path.abspath(self.db_name))
        except Error as e:
            logger.critical('Cannot connect to db: {}'.format(format_exc()))

        logger.debug('Class __init__ end')
    
    def create_table(self):
        pass

    def insert(self, data):
        pass

    def close(self):
        pass