import pybithumb
import time     #예외처리는 중요하다. 네트워크 연결이 끊기거나 작성한 코드에 잠재적인 문제가 있어 예상치 못한 값이 변수에 바인딩될 수 있다.
#프로그램이 오작동해서 금전적 손실을 볼 수 있으니 예외처리는 중요. 특히, 자동매매 프로그램같은 경우는 24시간 돌리니 예외처리는 필수.
#예외 발생시 pybithumb 모듈은 None을 리턴한다.
while True:
    price = pybithumb.get_current_price("BTC")
    if price is not None:
        print(price/2)
        time.sleep(0.2)

#또는 while True:                                         try~else문을 이용하여 예외처리도 방법이다.
         #price = pybithumb.get_current_price("BTC")
         #try:
         #    print(price/2)
         #else:
         #   print("error",price)
         #time.sleep(0.2)