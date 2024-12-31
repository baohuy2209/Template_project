from data_access_layer.UserDAL import UserDAL

user_dal = UserDAL()
user_dal.connect()
list_user = user_dal.printUserList()
for user in list_user:
    print(user.username, user.password, user.isResetPassword, user.isAdmin)
user = user_dal.login("baohuy", "123")
print(user)