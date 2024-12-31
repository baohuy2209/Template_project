class User:
    def __init__(self, username=None, password=None, isAdmin=None, isResetPassword=None):
        self.username = username
        self.password = password
        self.isAdmin = isAdmin
        self.isResetPassword = isResetPassword
    def __str__(self):
        info = f"{self.username}, {self.password}, {self.isResetPassword}, {self.isAdmin}"
        return info