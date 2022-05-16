import pybithumb
# 지정가 매수
con_key = "00dd3f3ea679312eef4e746a80378360"
sec_key = "e4349eafad334167a3e46434aacad640"
bithumb = pybithumb.Bithumb(con_key, sec_key)
order = bithumb.buy_limit_order() #여기에 가상화폐 티거, 가격(호가단위 파악먼저), 수량 차례로 입력하면 됨. 티거는 큰 따옴표 안에다가.
#입력하는 것 주의. 입력 즉시 체결됨.
print(order)
#책에 최우선 매도호가에 거래되는 시장가 매수 코드도 있다. 실행하지는 말자.p.256부터



