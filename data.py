import os
import sqlite3
from sqlite3 import Error
import logging
from traceback import format_exc
from datetime import datetime
from util.log import log_func, get_logger

logger = get_logger(__name__)


class Data:
    @log_func(logger)
    def __init__(self, db_path):

        self.db_name = db_path

        try:
            self.conn = sqlite3.connect(os.path.abspath(self.db_name))
        except Error as e:
            logger.critical(f'Cannot connect to db: {format_exc()}')

    @log_func(logger)
    def create_table(self):

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
        except Error as e:

            if isinstance(e, sqlite3.DatabaseError):
                # sqlite3 docs say ProgrammingError is raised when table exists, although OperationalError was raised
                # when testing.
                logger.critical(f'Error creating table:\n{format_exc()}')
                return False

            logger.warning(f'Exception raised while creating table:\n{format_exc()}')
            return True

    @log_func(logger)
    def insert(self, img_name):

        sql = ''' INSERT INTO sensor_data(time,img_name)
                VALUES(?,?) '''

        try:
            cur = self.conn.cursor()

            # Insert a row of data
            cur.execute(sql, (datetime.now(), img_name))

            self.conn.commit()

            logger.info(f'Inserted a row of data: id {cur.lastrowid}')

            return cur.lastrowid
        except Error as e:
            logger.critical(f'Could not insert data: {format_exc()}')
            return None

    @log_func(logger)
    def close(self):

        try:
            self.conn.commit()

            # Close the connection
            self.conn.close()
            logger.info("DB conn closed")
            return True
        except Error as e:
            logger.error(f'Could not close itself: {e}')
            return False
