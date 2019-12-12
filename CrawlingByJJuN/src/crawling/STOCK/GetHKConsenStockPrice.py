# -*- coding: utf-8 -*-


'''
Created on 2018. 5. 11.

@author: 073860
'''

import requests
from selenium import webdriver
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from telnetlib import theNULL

phantomjs='C:\\phantomjs2.1.1\\bin\\phantomjs.exe'


'''
현재가를 네이버에서 들고오는걸로 변경(지금버전 2019.6.19)
'''
def getCurrentStockPriceNaver(stock_code):
    
    stock_price = {}
    if stock_code == '130960':
        stock_code = '035760'
    
    request_url = 'https://finance.naver.com/item/main.nhn?code='+stock_code
        
    driver = webdriver.PhantomJS(phantomjs, service_args=['--cookies-file=/tmp/cookies.txt'])
    
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
    #driver.service.process.send_signal(signal.SIGTERM)
    driver.quit()
        
    return stock_price


'''
DAUM에서 주식 현재가 추출
'''
def getCurrentStockPriceDAUM(stock_code):
    
    stock_price = {}
    if stock_code == '130960':
        stock_code = '035760'
    
    request_url = 'http://finance.daum.net/item/main.daum?code='+stock_code
    driver = webdriver.PhantomJS(phantomjs)
    #print request_url
    try:
        #driver = webdriver.PhantomJS(phantomjs)
        driver.get(request_url)
        
        stock_now_price = driver.find_element_by_xpath('//*[@id="topWrap"]/div[1]/ul[2]/li[1]/em')
        stock_updown_rate = driver.find_element_by_xpath('//*[@id="topWrap"]/div[1]/ul[2]/li[3]/span')
        
        stock_price['now_price'] = stock_now_price.text
        stock_price['updown_rate'] = stock_updown_rate.text
    except:
        stock_price['now_price'] = "0"
        stock_price['updown_rate'] = "0"
    
    #print stock_code
    #print stock_now_price.text
    #print stock_updown_rate.text
    
    #print stock_now_price.text+' ('+stock_updown_rate+')'
    driver.close()
    return stock_price


'''
PAXNET에서 주식 현재가 추출
'''
def getCurrentStockPricePAXNET(stock_code):
    
    stock_price = {}
    if stock_code == '130960':
        stock_code = '035760'
    
    request_url = 'http://paxnet.moneta.co.kr/stock/analysis/main?abbrSymbol='+stock_code
    #print request_url
    driver = webdriver.PhantomJS(phantomjs)
    try:
        #driver = webdriver.PhantomJS(phantomjs)
        driver.get(request_url)
        #print request_url
        
        stock_now_price = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[1]/td[1]/span')
        #print stock_now_price.text
        
        stock_updown_rate = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div[1]/div/table/tbody/tr[3]/td[1]/span')
        #print stock_updown_rate.text
        
        
        stock_price['now_price'] = stock_now_price.text
        stock_price['updown_rate'] = stock_updown_rate.text
    
    except:
        stock_price['now_price'] = "0"
        stock_price['updown_rate'] = "0"
    
    #print stock_code
    #print stock_now_price.text
    #print stock_updown_rate.text
    
    #print stock_now_price.text+' ('+stock_updown_rate+')'
    driver.close()
    return stock_price


'''
MK증권 에서 주식 현재가 추출
'''
def getCurrentStockPriceMK(stock_code):
    
    stock_price = {}
    if stock_code == '130960':
        stock_code = '035760'
    
    request_url = 'http://vip.mk.co.kr/newSt/price/price.php?stCode='+stock_code
    #print request_url
    driver = webdriver.PhantomJS(phantomjs)
    try:
        #driver = webdriver.PhantomJS(phantomjs)
        driver.get(request_url)
        #print request_url
        
        stock_now_price = driver.find_element_by_xpath('//*[@id="lastTick[6]"]/font[1]')
        #print stock_now_price.text
        
        stock_updown_rate = driver.find_element_by_xpath('//*[@id="disArr[0]"]/span')
        #print stock_updown_rate.text
        
        
        stock_price['now_price'] = stock_now_price.text
        stock_price['updown_rate'] = stock_updown_rate.text
    
    except:
        stock_price['now_price'] = "0"
        stock_price['updown_rate'] = "0"
    
    #print stock_code
    #print stock_now_price.text
    #print stock_updown_rate.text
    
    #print stock_now_price.text+' ('+stock_updown_rate+')'
    driver.close()
    return stock_price

