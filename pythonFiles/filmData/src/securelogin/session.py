import pymysql

"""
CurrentSession class manages the current state. Which User is logged in
and whether they are ADMIN (and hence have access to certain privileges)
Encapsulated code inside this class and this file for functions for
extra security.
"""

class CurrentSession:

    def __init__(self):
        self.user_profile = None
        self.conn = None
        self.cursor = None

    def get_user(self):
        return self.user_profile

    def get_cursor(self):
        return self.cursor

    def set_user(self, user_profile):
        self.user_profile = user_profile

    def open_conn(self):
        self.conn = pymysql.connect(host="localhost", user="root",
                                    password="Founders72!", database="record_boxes")
        self.cursor = self.conn.cursor()

    def close_conn(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def print_results(self):
        results = (self.cursor.fetchall())
        for row in results:
            print(row)
        if not results :
            print("No matching films found!")