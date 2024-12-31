import traceback

import mysql.connector
from mysql.connector import Error
class Connector:
    def __init__(self):
        self.server = "localhost"
        self.port = 3306
        self.database = "sap"
        self.username = "root"
        self.password = "Huy_22092005"
    def connect(self, server=None, port=None,database=None, username=None, password=None):
        try:
            if server != None:
                self.server = server
                self.port = port
                self.database = database
                self.username = username
                self.password = password
            self.conn = mysql.connector.connect(host=self.server, port=self.port, database = self.database, user=self.username, password=self.password)
            print("Connect successfully !!!")
        except Error as e:
            traceback.print_exc()
            print(e)
    def query(self,sql, val_input=None):
        cursor = self.conn.cursor()
        cursor.execute(sql, val_input)
        return cursor