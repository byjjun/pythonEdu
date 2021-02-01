# -*- coding: utf-8 -*-

'''
Created on 2020. 5. 22.

@author: 073860
'''

from src.util import Preference
from datetime import date, timedelta
from bs4 import BeautifulSoup

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
        #stock_info_element = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[12]/td[1]')
        stock_info_element = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[12]/td[1]')
        stock_info['PER']= stock_info_element.get_attribute('innerHTML')
        stock_info['PER']=stock_info['PER'].replace(u'\ubc30','')
        stock_info['PER']=stock_info['PER'].replace(' ','')
        print stock_info['PER']
        
        #PBR
        #stock_info_element = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[13]/td[2]')
        stock_info_element = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[13]/td[1]')
        stock_info['PBR']= stock_info_element.get_attribute('innerHTML')
        stock_info['PBR']=stock_info['PBR'].replace(u'\ubc30','')
        stock_info['PBR']=stock_info['PBR'].replace(' ','')
        print stock_info['PBR']
        
        good_count = 0
        bad_count = 0
        
        good_count, bad_count = getStockGoodBadfromHK(stock_code)
        stock_info['GOOD']=str(good_count)
        stock_info['BAD']=str(bad_count)
    
    except Exception as e:
        print(e)
            
    return stock_info
    

def getStockGoodBadfromHK(stock_code):
    
    count_good = 0
    count_bad = 0
    
    try:
        
        driver = Preference.getWebDriver()
        
        today = date.today()
        pre_1month = today - timedelta(30)
        
        today_str = today.strftime('%Y-%m-%d')
        pre_1month_str = pre_1month.strftime('%Y-%m-%d')
                
        #목표상향 갯수 추출
        request_url = 'http://consensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&search_text='+stock_code+'&sdate='+pre_1month_str+'&edate='+today_str
        #print request_url
        
        driver.get(request_url)        
        table_element = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/tbody')
        tablebody_html = table_element.get_attribute('innerHTML')
        
        soup = BeautifulSoup(tablebody_html, "html.parser")
        stock_element_list = soup.find_all('tr')
        
        for stock_element in stock_element_list:
            result_msg = stock_element.find('td').text
            #print result_msg
            #if(result_msg.find("결과가".decode('UTF-8'))):
            if "결과가".decode('UTF-8') in result_msg:
                print "None"
            else:
                count_good=count_good+1        
        #목표하향 갯수 추출
        request_url = 'http://consensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_bad&search_text='+stock_code+'&sdate='+pre_1month_str+'&edate='+today_str
        #print request_url
        
        driver.get(request_url)        
        table_element = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/tbody')
        tablebody_html = table_element.get_attribute('innerHTML')
        
        soup = BeautifulSoup(tablebody_html, "html.parser")
        stock_element_list = soup.find_all('tr')
        
        for stock_element in stock_element_list:
            result_msg = stock_element.find('td').text
            #print result_msg
            #if(result_msg.find("결과가".decode('UTF-8'))):
            if "결과가".decode('UTF-8') in result_msg:
                print "None"
            else:
                count_bad=count_bad+1
        
    except Exception as e:
        print(e)        

    return count_good, count_bad

#getStockDeatilInfofromPaxnet('228760')
