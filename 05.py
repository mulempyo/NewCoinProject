import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):  #사용자 시그널을 정의하기 위해 MySiganl클래스를 정의함.
    signal1 = pyqtSignal()#클래스 변수로 pyqtSignal 클래스의 객체를 생성합니다.
    signal2 = pyqtSignal(int,int)

    def run(self):
        self.signal1.emit() #emit 메소드를 호출하여 시그널을 발생시킵니다.
        self.signal2.emit(1,2)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysingnal = MySignal()
        mysingnal.signal1.connect(self.signal1_emitted) #사용자 정의 시그널과 이를 처리하는 메소드를 연결합니다.
        mysingnal.signal2.connect(self.signal2_emitted)
        mysingnal.run()

    @pyqtSlot()
    def signal1_emitted(self): #사용자 정의 시그널이 방출될 때 호출되는 메소드를 정의합니다.
        print("signal1 emitted")

    @pyqtSlot(int,int)
    def signal2_emitted(self, arg1, arg2):
        print("signal2 emitted", arg1, arg2)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()