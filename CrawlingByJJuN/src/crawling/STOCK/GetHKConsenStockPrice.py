# -*- coding: utf-8 -*-


'''
Created on 2018. 5. 11.

@author: 073860
'''

import requests
from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup


def getCurrentStockPriceDAUM(stock_code):
    
    request_url = 'http://finance.daum.net/item/main.daum?code='+stock_code
    #print request_url
    
    driver = webdriver.PhantomJS(phantomjs)
    driver.get(request_url)
    
    stock_now_price = driver.find_element_by_xpath('//*[@id="topWrap"]/div[1]/ul[2]/li[1]/em')
    stock_updown_rate = driver.find_element_by_xpath('//*[@id="topWrap"]/div[1]/ul[2]/li[3]/span')
    
    #print stock_code
    #print stock_now_price.text
    #print stock_updown_rate.text
    
    #print stock_now_price.text+' ('+stock_updown_rate+')'
    return stock_now_price.text+' ('+stock_updown_rate.text+')'

def getCurrentStockConsenFromHK():
    
    #한경 컨세서스 연결.
    #
    stock_dic_list = []
    
    today_str = datetime.today().strftime('%Y-%m-%d')
    #request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate=2018-05-08&edate=2018-05-08&up_down_type=1&pagenum=150&order_type=&now_page=1&order_type=10010000'
    request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+today_str+'&edate='+today_str+'&up_down_type=1&pagenum=150&order_type=&now_page=1&order_type=10010000'
    
    driver = webdriver.PhantomJS(phantomjs)
    driver.get(request_url)
    #html = driver.page_source
    table_element = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/tbody')
    tablebody_html = table_element.get_attribute('innerHTML')
    #print tablebody_html
    
    soup = BeautifulSoup(tablebody_html, "html.parser")
    
    stock_element_list = soup.find_all('tr')
    
    for stock_element in stock_element_list:
        
        #DATE
        upload_date=stock_element.td.string
        stock_data = stock_element.find_all('td')
        stock_dic ={}
        i = 1
        for astock_data in stock_data:
            if(i==1):
                #print astock_data.text
                stock_dic['update_date']=astock_data.text
            if(i==2):                
                #print astock_data.find('strong').text
                stock_dic['all_title'] = astock_data.find('strong').text
                all_title = stock_dic['all_title']
                start = all_title.find('(')+1
                end = start+6    
                stock_code = all_title[start:end]
                stock_dic['stock_code']=stock_code
                stock_name = all_title[0:all_title.find('(')] 
                stock_dic['stock_name']=stock_name
                title = all_title[end+1:len(all_title)]
                stock_dic['title']=title
                #print stock_dic['all_title']
                #print stock_dic['stock_code']
                #print stock_dic['stock_name']
                #print stock_dic['title']
            if(i==3):
                #print astock_data.text
                stock_dic['analyst_name']=astock_data.text                
            if(i==4):
                #print astock_data.text
                stock_dic['analyst_company']=astock_data.text    
            if(i==5):
                #print astock_data.text
                stock_dic['new_price']=astock_data.text
            if(i==6):
                #print astock_data.text
                stock_dic['old_price']=astock_data.text
                continue
            i=i+1
            
        upper_rate=float(stock_dic['new_price'].replace(',',''))/float(stock_dic['old_price'].replace(',',''))    
        upper_rate=int((upper_rate-1)*100)        
        stock_dic['upper_rate']=upper_rate
        #print str(stock_dic['upper_rate'])+'%'
        stock_dic['now_price']=getCurrentStockPriceDAUM(stock_dic['stock_code'])
        print stock_dic['now_price']
        stock_dic_list.append(stock_dic)
                
        print stock_dic
        
    return stock_dic_list
    
phantomjs='C:\\phantomjs2.1.1\\bin\\phantomjs.exe'

getCurrentStockConsenFromHK()

    
    
