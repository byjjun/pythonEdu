#-*- coding: utf-8 -*-
'''
Created on 2020. 9. 19.

@author: JJ
'''

import datetime
import backtrader as bt
import backtrader.feeds as btfeed
from dask import sizeof

'''
#SAMPLE
class SmaCross(bt.Strategy): # bt.Strategy를 상속한 class로 생성해야 함.
    params = dict(
        pfast=5, # period for the fast moving average
        pslow=30 # period for the slow moving average
    )
    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast) # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow) # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2) # crossover signal
    def next(self):
        
        print(self.broker.getvalue())
        if not self.position: # not in the market
            if self.crossover > 0: # if fast crosses slow to the upside
                close = self.data.close[0] # 종가 값
                size = int(self.broker.getcash() / close) # 최대 구매 가능 개수
                self.buy(size=size) # 매수 size = 구매 개수 설정
                
        elif self.crossover < 0: # in the market & cross to the downside
            self.close() # 매도
'''
'''
#수익률
earings_rate = 0.0
#매수한지 몇일 지났는지 확인
buying_period=0
# 장종류
market_status="Bull" ##Bull/Bear/Sideway
# 장 종류가 변할 때 로깅용
change_market_type=True

#한번에 몇개 살꺼냐
buying_size=-1
#몇등분 할꺼냐
cash_separate_size=20
#몇일에 한번 살꺼냐(임시)
date_separate_size=20
#몇프로 수익나면 팔꺼냐
selling_point_rate = 5.0

# 최초금액
start_value = 0.0
# 최종 금액
result_value = 0.0
'''

'''
프로그램 CONF - 손대지 말것 - START
'''
# 최종 금액(프로그램 입력)
result_value = 0.0
#수익률(프로그램 입력)
earings_rate = 0.0
#매수한지 몇일 지났는지 확인(프로그램 입력)
buying_period=0
# 장종류(프로그램 입력)
market_status="Bull" ##Bull/Bear/Sideway
# 장 종류가 변할 때 로깅용(프로그램 입력)
change_market_type=True

'''
프로그램 CONF - 손대지 말것 - END
'''


def printResult():
    global start_value
    global result_value
    global date_separate_size
    global cash_separate_size
    global selling_point_rate
    
    print(str(date_separate_size) +"일에 1회씩 " + str(cash_separate_size) + "등분 해서 " + str(selling_point_rate) + "% 수익 나면  매도")
    print("[ 시작 금액 : " + str(start_value) + " // 최종 금액 : " + str(result_value) + " // 수익률 : " + str(round(float(((result_value/start_value)-1.0)*100),2)) +"% ]")


class TestStrategy(bt.Strategy): # bt.Strategy를 상속한 class로 생성해야 함.
    
        
    def infoLog(self, txt):
        print(txt)
    
    def log(self, txt, dt=None):
        global debug_mode    
        dt = dt or self.datas[0].datetime.date(0)
        if(debug_mode):
            print('%s, %s' % (dt.isoformat(), txt))
    
    param = dict(    
    )
    
    def __destroy__(self):
        self.printResult()
    
    def __init__(self):
        global buying_period
        global buying_size
        global cash_separate_size
        global date_separate_size
        
        self.infoLog("===========================================================" )
        
        
    def next(self):
        global buying_period
        global change_market_type
        global market_status
        global buying_size
        global cash_separate_size
        global date_separate_size
        
        #earings_rate = fundvalue /prev_cash_value
        close_value = self.data.close[0] # 종가 값
        
        ##상승장
        if(market_status=="Bull"):
            
            #하루 +1
            buying_period=buying_period+1
            
            ## 장종류가 변경되었을때 로깅용 - START
            if(change_market_type):
                self.log("####### Bull Market ##### : ")
                change_market_type=False
                market_status="Bull"
            ## 장종류가 변경되었을때 로깅용 - END
            
            ''' 펀드 잔고 확인 '''    
            #self.log(self.getposition(data=self.data, broker=self.broker))
            ''' 펀드 잔고 확인 '''
            position_size=self.getposition(data=self.data, broker=self.broker).size
                    
            ## 한번 구매용 size       
            if(buying_size < 0):
                buying_size = int((self.broker.getcash() / close_value) / cash_separate_size)
            
            
            ## 매수 날이 들어오면 매수
            if(buying_period==date_separate_size):
                self.buy(size=buying_size)
                self.log(str(" ## Buy : "+ str(buying_size)))
                buying_period=0
             
            
            
            #펀드 잔고가 있을 때
            if(int(position_size)>0):
            
                ### 수익률 계산 -- 시작
                if(self.getposition(data=self.data, broker=self.broker).adjbase!=None):
                    fund_everage_price=self.getposition(data=self.data, broker=self.broker).adjbase
                #self.log("FUND EVERAGE : " + str(fund_everage_price))
                buying_price=self.getposition(data=self.data, broker=self.broker).price
                fund_earing_rate= (float(float(fund_everage_price) / float(buying_price))-1.0)*100
                ### 수익률 계산 -- 끝    
                                
                self.log("종가 : " + str(close_value) + " @@ 펀드 단가 : " + str(buying_price) + " / 수량 : " +str(position_size)+ " / 수익률 " + str(round(fund_earing_rate,2)) + "%" )
                
                #selling point 이상 수익이 났을때 전체 매도
                if(fund_earing_rate > selling_point_rate):
                    selling_size = position_size
                    self.log(str(" ## Sell : "+ str(selling_size)))
                    self.sell(size=selling_size)
                    #다팔고 다음날 다시 매수
                    buying_period=(date_separate_size-1)
                    #한방에 살 수량 다시계산
                    buying_size=-1
 
        
        ## 횡보장
        elif(market_status=="Sideway"):
            self.log("####### Sideway Market ##### : ")
        ## 하락장
        elif(market_status=="Bear"):
            self.log("####### Bear Market ##### : ")
        ## 모름장
        else:
            self.log("#######  Unknown Market ####### : ")
        
        
        now_value = "보유현금 :" + str(self.broker.getcash()) + " :: 평가금액 :" + str(self.broker.getvalue())
        self.log(now_value)
        
        
        
        global result_value
        result_value = self.broker.getvalue()
        
        
        #print("BBB")


'''
환경세팅 - START
'''
#한번에 몇개 살꺼냐
buying_size=-1
#몇등분 할꺼냐
cash_separate_size=20
#몇일에 한번 살꺼냐(임시)
date_separate_size=10
#몇프로 수익나면 팔꺼냐
selling_point_rate = 6.5
# 최초금액
start_value = 10000000.0
# 일일 Debug모드
debug_mode=True
'''
환경세팅 - END
'''


cerebro = bt.Cerebro() # create a "Cerebro" engine instance

data = btfeed.GenericCSVData(
    
    dataname = "D:\\cpbyjjun\\data\\A122630.csv",    
    fromdate = datetime.datetime(2010, 3, 1),
    todate = datetime.datetime(2020, 9, 15),
    nullvalue=0.0,
    dtformat=('%Y%m%d'),
    datetime=0,
    open=1,
    high=2,
    low=3,
    close=4,
    volume=6,
    openinterest=-1
)


cerebro.adddata(data)

cerebro.broker.setcash(start_value) # 초기 자본 설정 500,000
cerebro.broker.setcommission(commission=0.003) # 매매 수수료는 0.3% 설정
cerebro.addstrategy(TestStrategy) # 자신만의 매매 전략 추가
cerebro.run() # 백테스팅 시작
cerebro.plot() # 그래프로 보여주기

printResult()


