# -*- coding: utf-8 -*-


'''
Created on 2018. 5. 11.

@author: 073860
'''

import requests
from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup

phantomjs='C:\\phantomjs2.1.1\\bin\\phantomjs.exe'

'''
DAUM에서 주식 현재가 추출
'''
def getCurrentStockPriceDAUM(stock_code):
    
    stock_price = {}
    
    request_url = 'http://finance.daum.net/item/main.daum?code='+stock_code
    #print request_url
    
    driver = webdriver.PhantomJS(phantomjs)
    driver.get(request_url)
    
    stock_now_price = driver.find_element_by_xpath('//*[@id="topWrap"]/div[1]/ul[2]/li[1]/em')
    stock_updown_rate = driver.find_element_by_xpath('//*[@id="topWrap"]/div[1]/ul[2]/li[3]/span')
    
    stock_price['now_price'] = stock_now_price.text
    stock_price['updown_rate'] = stock_updown_rate.text
    
    #print stock_code
    #print stock_now_price.text
    #print stock_updown_rate.text
    
    #print stock_now_price.text+' ('+stock_updown_rate+')'
    return stock_price

'''
한경 CONSENSUS에서 리포트 추출 
'''
def getCurrentStockConsenFromHK():
    
    #한경 컨세서스 연결.
    #
    stock_dic_list = []
    
    today_str = datetime.today().strftime('%Y-%m-%d')
    #request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate=2018-05-08&edate=2018-05-08&up_down_type=1&pagenum=150&order_type=&now_page=1&order_type=10010000'
    #request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+today_str+'&edate='+today_str+'&up_down_type=1&pagenum=150&order_type=&now_page=1&order_type=10010000'
    request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+today_str+'&edate='+today_str+'&order_type=10010000&pagenum=150'
    
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
            print "."
            
            
            
        upper_rate=float(stock_dic['new_price'].replace(',',''))/float(stock_dic['old_price'].replace(',',''))    
        upper_rate=int((upper_rate-1)*100)        
        stock_dic['upper_rate']=str(upper_rate)
        #print str(stock_dic['upper_rate'])+'%'
        now_stock_price = getCurrentStockPriceDAUM(stock_dic['stock_code'])
        stock_dic['now_price']=now_stock_price['now_price']
        stock_dic['now_updown_rate']=now_stock_price['updown_rate']
        #print stock_dic['now_price']
        diff_rate=float(stock_dic['now_price'].replace(',',''))/float(stock_dic['new_price'].replace(',',''))    
        diff_rate=int(diff_rate*100)
        stock_dic['diff_rate']=str(diff_rate)
        
        stock_dic_list.append(stock_dic)
                
        #print stock_dic
        
    return stock_dic_list


def makeSTOCKHtml(stock_dic_list):
    
    stock_html = "<span style=\"font-size: 10pt;\">금일의 목표가 상승 기업</span><br>"\
    "<span style=\"font-size: 10pt;\">"+str(datetime.today().strftime('%Y-%m-%d %H:%M'))+"기준 발행된 증권사 리서치 보고서 중 목표가가 상승된 기업 리스트 입니다.</span><br>"\
    "<br>FundingChoice에서는 최신자료로 매일 업데이트 됩니다"\
    "<br>오늘자 정보가 아니면 "\
    "<font size=5><a href=\"http://fundingchoice.co.kr/?cat=63\">[여기]</a></font>에서 최신 비교자료를 확인하세요"\
    "<br/>"\
    "&nbsp;" 

    
    pre_stockcode = ""
    count = 1
    for stock_dic in stock_dic_list:
        #if(count ==5):
            #stock_html += "<br>&nbsp;&nbsp;"
        
        if(count == 1 or pre_stockcode != stock_dic['stock_code']):
            stock_html += \
            "<hr style=\"border: double 1px black;\">"\
            "<span style=\"font-size: 10pt;\"><span style=\"font-size: 18pt;\"><strong>"+stock_dic['stock_name'].encode('UTF-8')+"</strong></span>("+stock_dic['stock_code'].encode('UTF-8')+") 현재가 : "+ stock_dic['now_price'].encode('UTF-8')+"("+stock_dic['now_updown_rate'].encode('UTF-8')+")</span><br>"
        else:
            stock_html += \
            "<hr align=\"left\" noshade=\"noshade\" width=\"250\" />"
                    
        stock_html += "<span style=\"font-size: 10pt;\"><span style=\"font-size: 12pt;\"><strong>상승률  : "+ stock_dic['upper_rate'].encode('UTF-8') +"%</strong></span> (<strong>신규"+ stock_dic['new_price'].encode('UTF-8') +"</strong> / 이전 "+stock_dic['old_price'].encode('UTF-8')+")</span><br>"\
        "<span style=\"font-size: 10pt;\"><span style=\"font-size: 12pt;\"><strong>목표대비 : "+stock_dic['diff_rate'].encode('UTF-8')+"%</strong></span> (현재 "+stock_dic['now_price'].encode('UTF-8')+" / <strong>목표"+stock_dic['new_price'].encode('UTF-8')+"</strong>)</span><br>"\
        "<span style=\"font-size: 10pt;\">"+stock_dic['analyst_company'].encode('UTF-8')+"("+stock_dic['analyst_name'].encode('UTF-8')+")</span><br>"\
        "<span style=\"font-size: 10pt;\">   - "+stock_dic['title'].encode('UTF-8')+"</span><br>"
        #"<hr align=\"left\" noshade=\"noshade\" width=\"250\" />"

        #if(count == 1 or pre_stockcode != stock_dic['stock_code']):
            #stock_html += "<hr />"
        count = count+1
        pre_stockcode=stock_dic['stock_code']
        
    stock_html += \
    "<br><br>"\
    "<hr style=\"border: double 1px black;\">"\
    "<span style=\"font-size: 10pt;\">증권 투자는 원금손실의 가능성에 유의하시고, 투자자 본인의 판단과 책임하에 최종 결정을 하셔야 합니다. </span><br>"\
    "<span style=\"font-size: 10pt;\">본 자료는 어떠한 경우에도 증권투자 결과에 대한 법적 책임소재의 증빙자료로 사용될 수 없습니다.</span><br>"    
    
    return stock_html
 

def getStockConsenStockMain():
    
    stock_dic_list = getCurrentStockConsenFromHK()
    stock_dic_list_sorted = sorted(stock_dic_list, key=lambda k: float(k['upper_rate']), reverse=True)
    print makeSTOCKHtml(stock_dic_list_sorted)
    return makeSTOCKHtml(stock_dic_list_sorted)

#getStockConsenStockMain()
