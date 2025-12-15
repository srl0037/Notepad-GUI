import sys

from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
from mainwindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()
app.exec()