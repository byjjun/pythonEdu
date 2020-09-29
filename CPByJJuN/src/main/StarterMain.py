#-*- coding: utf-8 -*-

'''
Created on 2020. 9. 12.

@author: JJ
'''
import connect.ConnectCP as connect
import get.StockDatafromCP as StockDatafromCP
from conf import ConfigConsts as CONF
from util import ToCSV


if __name__ == '__main__':
    pass

############################
''' 환경설정  시작 '''
############################
#CREON PLUS 연결 및 CSV파일 생성 여부 
#True = 생성 / False = 안생성
#############################
CONF.setmakeFile(True)
#############################
#종목코드 
#A122630 : KODEX레버리지
#############################
CONF.setStockCode("A122630")
############################
''' 환경설정  끝 '''
############################



if(CONF.getmakeFile()):
    #CP연결 확인
    print("Connect CREON PLUS")
    connect.checkConnect()
    #DATA가져와서 CSV 만들기
    print("MAKE CSV FIle")
    kodex = StockDatafromCP.GetStockData(CONF.stockcode,200)
    kodex.getStockDatatoCSV()
    print("MAKE CSV FIle END")
    print("MAKE CSV REVERSE")
    ToCSV.makeReversedCsvFile(CONF.stockcode)
    print("MAKE CSV REVERSE END")
    
    