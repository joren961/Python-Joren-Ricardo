import sqlite3 as sql
from sqlite3 import Error
from datetime import datetime


class db:
    def __init__(self, db_file):
        conn = None
        try:
            conn = sql.connect(db_file)
            conn.execute(self.create_database())
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def create_database(self):
        return """ CREATE TABLE IF NOT EXISTS stats (
                                                id integer PRIMARY KEY,
                                                nickname text NOT NULL,
                                                cheat integer NOT NULL,
                                                play_date text NOT NULL,
                                                guesses integer NOT NULL
                                            ); """

    def getLeaderboard(self):
        try:
            sqlite_connection = sql.connect('mastermind.db')
            cursor = sqlite_connection.cursor()
            sqlite_select_query = """SELECT * from stats ORDER BY nickname"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            cursor.close()
            return self.groupByNickname(records)
        except sql.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    def groupByNickname(self, records):
        gamesDic = {}
        for index in range(0, len(records)):
            if records[index][1] in gamesDic:
                gamesDic[records[index][1]].append(records[index])
            else:
                gamesDic[records[index][1]] = []
                gamesDic[records[index][1]].append(records[index])

        return gamesDic

    def storeGame(self, nick_name, guess_amount, cheat_on):
        try:
            sqlite_connection = sql.connect('mastermind.db')
            cursor = sqlite_connection.cursor()

            sqlite_insert_with_param = """INSERT INTO stats
                                      (nickname,cheat,play_date,guesses) 
                                      VALUES (?, ?, ?, ?);"""

            parmameters = (nick_name, cheat_on, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), guess_amount)
            cursor.execute(sqlite_insert_with_param, parmameters)
            sqlite_connection.commit()
            cursor.close()
        except sql.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
