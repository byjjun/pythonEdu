# -*- coding: utf-8 -*-


'''
Created on 2018. 5. 11.

@author: 073860
'''

import requests
from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup
from telnetlib import theNULL

def getCurrentStockConsenFromHK():
    
    #한경 컨세서스 연결.
    #
    stock_dic_list = []
    
    today_str = datetime.today().strftime('%Y-%m-%d')
    #request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate=2018-05-08&edate=2018-05-08&up_down_type=1&pagenum=150&order_type=&now_page=1&order_type=10010000'
    request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+today_str+'&edate='+today_str+'&up_down_type=1&pagenum=150&order_type=&now_page=1&order_type=10010000'
    
    driver = webdriver.PhantomJS('C:\\phantomjs2.1.1\\bin\\phantomjs.exe')
    driver.get(request_url)
    html = driver.page_source
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
                end = all_title.find(')')
                stock_code = all_title[start:end]
                stock_dic['stock_code']=stock_code
                stock_name = all_title[0:all_title.find('(')] 
                stock_dic['stock_name']=stock_name
                title = all_title[all_title.find(')')+1:len(all_title)]
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
        stock_dic_list.append(stock_dic)
        
        print stock_dic
        
    '''
    #parser = etree.XMLParser(recover=True)
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.fromstring(tablebody_html, parser=parser)
    
    stock_conses_dic_list = []
    
    for stockdata_lst in tree.findAll('tr'):
        for stockdata in stockdata_lst:
            print stockdata.findAll('td').text
        
        
    '''
    
    #print tablebody_html
    
    
    
    #title = table_element.find_element_by_xpath('//*[@id="content_477657"]/strong')
    #print title.text
    
    #print table_element
    
    #html = table_element.text
    
    #print html
    return html

    '''    
    session = requests.Session()
    request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate=2018-05-11&edate=2018-05-11&up_down_type=4&pagenum=150&order_type=&up_down_type=1#'
    #request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+today_str+'&edate='+today_str+'&order_type=&pagenum=150&now_page=1'
                       
    print request_url
    raw_data = session.get(request_url)
    #raw_data = requests.get(request_url)
    
    print raw_data.status_code
    html = raw_data.text
    
    #print '-----'
    print html
    #print '-----'
    '''
    
    
    

getCurrentStockConsenFromHK()

    
    
