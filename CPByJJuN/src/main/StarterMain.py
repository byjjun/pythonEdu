#-*- coding: utf-8 -*-

'''
Created on 2020. 9. 12.

@author: JJ
'''
import connect.ConnectCP as connect
import get.StockDatafromCP as StockDatafromCP


if __name__ == '__main__':
    pass

#CP연결 확인
connect.checkConnect()

kodex = StockDatafromCP.GetStockData('A122630',5)
kodex.getStockData()



