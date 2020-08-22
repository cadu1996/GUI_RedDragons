from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi

import sys



class GUI_main(QMainWindow):
    def __init__(self):
        super(GUI_main, self).__init__()
        loadUi('interface/main.ui', self)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        
        # add class in stack
        self.stackedWidget.addWidget(GUI_home())

        # execute button
        self.btn_close.clicked.connect(self.close)
        self.QT_btHome.clicked.connect(self.home)
        
        self.clicked = False

      
        
        self.show()

       

    # moousePressEvent, mouseMoveEvent, move the window.
    def mousePressEvent(self, ev):
        self.old_pos = ev.screenPos()
    
    def mouseMoveEvent(self, ev):
        if self.clicked:
            dx = self.old_pos.x() - ev.screenPos().x()
            dy = self.old_pos.y() - ev.screenPos().y()
            self.move(self.pos().x() - dx, self.pos().y() - dy)
        self.old_pos = ev.screenPos()
        self.clicked = True
        return QWidget.mouseMoveEvent(self, ev)

    def home(self):
        self.label_aba.setText("Home")
        self.stackedWidget.setCurrentIndex(0)
    


# repeat class for others stacks.
class GUI_home(QMainWindow):
    def __init__(self):
        super(GUI_home, self).__init__()
        loadUi('interface/home.ui', self)
        self.show()
        


app = QApplication(sys.argv)
window = GUI_main()
app.exec_()
