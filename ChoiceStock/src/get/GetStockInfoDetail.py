# -*- coding: utf-8 -*-

'''
Created on 2020. 5. 22.

@author: 073860
'''

from src.util import Preference

def getStockDeatilInfofromPaxnet(stock_code):
    
    
    stock_info = {}
    request_url = 'http://www.paxnet.co.kr/stock/analysis/presentValue?abbrSymbol='+stock_code   
    
    driver = Preference.getWebDriver()
    
    try:
                
        driver.get(request_url)    
        #시가총액
        stock_info_element = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[8]/td[1]')
        stock_info['total_cap']= stock_info_element.get_attribute('innerHTML')
        print stock_info['total_cap'] 
        
        #당일 거래량
        stock_info_element = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[4]/td[1]')
        stock_info['today_volume']= stock_info_element.get_attribute('innerHTML')
        print stock_info['today_volume']
        
        #전일 거래량
        stock_info_element = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[8]/td[2]')
        stock_info['yesterday_volume']= stock_info_element.get_attribute('innerHTML')
        print stock_info['yesterday_volume'] 
        
        #거래량전일대비
        volume_ratio =  float(stock_info['today_volume'].replace(',',''))/float(stock_info['yesterday_volume'].replace(',',''))
        volume_ratio = int(volume_ratio*100)
        stock_info['volume_ratio']=str(volume_ratio)
        print stock_info['volume_ratio']
                
        #PER
        stock_info_element = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[12]/td[2]')
        stock_info['PER']= stock_info_element.get_attribute('innerHTML')
        print stock_info['PER'] 
        
        #PBR
        stock_info_element = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[13]/td[2]')
        stock_info['PBR']= stock_info_element.get_attribute('innerHTML')
        print stock_info['PBR'] 
            
    
    except Exception as e:
        print(e)
            
    return stock_info
    


#getStockDeatilInfofromPaxnet('228760')
