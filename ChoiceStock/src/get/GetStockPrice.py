# -*- coding: utf-8 -*-

'''
Created on 2020. 5. 21.

@author: 073860
'''

from src.util import Preference

'''
현재가를 네이버에서 들고오는걸로 변경(지금버전 2020.5.20)
'''
def getCurrentStockPriceNaver(stock_code):
    
    stock_price = {}
    if stock_code == '130960':
        stock_code = '035760'
    
    
    request_url = 'https://finance.naver.com/item/main.nhn?code='+stock_code
    driver = Preference.getWebDriver()
    
    try:
        
        
        driver.get(request_url)
        #print request_url + "aaa"
        
        stock_price_info_element = driver.find_element_by_xpath('//*[@id="middle"]/dl/dd[4]')
        stock_price_info = stock_price_info_element.get_attribute('innerHTML')
        #print stock_price_info
                
        stock_price_info_array = stock_price_info.split(' ')
        
        #print stock_price_info_array[1]
        #print stock_price_info_array[5]
        #print stock_price_info_array[6]
        
        #stock_updown_rate = driver.find_element_by_xpath('//*[@id="disArr[0]"]/span')
        #print stock_updown_rate.text
        plusminus = stock_price_info_array[5]
        
        if(plusminus == u'플러스'):
            plusminus = u'+'
            #print '+'
        elif(plusminus == u'마이너스'):
            plusminus = u'-'
            #print '-'
                
        stock_price['now_price'] = stock_price_info_array[1].encode('utf-8')
        stock_price['updown_rate'] = plusminus.encode('utf-8')+stock_price_info_array[6].encode('utf-8')+u'%'.encode('utf-8')
    
    except Exception as e:
        print(e)
        stock_price['now_price'] = "0"
        stock_price['updown_rate'] = "0"
    
    #print stock_code
    #print stock_now_price.text
    #print stock_updown_rate.text
    
    #print stock_now_price.text+' ('+stock_updown_rate+')'
            
    return stock_price

