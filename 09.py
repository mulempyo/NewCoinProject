import sys
import pybithumb
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time
#버벅대는 현상은 파이썬 인터프리터가 현재가를 조회하고 화면에 GUI를 그리는 두가지 일을 순차적으로 실행하기 때문에 발생.
tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("coin_up_down_info.ui")[0] #uic모듈을 이용하면 Qt Designer로 만든 것을 파이썬 코드로 불러올 수 있다.
#Qt Designer로 만든 걸 이용하고 싶으면 현재 프로젝트에 Qt Designer결과물을 저장하는걸 잊지 마라.

class Worker(QThread):
    finished = pyqtSignal(dict)
    def run(self):
        while True:
            data = {}

            for ticker in tickers:
                data[ticker] = self.get_market_infos(ticker)
            self.finished.emit(data)
            time.sleep(2)
    def get_market_infos(self, ticker):
        try:
            df = pybithumb.get_ohlcv(ticker)
            ma5 = df['close'].rolling(window=5).mean()
            last_ma5 = ma5[-2]
            price = pybithumb.get_current_price(ticker)

            state = None
            if price > last_ma5:
                state = "상승장"
            else:
                state = "하락장"
            return price, last_ma5, state
        except:
            return None, None, None

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.worker = Worker()
        self.worker.finished.connect(self.update_table_widget)
        self.worker.start()



    @pyqtSlot(dict)
    def update_table_widget(self, data):
        try:
            for ticker, infos in data.items():
                index = tickers.index(ticker)

                self.tableWidget.setItem(index, 0, QTableWidgetItem(ticker))
                self.tableWidget.setItem(index, 1, QTableWidgetItem(str(infos[0])))
                self.tableWidget.setItem(index, 2, QTableWidgetItem(str(infos[1])))
                self.tableWidget.setItem(index, 3, QTableWidgetItem(str(infos[2])))
        except:
            pass
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()