# -*- coding: utf-8 -*-

'''
Created on 2020. 5. 22.

@author: 073860
'''

from src.util import Preference

def getStockDeatilInfofromPaxnet(stock_code):
    
    
    stock_info = {}
    request_url = 'http://www.paxnet.co.kr/stock/analysis/presentValue?abbrSymbol='+stock_code   
    
    print request_url 
    
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
        
        #전일 거래량 -> 5일평균으로 변경
        #stock_info_element = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[8]/td[2]')
        #stock_info['everage_5day_volume']= stock_info_element.get_attribute('innerHTML')
        #print stock_info['everage_5day_volume'] 
        
        # 5일평균 거래량
        volume_bf_days_element = driver.find_element_by_xpath('//*[@id="viewHtml2"]/tr[1]/td[8]')
        volume_bf_1day = float(volume_bf_days_element.get_attribute('innerHTML').replace(',',''))
        
        volume_bf_days_element = driver.find_element_by_xpath('//*[@id="viewHtml2"]/tr[2]/td[8]')
        volume_bf_2day = float(volume_bf_days_element.get_attribute('innerHTML').replace(',',''))
        
        volume_bf_days_element = driver.find_element_by_xpath('//*[@id="viewHtml2"]/tr[3]/td[8]')
        volume_bf_3day = float(volume_bf_days_element.get_attribute('innerHTML').replace(',',''))
        
        volume_bf_days_element = driver.find_element_by_xpath('//*[@id="viewHtml2"]/tr[4]/td[8]')
        volume_bf_4day = float(volume_bf_days_element.get_attribute('innerHTML').replace(',',''))
        
        volume_bf_days_element = driver.find_element_by_xpath('//*[@id="viewHtml2"]/tr[5]/td[8]')
        volume_bf_5day = float(volume_bf_days_element.get_attribute('innerHTML').replace(',',''))
        
        everage_5day_volume = float((volume_bf_1day+volume_bf_2day+volume_bf_3day+volume_bf_4day+volume_bf_5day)/5)
        
        
        #거래량 5일평균 대비
        volume_ratio =  float(stock_info['today_volume'].replace(',',''))/everage_5day_volume
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
