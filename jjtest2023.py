import time
import pyupbit
import datetime

access = "zA7lfQBqPiq8KVnh0YOhZwAUGULatAW2VyDpnstV"          # 본인 값으로 변경
secret = "1aEidxtYBI7a5W44IbAD7rjxckk47YwwTKMw0l5N"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


accesss = "SvQxLejA9kwM209gg4LZHkvjcB29UrrOjNEyLErq"          # 본인 값으로 변경
secrett = "BmiiIiO0hzZtO4tqLkdgogs7tC0GWiHlFM15v9U5"          # 본인 값으로 변경
upbitt = pyupbit.Upbit(accesss, secrett)


print(upbit.get_balance("KRW"))
print(upbit.get_balance("XRP"))
print(upbitt.get_balance("ETH"))
print(pyupbit.get_current_price("KRW-XRP"))
print(pyupbit.get_current_price("KRW-XRP") - 20)
print(pyupbit.get_current_price("KRW-ETH"))
print(pyupbit.get_current_price("KRW-ETH") - 30000)

while True:
    try:
        
        if 4900000 < upbit.get_balance("KRW"):            
            current_price = pyupbit.get_current_price("KRW-XRP")
            target_price = pyupbit.get_current_price("KRW-XRP") - 20
            upbit.buy_limit_order("KRW-XRP", target_price, 20000/target_price)
            print(20000/target_price)
        elif 4720 < upbit.get_balance("XRP"): 
                current_price = pyupbit.get_current_price("KRW-XRP")
                target_price1 = pyupbit.get_current_price("KRW-XRP") + 20
                upbit.sell_limit_order("KRW-XRP",current_price + 10, 20000/current_price)
                print(current_price+20)
                print(20000/current_price)
        elif 1510000 < upbitt.get_balance("KRW"):            
            current_pricee = pyupbit.get_current_price("KRW-ETH")
            target_pricee = pyupbit.get_current_price("KRW-ETH") - 30000
            upbitt.buy_limit_order("KRW-ETH", target_pricee, 60000/target_pricee)
            print(target_pricee,upbitt.get_balance("KRW"))
            print(60000/target_pricee)
        elif 0.012 < upbitt.get_balance("ETH"): 
                current_pricee = pyupbit.get_current_price("KRW-ETH")                
                upbitt.sell_limit_order("KRW-ETH",current_pricee + 30000, 60000/current_pricee)
              
    except Exception as e:
        print(e)
        time.sleep(1)
