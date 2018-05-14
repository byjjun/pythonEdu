# -*- coding: utf-8 -*-


'''
Created on 2018. 5. 11.

@author: 073860
'''

import requests
from datetime import datetime

def getCurrentStockConsenFromHK():
    
    
    today_str = datetime.today().strftime('%Y-%m-%d')
       
    #request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate=2018-05-11&edate=2018-05-11&up_down_type=4&pagenum=150&order_type=&up_down_type=1#'
    request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+today_str+'&edate='+today_str+'&up_down_type=4&pagenum=150&order_type=&up_down_type=1#'
    #print request_url
    raw_data = requests.post(request_url).content
    print raw_data
    
    return raw_data

getCurrentStockConsenFromHK()

    
    
