#!/usr/bin/python
from PyQt5.QtCore    import Qt, QSize, QTimer
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QWidget,
                            QPushButton, QGridLayout, QSpacerItem,
                            QSizePolicy, QLabel, QApplication)
import sys


class Blueprint():

    @staticmethod
    def run():
       app = QApplication(sys.argv)
       w = Dialog()
       w.exec_()
       QTimer.singleShot(200, app.quit)
       sys.exit(app.exec_())
    

class Dialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setObjectName('Custom_Dialog')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(Stylesheet)

        self.initUi()

    def initUi(self):
        # Important: this widget is used as background and rounded corners.
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        layout = QVBoxLayout(self)
        layout.addWidget(self.widget)

        # Add user interface to widget
        layout = QGridLayout(self.widget)
        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 0)
        layout.addWidget(QPushButton(
            'r', self, clicked=self.accept, objectName='closeButton'), 0, 1)
        layout.addWidget(QLabel("<h2 style='color:#db00a5;'>Hello, world!</h2>"), 2, 0, 5, 2, alignment=Qt.AlignCenter)                           

    def sizeHint(self):
        return QSize(480, 800)       

Stylesheet = """
#Custom_Widget {
    background: #212324;
    border-radius: 2px;
    opacity: 100;
    border: 2px solid #db00a5;                   
}
#closeButton {
    min-width: 36px;
    min-height: 36px;
    font-family: "Webdings";
    qproperty-text: "r";
    border-radius: 10px;
}
#closeButton:hover {
    color: #ccc;
    background: #db00a5;
}
"""
