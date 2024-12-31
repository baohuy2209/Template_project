from Models.User import User
from connector.Connector import Connector


class UserDAL(Connector):
    def printUserList(self):
        val_list = "select * from test"
        cursor = self.query(val_list)
        dataset = cursor.fetchall()
        users=[]
        for record in dataset:
            id = record[0]
            username = record[1]
            password = record[2]
            isResetPassword = record[3]
            isAdmin = record[4]
            user = User(username, password, isAdmin, isResetPassword)
            users.append(user)
        cursor.close()
        return users
    def login(self, username, password):
        sql_login="select * from test where username=%s and password=%s"
        value_input = (username,password)
        cursor = self.query(sql_login, value_input)
        data = cursor.fetchone()
        if data != None:
            id, username, password, isResetPassword, isAdmin = data
            user = User(username, password, isAdmin, isResetPassword)
        else:
            user = None
        cursor.close()
        return user