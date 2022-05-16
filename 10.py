import pybithumb
import time
#잔고조회
con_key = "00dd3f3ea679312eef4e746a80378360"
sec_key = "e4349eafad334167a3e46434aacad640"

bithumb = pybithumb.Bithumb(con_key, sec_key)
for ticker in pybithumb.get_tickers():
     balance = bithumb.get_balance(ticker)
     print(ticker, ";", balance)
     time.sleep(0.1)