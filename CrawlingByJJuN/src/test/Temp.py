'''
Created on 2017. 12. 21.

@author: 073860
'''
import datetime

def getPreStockConsenFromHK():
    
    stock_pre_consen = {}
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(1)
    pre_2month = today - datetime.timedelta(60)
    
    print yesterday.strftime('%Y-%m-%d')
    print pre_2month.strftime('%Y-%m-%d')
    
    
    return stock_pre_consen

#getPreStockConsenFromHK()