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


earings_rate = 0.0

count=0

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
selling_point_rate = 7.0


class TestStrategy(bt.Strategy): # bt.Strategy를 상속한 class로 생성해야 함.
    
    
    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
    
    param = dict(
        
    )
    def __init__(self):
        print("AAA")
        
    def next(self):
        global count
        global change_market_type
        global market_status
        global buying_size
        global cash_separate_size
        global date_separate_size
        
        #earings_rate = fundvalue /prev_cash_value

        close_value = self.data.close[0] # 종가 값
        self.log("%%%%%%%%%%%%%%%%%%%%%%%%" +str(close_value) +"%%%%%%%%%%%%%%%%%"+ str(count))
        
        
        ##상승장
        if(market_status=="Bull"):
            ## 장종류가 변경되었을때 로깅용 - START
            if(change_market_type):
                self.log("####### Bull Market ##### : ")
                change_market_type=False
                market_status="Bull"
            ## 장종류가 변경되었을때 로깅용 - END
                    
            ## 한방에 구매할 양이 안정해졌을때       
            if(buying_size < 0):
                buying_size = int((self.broker.getcash() / close_value) / cash_separate_size)
                
            count=count+1
            
            if(count==date_separate_size):
                self.log(str(" ## Buy : "+ str(buying_size)))
                self.buy(size=buying_size)
                count=0
                
 
            #self.log(self.getposition(data=self.data, broker=self.broker).size)
            self.log(self.getposition(data=self.data, broker=self.broker))
            
            fund_everage_price=0.0
            buying_price=1
            
            ### 수익률 계산 -- 시작
            if(self.getposition(data=self.data, broker=self.broker).adjbase!=None):
                fund_everage_price=self.getposition(data=self.data, broker=self.broker).adjbase
            #self.log("FUND EVERAGE : " + str(fund_everage_price))
            
            if(self.getposition(data=self.data, broker=self.broker).price==0.0):
                buying_price=0.001
            else:
                buying_price=self.getposition(data=self.data, broker=self.broker).price
            ### 수익률 계산 -- 끝    
            
            
            self.log("CLOSE : " + str(close_value) + "$$$ BUYING : " + str(buying_price))
            fund_earing_rate= (float(float(fund_everage_price) / float(buying_price))-1.0)*100
            self.log("FUND EARNING RATE : " + str(fund_earing_rate))
            
            
            position_size=self.getposition(data=self.data, broker=self.broker).size
            
            if(int(position_size)>0):
                if(fund_earing_rate > selling_point_rate):
                    selling_size = position_size
                    self.log(str(" ## Sell : "+ str(selling_size)))
                    self.sell(size=selling_size)
                    count=(date_separate_size-1)
                
 
        
        ## 횡보장
        elif(market_status=="Sideway"):
            self.log("####### Sideway Market ##### : ")
        ## 하락장
        elif(market_status=="Bear"):
            self.log("####### Bear Market ##### : ")
        ## 모름장
        else:
            self.log("#######  Unknown Market ####### : ")
        
        
        now_value = ":: cash:", self.broker.getcash(), " :: fund:", self.broker.getvalue()
        self.log(now_value)
        
        
        
        #print("BBB")



cerebro = bt.Cerebro() # create a "Cerebro" engine instance


data = btfeed.GenericCSVData(
    
    dataname = "D:\\cpbyjjun\\data\\A122630.csv",
    
    fromdate = datetime.datetime(2016, 4, 30),
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
cerebro.broker.setcash(10000000.0) # 초기 자본 설정 500,000
cerebro.broker.setcommission(commission=0.003) # 매매 수수료는 0.3% 설정
cerebro.addstrategy(TestStrategy) # 자신만의 매매 전략 추가
cerebro.run() # 백테스팅 시작
cerebro.plot() # 그래프로 보여주기


