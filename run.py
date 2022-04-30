import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,200,300,200)
        self.setWindowTitle("PyQT")
        self.setWindowIcon(QIcon("icon.png"))

        btn = QPushButton("버튼 1", self)
        btn.move(10,10)
        btn.clicked.connect(self.btn_clicked)
    def btn_clicked(self):
        print("버튼 클릭")
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_() #이벤트 루프 생성