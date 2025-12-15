from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton, QVBoxLayout
from PySide6.QtCore import QSize

class TextEdit (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Edit")

        self.text_edit = QTextEdit()
        self.text_edit.setMinimumSize(500,400)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)
