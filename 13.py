#주문취소
import pybithumb
import time
con_key = "00dd3f3ea679312eef4e746a80378360"
sec_key = "e4349eafad334167a3e46434aacad640"
bithumb = pybithumb.Bithumb(con_key, sec_key)
order = bithumb.buy_limit_order()#큰 따옴표 안의 티거, 가격, 수량 차례로 입력.
print(order)

time.sleep(10)
cancel = bithumb.cancel_order(order)
print(cancel)
#정상적으로 취소가 잘 되면 True가 출력되고, 주문 취소가 실패하면 None이 출력됨.