'''
최근 2달 목표주가 추출
'''
def getPreStockConsenFromHK(stock_code):
    driver = webdriver.PhantomJS(phantomjs)
    try:
        stock_pre_consen_list = []
        
        today = date.today()
        
        yesterday = today - timedelta(1)
        pre_2month = today - timedelta(60)
        
        yesterday_str = yesterday.strftime('%Y-%m-%d')
        pre_2month_str = pre_2month.strftime('%Y-%m-%d')
        
        request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?sdate='+pre_2month_str+'&edate='+yesterday_str+'&now_page=1&search_value=&report_type=CO&pagenum=50&search_text='+stock_code+'&business_code='
        #print request_url
        
        #driver = webdriver.PhantomJS(phantomjs)
        driver.get(request_url)
        
        table_element = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/tbody')
        tablebody_html = table_element.get_attribute('innerHTML')
        #print tablebody_html
        
        soup = BeautifulSoup(tablebody_html, "html.parser")
        
        stock_element_list = soup.find_all('tr')
        count = 1
        
        for stock_element in stock_element_list:
            
            #DATE
            upload_date=stock_element.td.string
            stock_data = stock_element.find_all('td')
            stock_pre_consen ={}
            i = 1
            
            for astock_data in stock_data:
                if(i==1):
                    #print astock_data.text
                    stock_pre_consen['update_date']=astock_data.text
                if(i==3):
                    #print astock_data.text
                    stock_pre_consen['consen_price']=astock_data.text
                    print '###'+stock_pre_consen['consen_price']
                                    
                if(i==4):
                    #print astock_data.text
                    stock_pre_consen['opinion']=astock_data.text    
                if(i==6):
                    #print astock_data.text
                    stock_pre_consen['anal_company']=astock_data.text
                i=i+1
                #print "."
            
            if(stock_pre_consen['consen_price']=='0'):
                print 'Not Rated'
                
            else:
                stock_pre_consen_list.append(stock_pre_consen)
                count+=1
                #print '####'+count
            
            #print 'debug4'
            #print count
                 
            if (count > 7):
                print '7 line limited'
                break
                
    except Exception, e:
        
        print 'No Pre Consen'
        print str(e)        
    
    driver.close()
    return stock_pre_consen_list

