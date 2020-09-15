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

''' 
CREON PLUS 연결 및 CSV파일 생성 
True = 생성
False = 안생성
'''
CONF.setmakeFile(True)
CONF.setStockCode("A122630")

if(CONF.getmakeFile()):
    #CP연결 확인
    print("Connect CREON PLUS")
    connect.checkConnect()
    #DATA가져와서 CSV 만들기
    print("MAKE CSV FIle")
    ToCSV.clearCsvFile(CONF.stockcode)
    kodex = StockDatafromCP.GetStockData(CONF.stockcode,30)
    kodex.getStockData()
    print("MAKE CSV FIle END")

