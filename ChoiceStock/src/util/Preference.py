# -*- coding: utf-8 -*-
'''
Created on 2020. 5. 21.

@author: 073860
'''

import platform
from selenium import webdriver
from datetime import datetime
from pytz import timezone



# Initialize
phantomjs= None
chromedrive = None
driver = None
pre_price_count = None
stock_rank_count = None
stock_days_count = None
stock_load_count = None


def getCategory(categorykind):
    if(categorykind == '상승여력'):
        #return '//*[@id="inspector-checkbox-control-7"]'
        return '//*[@id="editor"]/div/div/div/div[4]/div/div[3]/div[3]/div/div[4]/div/div/span'
    
    elif(categorykind == '목표상향'):
        return '//*[@id="editor"]/div/div/div/div[4]/div/div[3]/div[2]/div/div[2]/div/div/span'
    
    elif(categorykind == '거래폭발'):
        return '//*[@id="editor"]/div/div/div/div[4]/div/div[3]/div[2]/div/div[1]/div/div/span'
    
    else:
        #미분류
        return '//*[@id="editor"]/div/div/div/div[4]/div/div[3]/div[2]/div/div[3]/div/div/span' 


def getVolAgainstTime(volume_ratio):
    result = False
    
    KST=datetime.now(timezone('Asia/Seoul'))
    time_info = KST.strftime('%H%M')
    print "-----"
    print time_info
    print volume_ratio
    print "-----"
    
    if(int(time_info) < 950):
        if(float(volume_ratio) > 50.0):
             result=True
        else:
            result=False
    if(int(time_info) < 1020):
        if(float(volume_ratio) > 80.0):
             result=True
        else:
            result=False
    if(int(time_info) < 1110):
        if(float(volume_ratio) > 100.0):
             result=True
        else:
            result=False
    if(int(time_info) < 1310):
        if(float(volume_ratio) > 150.0):
             result=True
        else:
            result=False
    else:
        if(float(volume_ratio) > 250.0):
             result=True
        else:
            result=False
    
    return result


def isLinux():
    result = False
    if(platform.system() == 'Windows'):
        result = False
    else:
        result = True
    return result


def setPhantomjsPath():
    global phantomjs
    if(platform.system() == 'Windows'):
        phantomjs='C:\\phantomjs2.1.1\\bin\\phantomjs.exe'
    else:
        phantomjs='/usr/bin/phantomjs'

def setChromedriverPath():
    global chromedrive
    if(platform.system() == 'Windows'):
        chromedrive='C:\\git_repo\\pythonEdu\\ChoiceStock\\src\\write\\lib\\chromedriver.exe'
    else:
        chromedrive='/usr/bin/chromedriver'

def setWebDriverInit():
    global driver
    opt = webdriver.ChromeOptions()
    
    #headless
    opt.add_argument('headless')
    opt.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(chromedrive, chrome_options=opt)
    return driver

def getWebDriver():
    global driver
    return driver

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


# Driver Close
def setWebDriverClose():
    global driver
    driver.quit()
