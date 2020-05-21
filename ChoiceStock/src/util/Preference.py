# -*- coding: utf-8 -*-
'''
Created on 2020. 5. 21.

@author: 073860
'''

import platform
from selenium import webdriver


# Initialize
phantomjs= None
chromedrive = None
driver = None
pre_price_count = None
stock_rank_count = None
stock_days_count = None
stock_load_count = None

def setPhantomjsPath():
    global phantomjs
    if(platform.system() == 'Windows'):
        phantomjs='C:\\phantomjs2.1.1\\bin\\phantomjs.exe'
    else:
        phantomjs='/usr/bin/phantomjs'

def setChromedriverPath():
    global chromedrive
    if(platform.system() == 'Windows'):
        chromedrive='C:\\dev\\py_stockchoice\\ChoiceStock\\src\\write\\lib\\chromedriver.exe'
    else:
        chromedrive='/usr/bin/chromedriver'

def setWebDriverInit():
    global driver
    opt = webdriver.ChromeOptions()
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