'''
한경 CONSENSUS에서 리포트 추출 
'''
def getCurrentStockConsenFromHK():
    
    #한경 컨세서스 연결.
    
    stock_dic_list = []
    
    today = date.today()   
    yesterday = today - timedelta(1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    
    today_str = datetime.today().strftime('%Y-%m-%d')
    #request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate=2018-05-08&edate=2018-05-08&up_down_type=1&pagenum=150&order_type=&now_page=1&order_type=10010000'
    #request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+today_str+'&edate='+today_str+'&up_down_type=1&pagenum=150&order_type=&now_page=1&order_type=10010000'
    request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+yesterday_str+'&edate='+today_str+'&order_type=10010000&pagenum=150'
    print request_url
    
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
        
        now_stock_price = getCurrentStockPriceNaver(stock_dic['stock_code'])
                
        stock_dic['now_price']=now_stock_price['now_price']
        stock_dic['now_updown_rate']=now_stock_price['updown_rate']
        #print stock_dic['now_price']
        diff_rate=float(stock_dic['now_price'].replace(',',''))/float(stock_dic['new_price'].replace(',',''))    
        diff_rate=int(diff_rate*100)
        stock_dic['diff_rate']=str(diff_rate)
        
        stock_dic_list.append(stock_dic)
                
        #print stock_dic
        
    driver.close()    
    return stock_dic_list


'''
최근 2달 목표주가 html로 리턴
'''
def makePreSTOCKHtml(stockcode):
    
    stock_pre_consen_list = getPreStockConsenFromHK(stockcode)
   #print "debug1"
   #print stock_pre_consen_list
   
    html_str = '<span style=\"font-size: 8pt;\">'
    html_str += '<table width=\"450\">'
    #html_str += '<tr>'
    
    for astock_pre_consen in stock_pre_consen_list:
        
        
        html_str += '<tr hight=\"8\">'
        html_str += '<td>'
        html_str += astock_pre_consen['update_date'].encode('UTF-8')
        html_str += '</td><td>'
        html_str += astock_pre_consen['consen_price'].encode('UTF-8')
        html_str += '</td><td>'
        html_str += astock_pre_consen['opinion'].encode('UTF-8').lstrip('\n').rstrip()
        html_str += '</td><td>'
        html_str += astock_pre_consen['anal_company'].encode('UTF-8')
        html_str += '</td></tr>'
    
    html_str += '</table></span>'
        
    return html_str

def makeSTOCKHtml(stock_dic_list):
    
    stock_html = "<span style=\"font-size: 10pt;\">금일/전일의 목표가 상승 기업</span><br>"\
    "<span style=\"font-size: 10pt;\">"+str(datetime.today().strftime('%Y-%m-%d %H:%M'))+"기준 발행된 증권사 리서치 보고서 중 목표가가 상승된 기업 리스트 입니다.</span><br>"\
    "<br>FundingChoice에서는 최신자료로 매일 업데이트 됩니다"\
    "<br>오늘자 정보가 아니면 "\
    "<font size=5><a href=\"http://fundingchoice.co.kr/?cat=63\">[여기]</a></font>에서 최신 비교자료를 확인하세요"\
    "<br/>"\
    "&nbsp;" 

    
    pre_stockcode = ""
    pre_stockconsen_html =""
    
    count = 1
    for stock_dic in stock_dic_list:
        #if(count ==5):
            #stock_html += "<br>&nbsp;&nbsp;"
        
        #if(count == 1 or pre_stockcode != stock_dic['stock_code']):
        stock_html += \
        "<hr style=\"border: double 1px black;\">"\
        "<span style=\"font-size: 10pt;\"><span style=\"font-size: 18pt;\"><strong><a href=\"https://finance.naver.com/item/main.nhn?code="+stock_dic['stock_code'].encode('UTF-8')+"\" target=\"_blank\">" +stock_dic['stock_name'].encode('UTF-8')+"</a></strong></span>("+stock_dic['stock_code'].encode('UTF-8')+") 현재가 : "+ stock_dic['now_price'].encode('UTF-8')+"("+stock_dic['now_updown_rate'].encode('UTF-8')+")</span><br>"
            
            #print 'debug3'
        pre_stockconsen_html=makePreSTOCKHtml(stock_dic['stock_code'])
        print "."
            #print pre_stockconsen_html
            
        #else:
        #    stock_html += \
        #    "<hr align=\"left\" noshade=\"noshade\" width=\"250\" />"
                    
        stock_html += "<span style=\"font-size: 10pt;\"><span style=\"font-size: 12pt;\"><strong>상승률  : "+ stock_dic['upper_rate'].encode('UTF-8') +"%</strong></span> (<strong>신규"+ stock_dic['new_price'].encode('UTF-8') +"</strong> / 이전 "+stock_dic['old_price'].encode('UTF-8')+")</span><br>"\
        "<span style=\"font-size: 10pt;\"><span style=\"font-size: 12pt;\"><strong>목표대비 : "+stock_dic['diff_rate'].encode('UTF-8')+"%</strong></span> (현재 "+stock_dic['now_price'].encode('UTF-8')+" / <strong>목표"+stock_dic['new_price'].encode('UTF-8')+"</strong>)</span><br>"\
        "<span style=\"font-size: 10pt;\">"+stock_dic['analyst_company'].encode('UTF-8')+"("+stock_dic['analyst_name'].encode('UTF-8')+") : " + stock_dic['update_date'].encode('UTF-8') + "</span><br>"\
        "<span style=\"font-size: 10pt;\">   - "+stock_dic['title'].encode('UTF-8')+"</span>"
        #"<hr align=\"left\" noshade=\"noshade\" width=\"250\" />"

        #if(count == 1 or pre_stockcode != stock_dic['stock_code']):
            #stock_html += "<hr />"
        count = count+1
        pre_stockcode=stock_dic['stock_code']
        stock_html += pre_stockconsen_html + '<br>'
        
    stock_html += \
    "<br><br>"\
    "<hr style=\"border: double 1px black;\">"\
    "<span style=\"font-size: 10pt;\">증권 투자는 원금손실의 가능성에 유의하시고, 투자자 본인의 판단과 책임하에 최종 결정을 하셔야 합니다. </span><br>"\
    "<span style=\"font-size: 10pt;\">본 자료는 어떠한 경우에도 증권투자 결과에 대한 법적 책임소재의 증빙자료로 사용될 수 없습니다.</span><br>"    
    
    return stock_html
 
 

def getStockConsenStockMain():
    
    stock_dic_list = getCurrentStockConsenFromHK()
    #stock_dic_list_sorted = sorted(stock_dic_list, key=lambda k: float(k['stock_code']), reverse=True)
    stock_dic_list_sorted = sorted(stock_dic_list, key=lambda k: k['stock_code'], reverse=True)
    print makeSTOCKHtml(stock_dic_list_sorted)
    return makeSTOCKHtml(stock_dic_list_sorted)

#getStockConsenStockMain()

#getPreStockConsenFromHK('058470')