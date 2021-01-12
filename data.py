import os
import sqlite3
from sqlite3 import Error
import logging
from traceback import format_exc
from datetime import datetime

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
        logger.debug('Function create_table start')

        table = """CREATE TABLE IF NOT EXISTS data (
            id integer PRIMARY KEY,
            time timestamp NOT NULL,
            img_name INTEGER,
        );"""

        try:
            c = self.conn.cursor()

            # Create table
            c.execute(table)

            self.conn.commit()

            logger.info('Created a table')

            return True
        except Exception as e:
            table_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='spwords'"
            if self.conn.execute(table_exists).fetchone() and isinstance(e, sqlite3.OperationalError):
                # sqlite3 docs say ProgrammingError is raised when table exists, although OperationalError was raised when testing.
                logger.warning('Table already exists: {}'.format(format_exc()))
                return True

            logger.critical('Could not create a table: {}'.format(format_exc()))
            return False

        logger.debug('Function create_table end')

    def insert(self, img_name):
        logger.debug('Function insert_data start')

        sql = ''' INSERT INTO sensor_data(time,img_name)
                VALUES(?,?) '''

        try:
            cur = self.conn.cursor()

            # Insert a row of data
            cur.execute(sql, (datetime.now(), img_name))

            self.conn.commit()

            logger.info('Inserted a row of data: id {}'.format(cur.lastrowid))

            return cur.lastrowid
        except Error as e:
            logger.critical('Could not insert data: {}'.format(format_exc()))
            return None
        logger.debug('Function insert_table end')

    def close(self):
        logger.debug('Function close start')

        try:
            self.conn.commit()

            # Close the connection
            self.conn.close()
            logger.info("DB conn closed")
            return True
        except Error as e:
            logger.error('Could not close itself: {}'.format(e))
            return False

        logger.debug('Function close end')
