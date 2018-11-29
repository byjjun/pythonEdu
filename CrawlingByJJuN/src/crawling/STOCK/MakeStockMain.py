'''
Created on 2018. 5. 25.

@author: 073860
'''

from STOCK import GetHKConsenStockPrice

if __name__ == '__main__':
    pass

def getStockConsenStockMain():
    
    stock_dic_list = GetHKConsenStockPrice.getCurrentStockConsenFromHK()
    stock_dic_list_sorted = sorted(stock_dic_list, key=lambda k: float(k['upper_rate']), reverse=True)
    #stock_dic_list_sorted = sorted(stock_dic_list, key=lambda k: k['stock_code'], reverse=True)
    #print GetHKConsenStockPrice.makeSTOCKHtml(stock_dic_list_sorted)
    return GetHKConsenStockPrice.makeSTOCKHtml(stock_dic_list_sorted)

