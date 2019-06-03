# -*- coding: utf-8 -*-

'''
Created on 2019. 4. 9.

@author: 073860
'''

import platform
import requests
from selenium import webdriver
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from time import time, sleep
import requests as RR

# phantomjs='C:\\phantomjs2.1.1\\bin\\phantomjs.exe'
phantomjs='/usr/local/bin/phantomjs'
pre_price_count = 7
stock_rank_count = 20
stock_days_count = 4
stock_load_count = "250"

def setPhantomjsPath():
    global phantomjs
    if(platform.system() == 'Windows'):
        phantomjs='C:\\phantomjs2.1.1\\bin\\phantomjs.exe'
    else:
        phantomjs='/usr/local/bin/phantomjs'


#최근 목표주가 몇개 세팅
def setPrePriceCount(count):
    global pre_price_count
    pre_price_count = count
    
def getPrePriceCount():
    global pre_price_count
    return pre_price_count    
    
#괴리율 높은 주식 몇개 표시
def setStockRankCount(count):
    global stock_rank_count
    stock_rank_count = count

def getStockRankCount():
    global stock_rank_count
    return stock_rank_count

#몇일전 보고서 까지 찾을꺼냐
def setStockDaysCount(count):
    global stock_days_count
    stock_days_count = count

def getStockDaysCount():
    global stock_days_count
    return stock_days_count

#최근 몇개 가지고 분석 할꺼냐
def setStockLoadCount(count):
    global stock_load_count
    stock_load_count = count
    
def getStockLoadCount():
    global stock_load_count
    return stock_load_count


