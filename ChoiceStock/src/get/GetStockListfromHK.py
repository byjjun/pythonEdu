# -*- coding: utf-8 -*-

'''
Created on 2020. 5. 21.

@author: 073860
'''

from datetime import date, datetime, timedelta
from bs4 import BeautifulSoup
from pytz import timezone
from src.util import Preference
from src.get import GetStockPrice


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
    
    KST=datetime.now(timezone('Asia/Seoul'))
    today_str = KST.strftime('%Y-%m-%d')
    #몇일전까지 : days=0 은 오늘
    startday_str = (datetime.today() - timedelta(days=Preference.getStockDaysCount())).strftime('%Y-%m-%d')
    #몇개 분석할 것이냐?
    stock_count = Preference.getStockLoadCount()
    #request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+today_str+'&edate='+today_str+'&order_type=10010000&pagenum=150'
    #http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=business&sdate=2019-04-03&edate=2019-04-09&pagenum=1000&order_type=12000001&now_page=1
    request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=business&sdate='+startday_str+'&edate='+today_str+'&pagenum='+stock_count+'&order_type=12000001&now_page=1'
    
    print(request_url)
    
    driver = Preference.getWebDriver()
    
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
             
            now_stock_price = GetStockPrice.getCurrentStockPriceNaver(stock_dic['stock_code'])
                    
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

    
    return stock_dic_list_sorted



'''
최근 2달간 이전 목표주가 추출
'''
def getPreStockConsenFromHK(stock_code):
    
    #driver = webdriver.PhantomJS(phantomjs, service_args=['--cookies-file=/tmp/cookies.txt'])
    #driver.delete_all_cookies()
    '''
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    opt.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chromedrive, chrome_options=opt)
    '''
    
    
    try:
        stock_pre_consen_list = []
        
        today = date.today()
        
        yesterday = today - timedelta(1)
        pre_2month = today - timedelta(60)
        
        yesterday_str = yesterday.strftime('%Y-%m-%d')
        pre_2month_str = pre_2month.strftime('%Y-%m-%d')
        
        request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?sdate='+pre_2month_str+'&edate='+yesterday_str+'&now_page=1&search_value=&report_type=CO&pagenum=50&search_text='+stock_code+'&business_code='
        print request_url
        
        #driver = webdriver.PhantomJS(phantomjs)
        driver=Preference.getWebDriver()
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
                
                if(i==9):
                    stock_pre_consen['report_url']=astock_data.text
                    print stock_pre_consen['report_url']
                
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
                 
            if (count > Preference.getPrePriceCount()):
                print Preference.getPrePriceCount() + ' line limited'
                break
                
    except Exception, e:
        
        print 'No Pre Consen'
        print str(e)
    
    #driver.service.process.send_signal(signal.SIGTERM)          
    #driver.quit()
    return stock_pre_consen_list


'''
한경 CONSENSUS에서 리포트 추출 - 목표가 상향기업
input : none
doing : 
1. 한경 CONSENSUS 접속 - 최근 2일 목표가 상향기업 URL 호출
2. 매경주식페이지 접속 - 현재가 추출
3. 취합 후 tuple로 생성
output : tuple(최근 7일 목표주가, 현재가)
''' 

def getUpturnStockFromHK():
    
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
        
    
    driver = Preference.getWebDriver()   
    driver.get(request_url)
    
    
    
    
    table_element = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/tbody')
    tablebody_html = table_element.get_attribute('innerHTML')
    
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
                #print '---'
                stock_dic['report_url']=''
                try:
                    spl1 = str(astock_data).split("\n")
                    #print spl1
                    spl2 = spl1[3].split("\"")
                    #print spl2
                    spl3 = spl2[3].split("_")
                    #print spl3
                    report_index = spl3[1]
                    #print report_index
                    stock_dic['report_url']='http://consensus.hankyung.com/apps.analysis/analysis.downpdf?report_idx='+report_index
                except:
                    stock_dic['report_url']=''
                    
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
            #print "."
        

        stock_dic['companyinfo_url']='http://media.kisline.com/highlight/mainHighlight.nice?paper_stock='+stock_code+'&nav=1'    
        #print stock_dic['companyinfo_url']        
        upper_rate=float(stock_dic['new_price'].replace(',',''))/float(stock_dic['old_price'].replace(',',''))    
        upper_rate=int((upper_rate-1)*100)        
        stock_dic['upper_rate']=str(upper_rate)
        
        
        if(stock_dic['new_price'] != "0" ):
             
            now_stock_price = GetStockPrice.getCurrentStockPriceNaver(stock_dic['stock_code'])
                    
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
        
    
    return stock_dic_list_sorted



    
def tester():
    

    today = date.today()   
    yesterday = today - timedelta(1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    
    today_str = datetime.today().strftime('%Y-%m-%d')
    
    request_url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&sdate='+yesterday_str+'&edate='+today_str+'&order_type=10010000&pagenum=150'
    print request_url
        
    
    driver = Preference.getWebDriver()   
    driver.get(request_url)
    
    report_index_element = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/tbody/tr/td[2]/div')
    report_index_html = report_index_element.get_attribute('innerHTML')
    spl = report_index_html.split("\"")
    spl2 = spl[1].split("_")
    report_index = spl2[1]
    
    
    '''
    soup = BeautifulSoup(tablebody_html, "html.parser")
    div_list = soup.find_all('div')
    
    for _div in div_list:
        print _div
        print '---'
    '''

    #print tablebody_html
    
    
    return True
    

