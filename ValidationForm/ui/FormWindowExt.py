from PyQt6.QtWidgets import QMainWindow

from Models.User import User
from data_access_layer.UserDAL import UserDAL
from ui.FormWindow import Ui_MainWindow
from ui.MainWindowExt import MainWindowExt


class FormWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.sub_mainwindow = None
        self.setupSignAndSlots()
    def setupSignAndSlots(self):
        self.pushButton.clicked.connect(self.login)
    def login(self):
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()
        if username == '':
            self.labelError.setText("username empty !!!")
        if password == '':
            self.labelError.setText("password empty !!!")
        user_dal = UserDAL()
        user_dal.connect()
        users = user_dal.printUserList()
        print(users)
    def show(self):
        self.MainWindow.show()
