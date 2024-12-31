from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.FormWindowExt import FormWindowExt

app = QApplication([])
ui = FormWindowExt()
ui.setupUi(QMainWindow())
ui.show()
app.exec()