'''
최근 2달간 이전 목표주가 추출
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
                    stock_pre_consen['analyst_company']=astock_data.text
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
                 
            if (count > getPrePriceCount()):
                print getPrePriceCount() + ' line limited'
                break
                
    except Exception, e:
        
        print 'No Pre Consen'
        print str(e)        
    driver.close()
    return stock_pre_consen_list

'''
최근 2달 목표주가 html로 리턴
'''
def makePreSTOCKHtml(stockcode):
    
    stock_pre_consen_list = getPreStockConsenFromHK(stockcode)
   
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
        html_str += astock_pre_consen['analyst_company'].encode('UTF-8')
        html_str += '</td></tr>'
    
    html_str += '</table></span>'
        
    return html_str


'''
MK증권 에서 주식 현재가 추출
'''
def getCurrentStockPriceMK(stock_code):
    
    stock_price = {}
    if stock_code == '130960':
        stock_code = '035760'
    
    request_url = 'http://vip.mk.co.kr/newSt/price/price.php?stCode='+stock_code
    #print request_url
    try:
        driver = webdriver.PhantomJS(phantomjs)
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
MK증권(모바일) 에서 주식 현재가 추출 - 속도개선용
'''
def getCurrentStockPriceMMK(stock_code):
    
    stock_price = {}
    if stock_code == '130960':
        stock_code = '035760'
    
    request_url = 'http://m.mk.co.kr/stock/price/'+stock_code
    #print request_url
    
    try:
        driver = webdriver.PhantomJS(phantomjs) 
        driver.get(request_url)
        #print request_url
        
        stock_now_price = driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[4]/div[2]/ul/li[1]/span[1]')
        #print stock_now_price.text
        
        stock_updown_rate = driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[4]/div[2]/ul/li[1]/span[2]')
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
한경 CONSENSUS에서 리포트 추출
input : none
doing : 
1. 한경 CONSENSUS 접속 - 최근 7일 기업보고서 추출, 목표주가 산출
2. 매경주식페이지 접속 - 현재가 추출
3. 취합 후 tuple로 생성
output : tuple(최근 7일 목표주가, 현재가)
'''
def getCurrentStockConsenFromHK():
    
    #한경 컨세서스 연결.
    
    stock_dic_list = []
    
    today_str = datetime.today().strftime('%Y-%m-%d')
    #몇일전까지 : days=0 은 오늘
    startday_str = (datetime.today() - timedelta(days=getStockDaysCount())).strftime('%Y-%m-%d')
    #몇개 분석할 것이냐?
    stock_count = getStockLoadCount()
    #request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+today_str+'&edate='+today_str+'&order_type=10010000&pagenum=150'
    #http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=business&sdate=2019-04-03&edate=2019-04-09&pagenum=1000&order_type=12000001&now_page=1
    request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=business&sdate='+startday_str+'&edate='+today_str+'&pagenum='+stock_count+'&order_type=12000001&now_page=1'
    
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
        stockcode = '000000'
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
                stockcode=stock_code
                stock_name = all_title[0:all_title.find('(')] 
                stock_dic['stock_name']=stock_name
                title = all_title[end+1:len(all_title)]
                stock_dic['title']=title
                #print stock_dic['all_title']
                #print stock_dic['stock_code']
                #print stock_dic['stock_name']
                #print stock_dic['title']
            if(i==3):
                #적정가격
                #print astock_data.text
                stock_dic['new_price']=astock_data.text                
            if(i==4):
                #print astock_data.text
                stock_dic['opinion']=astock_data.text    
            if(i==5):
                #print astock_data.text
                stock_dic['analyst_name']=astock_data.text
            if(i==6):
                #print "####a####"
                #print astock_data.text
                stock_dic['analyst_company']=astock_data.text
            
            if(i==9):
                for link in astock_data.find_all('a', href=True):
                    url = link['href']
                stock_dic['report_url'] = 'http://hkconsensus.hankyung.com/'+ url
                #print stock_dic['report_url']
                break
            i=i+1
            #print "."
            
        stock_dic['companyinfo_url']='http://media.kisline.com/highlight/mainHighlight.nice?paper_stock='+stockcode+'&nav=1'    
        #print stock_dic['companyinfo_url']        
        
        if(stock_dic['new_price'] != "0" ):
             
            now_stock_price = getCurrentStockPriceMMK(stock_dic['stock_code'])
                    
            stock_dic['now_price']=now_stock_price['now_price']
            stock_dic['now_updown_rate']=now_stock_price['updown_rate']
            
            print(stock_dic['stock_name'])
            print(stock_dic['new_price'])
            print(stock_dic['now_price'])
                  
            diff_rate=float(stock_dic['now_price'].replace(',',''))/float(stock_dic['new_price'].replace(',',''))    
            diff_rate=int(diff_rate*100)
            stock_dic['diff_rate']=str(diff_rate)
            
            print(stock_dic['diff_rate'])
            
            if(diff_rate > 20 and diff_rate < 100):
                stock_dic_list.append(stock_dic)
            
        #print stock_dic
    stock_dic_list_sorted = sorted(stock_dic_list, key=lambda k: k['diff_rate'], reverse=False)
    
    driver.close()           
    return stock_dic_list_sorted


def makeSTOCKHtml(stock_dic_list):
    
    stock_html = "<span style=\"font-size: 10pt;\">금일의 상승여력 랭킹</span><br>"\
    "<span style=\"font-size: 10pt;\">"+str(datetime.today().strftime('%Y-%m-%d %H:%M'))+"기준 발행된 증권사 리서치 보고서 중 목표가와 현 주가의 괴리율이  큰 기업순위입니다.</span><br>"\
    #"<br>FundingChoice에서는 최신자료로 매일 업데이트 됩니다"\
    #"<br>오늘자 정보가 아니면 "\
    #"<font size=5><a href=\"http://fundingchoice.co.kr/?cat=63\">[여기]</a></font>에서 최신 비교자료를 확인하세요"\
    "<br/>"\
    "&nbsp;" 
    
    pre_stockconsen_html =""
    
    count = 1
    for stock_dic in stock_dic_list:
        
        stock_html += \
        "<hr style=\"border: double 1px black;\">"\
        "<span style=\"font-size: 10pt;\"><span style=\"font-size: 18pt;\"><strong><a href=\"https://finance.naver.com/item/main.nhn?code="+stock_dic['stock_code'].encode('UTF-8')+"\" target=\"_blank\">" +stock_dic['stock_name'].encode('UTF-8')+"</a></strong></span>("+stock_dic['stock_code'].encode('UTF-8')+") 현재가 : "+ stock_dic['now_price'].encode('UTF-8')+"("+stock_dic['now_updown_rate'].encode('UTF-8')+")</br>"\
        "<a href=\""+stock_dic['companyinfo_url'].encode('UTF-8')+"\">[기업]</a><a href=\""+stock_dic['report_url'].encode('UTF-8')+"\">[report]</a></span><br>"
                                     
        stock_html += "<span style=\"font-size: 10pt;\"><span style=\"font-size: 12pt;\"><strong>목표가 대비 현재가 : "+stock_dic['diff_rate'].encode('UTF-8')+"%</strong></span> (현재 "+stock_dic['now_price'].encode('UTF-8')+" / <strong>목표"+stock_dic['new_price'].encode('UTF-8')+"</strong>)</span><br>"\
        "<span style=\"font-size: 10pt;\">"+stock_dic['analyst_company'].encode('UTF-8')+"("+stock_dic['analyst_name'].encode('UTF-8')+") : "+stock_dic['update_date'].encode('UTF-8')+"</span><br>"\
        "<span style=\"font-size: 10pt;\">   - "+stock_dic['title'].encode('UTF-8')+"</span>"

        pre_stockconsen_html=makePreSTOCKHtml(stock_dic['stock_code'])
        #print "."

        count = count+1

        stock_html += pre_stockconsen_html + '<br>'
        if (count > getStockRankCount()):
            break
                
    stock_html += \
    "<br><br>"\
    "<hr style=\"border: double 1px black;\">"\
    "<span style=\"font-size: 10pt;\">증권 투자는 원금손실의 가능성에 유의하시고, 투자자 본인의 판단과 책임하에 최종 결정을 하셔야 합니다. </span><br>"\
    "<span style=\"font-size: 10pt;\">본 자료는 어떠한 경우에도 증권투자 결과에 대한 법적 책임소재의 증빙자료로 사용될 수 없습니다.</span><br>"    
    
    return stock_html


def writeTstoryPost(category,title,tag,contents):
    '''
    $$$$카테고리 $$$$
        괴리율 742010

    '''
    url = 'https://www.tistory.com/apis/post/write'
    print url
    
    parameter = {'access_token' : 'cb08c8f727865836f77fd2fed9f4aef8_f76acdd266a3ec3bda480f948f4a3915',
                 'blogName': 'stockchoice',
                 'title' : 'title'
                 }
    
    post_data = {'content' : '<br>contents</br>으아아아',
                 'tag' : '',
                 'visibility' : '3', 
                 'category' : '742010' }
    
    
    parameter['title']=title
    post_data['tag']=tag
    post_data['content']=contents
    post_data['category']=category

    #print title
    #print post_data['title']
    #print post_data['tag']
    #print post_data['content']
    #print post_data['category']
    
    sleep(10)
    
    #r = RR.post(url, params = parameter, data=json.dumps(post_data), verify=False)
    r = RR.post(url, params = parameter, data=post_data, verify=False)
       
    print(r.text)
    print(r.status_code)




def main():
    
    #환경세팅
    setPhantomjsPath()
        
    #최근 몇개 주식을 가지고 올것이냐
    setStockLoadCount("250")
    #250
    
    #괴리율 랭킹 몇등까지 표출
    setStockRankCount(20)
    #20
    
    #이전목표주가는 몇개까지 표출
    setPrePriceCount(7)
    #7
    
    #몇일전 보고서 까지 찾을꺼냐
    setStockDaysCount(14)
    #14
    
    
    stock_dic_list = getCurrentStockConsenFromHK()
    
    result_html = makeSTOCKHtml(stock_dic_list)
    
    print "  "
    print "--------------------------------"
    print "  "
    
    print result_html 
    
    print "--------------------------------"
    
    title_name = datetime.today().strftime('%Y년 %m월 %d일 %H시 ')+' 상승여력 랭킹 '
    
    writeTstoryPost("742010",title_name,"",result_html)
    
    print "--------------------------------"
    

main()
