#-*- coding: utf-8 -*-

'''
Created on 2020. 9. 11.

@author: JJ
'''
 
import win32com.client


class GetStockData:

    '''
    --주요 코드 --
    A122630 : KODEX레버리지
    '''
    
    def __init__(self, stockCode, dataAmount):
        self.stockCode = stockCode
        self.dataAmount = dataAmount
    
    def setStockCode(self, stockcode):
        self.stockCode = stockcode
        return True

    # 1dozen = 36days    
    def setDataAmount(self, dozen):
        self.dataAmount = dozen
        
    def __reqeustData(self, obj):
        # 데이터 요청
        obj.BlockRequest()
     
        # 통신 결과 확인
        rqStatus = obj.GetDibStatus()
        rqRet = obj.GetDibMsg1()
        #print("통신상태", rqStatus, rqRet)
        if rqStatus != 0:
            return False
     
        # 일자별 정보 데이터 처리
        count = obj.GetHeaderValue(1)  # 데이터 개수
        for i in range(count):
            date = obj.GetDataValue(0, i)  # 일자
            open = obj.GetDataValue(1, i)  # 시가
            high = obj.GetDataValue(2, i)  # 고가
            low = obj.GetDataValue(3, i)  # 저가
            close = obj.GetDataValue(4, i)  # 종가
            diff = obj.GetDataValue(5, i)  # 차이
            #vol = obj.GetDataValue(6, i)  # 거래량
            print(date, open, high, low, close, diff)
     
        return True
    
    
    def getStockData(self):
        
        objStockWeek = win32com.client.Dispatch("DsCbo1.StockWeek")
        objStockWeek.SetInputValue(0, self.stockCode)   #종목 코드 - 삼성전자
         
        # 최초 데이터 요청
        ret = self.__reqeustData(objStockWeek)
        
        # 연속 조회
        NextCount = 1
        while objStockWeek.Continue:  #연속 조회처리
            NextCount+=1;
            if (NextCount > self.dataAmount):
                break
            ret = self.__reqeustData(objStockWeek)
            if ret == False:
                exit()
        
        return True
    
     
