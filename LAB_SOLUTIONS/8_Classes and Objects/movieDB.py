#! /usr/bin/python
# Author: QA2.0 LIVE, V1.0
# Description: This module defines a class called MovieDB for creating objects
# that can interact with a SQLite3 database file.
"""
    MovieDB class.
"""
import sqlite3

class MovieDB:
    # Class variable storing location of DB
    DB_LOC = "C:\labs\wmovie_db.sqlite"

    def __init__(self):
        try:
            self.__db_conn = sqlite3.connect(DB_LOC)
            self.cur = self.__db_conn.cursor()
        except Exception as err:
            raise ValueError
        # No return as not explicitly called.


    def create_table(self, table_name="movies"):
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS movies
                    ( id        INTEGER PRIMARY KEY
                    ,title      VARCHAR(30)                  
                    ,year       VARCHAR(30)
                    ) """)
        return None

    def commit(self):
        """ Commit changes to database """
        self.__db_conn.commit()
        return None

    def __del__(self):
        """ Close connection automatically when object is deleted """
        self.__db_conn.close()
        return None