import pybithumb
import time
#잔고조회
con_key = ""
sec_key = ""

bithumb = pybithumb.Bithumb(con_key, sec_key)
for ticker in pybithumb.get_tickers():
     balance = bithumb.get_balance(ticker)
     print(ticker, ";", balance)
     time.sleep(0.1)