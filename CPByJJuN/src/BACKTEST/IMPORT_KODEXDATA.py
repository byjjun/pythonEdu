#-*- coding: utf-8 -*-

'''
Created on 2017. 12. 12.

@author: 073860
'''
import win32com.client
from boto.ec2 import buyreservation
 
all_kodex_price_list = []
# date, open, high, low, close, diff, vol
my_account = []
# stock_count, stock_price, cash, amount,
fee=0.0005
one_buy_amount=100000
sell_ratio=0.03

def init_set_invest():
    my_account['date'] = 20100222
    my_account['stock_count']=0
    my_account['stock_original_price']=0
    my_account['stock_price']=0
    my_account['cash']=20000000 
    #투자금 2000만원
    my_account['amount']=20000000

def check_buy_sell(kodexprice):
    check_profit_rate = (my_account['stock_oroginal_price']/(kodexprice['high']*0.98))
    if ( check_profit_rate > sell_ratio):
        return 'sell'
    else:
        return 'buy'
    
def buy_stock():
    a = ''
    
def sell_stock():    
    a = ''
 
def ReqeustData(obj):
    # 데이터 요청
    obj.BlockRequest()
 
    # 통신 결과 확인
    rqStatus = obj.GetDibStatus()
    #rqRet = obj.GetDibMsg1()
    #print("통신상태", rqStatus, rqRet)
    if rqStatus != 0:
        return False
 
    kodex_price = []
    # 일자별 정보 데이터 처리
    count = obj.GetHeaderValue(1)  # 데이터 개수
    for i in range(count):
        date = obj.GetDataValue(0, i)  # 일자
        kodex_price['date']=date
        open = obj.GetDataValue(1, i)  # 시가
        kodex_price['open']=open
        high = obj.GetDataValue(2, i)  # 고가
        kodex_price['high']=high
        low = obj.GetDataValue(3, i)  # 저가
        kodex_price['low']=low
        close = obj.GetDataValue(4, i)  # 종가
        kodex_price['close']=close
        diff = obj.GetDataValue(5, i)  # 등락
        kodex_price['diff']=diff
        vol = obj.GetDataValue(6, i)  # 거래량
        kodex_price['vol']=diff
        all_kodex_price_list.add(kodex_price)
        #print(date, open, high, low, close, diff, vol) 
    return True
 
# 연결 여부 체크
objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("PLUS Not Connected. ")
    exit()
  
# 일자별 object 구하기
objStockWeek = win32com.client.Dispatch("DsCbo1.StockWeek")
objStockWeek.SetInputValue(0, 'A122630')   #종목 코드 - KODEX 레버리지
 
# 최초 데이터 요청
ret = ReqeustData(objStockWeek)
if ret == False:
    exit()

# 연속 데이터 요청
# 예제는 5번만 연속 통신 하도록 함.
NextCount = 1
while objStockWeek.Continue:  #연속 조회처리
    NextCount+=1;
    if (NextCount > 100):
        break
    ret = ReqeustData(objStockWeek)
    if ret == False:
        exit()


