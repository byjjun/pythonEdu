#-*- coding: utf-8 -*-
'''
Created on 2018. 3. 17.

@author: 073860
'''

from selenium import webdriver
from time import time, sleep
from datetime import datetime


from ELS import XmlParser4ELS
from ELS import MakeELSHtml
from SAVING import SavingMain
from STOCK import MakeStockMain
from LOAN import CreditLoanMakeHtml
from selenium.webdriver.common.keys import Keys
import requests as RR
import json
import traceback

def saving_title():
    #datetime.today().strftime('%Y년 %m월 %d일 '),'기준 '
    saving_title = datetime.today().strftime('%Y년 %m월 %d일 '),'은행 / 저축은행 예금 금리비교 Top 10 '
    return saving_title
def saving_tag():
    saving_tag = '금리비교, 고금리, 예금, 예금추천, 정기예금, 적금, 특판, 우대금리',''.decode('utf-8').encode('utf-8')
    return saving_tag
def saving_post():
    saving_post = SavingMain.str_saving()
    return saving_post

def ins_saving_title():
    #datetime.today().strftime('%Y년 %m월 %d일 '),'기준 '
    ins_saving_title = datetime.today().strftime('%Y년 %m월 %d일 '),'은행/저축은행 적금 금리비교 Top 10 '
    return ins_saving_title
def ins_saving_tag():
    ins_saving_tag = '금리비교, 고금리, 적금, 적금추천, 예금추천, 정기적금, 예금, 특판, 우대금리',''.decode('utf-8').encode('utf-8')
    return ins_saving_tag
def ins_saving_post():
    ins_saving_post = SavingMain.str_inssaving()
    return ins_saving_post

def els_title():
    #datetime.today().strftime('%Y년 %m월 %d일 '),'기준 '
    els_title = datetime.today().strftime('%Y년 %m월 %d일 '),'-청약중인 ELS목록 모아보기 '
    return els_title
def els_tag():
    els_tag = '금리비교, ELS랭킹, ELS순위, ELS추천, 고금리, 예금, 적금, 투자, 특판, 청약',''.decode('utf-8').encode('utf-8')
    return els_tag
def els_post():
    elsdiclist = XmlParser4ELS.elsparser()
    rate_sorted = sorted(elsdiclist, key=lambda k: float(k['elsrate']), reverse=True)
    els_post=MakeELSHtml.make_str_elshtml(rate_sorted, XmlParser4ELS.return_totalcount())    
    return els_post

def stock_title():
    stock_title = datetime.today().strftime('%Y년 %m월 %d일 '),' 증권사 추천주 - 목표가상승기업 '
    return stock_title
def stock_tag():
    stock_tag = '주식투자, 리서치, 보고서, 주식추천, 애널리스트, 증권가찌라시',''.decode('utf-8').encode('utf-8')
    return stock_tag
def stock_post():
    stock_post = MakeStockMain.getStockConsenStockMain()
    return stock_post

def creditloan_title():
    creditloan_title = datetime.today().strftime('%Y년 %m월 %d일 '),'- 신용대출 금리비교 '
    return creditloan_title
def creditloan_tag():
    creditloan_tag = '카카오 뱅크,비상금 대출,신용 대출,중소기업 진흥 공단,마통,마이너스 통장,대출금리,대출금리비교,대출추천',''.decode('utf-8').encode('utf-8')
    return creditloan_tag
def creditloan_post():
    creditloan_post=CreditLoanMakeHtml.creditloanmain()
    return creditloan_post

def write_init():
     ### write post ###
    
     
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    opt.add_argument("--disable-gpu")
     
    ### step 1 , login ###
    driver = webdriver.Chrome('lib\chromedriver.exe', chrome_options=opt)
    #driver = webdriver.Chrome('lib\chromedriver.exe')
    '''
    
    phantomjs='C:\\phantomjs2.1.1\\bin\\phantomjs.exe'
    driver = webdriver.PhantomJS(phantomjs)
    '''
    
    driver.get('http://fundingchoice.co.kr/wp-admin/')
    driver.implicitly_wait(100)
    
    login_id = 'byjjun@gmail.com'
    login_pw = ''
    
    print login_id
    driver.implicitly_wait(1000)
    driver.find_element_by_id('user_login').click()
    driver.find_element_by_id('user_login').send_keys(login_id)
    #driver.implicitly_wait(1000)
    driver.find_element_by_id('user_pass').click()
    driver.find_element_by_id('user_pass').send_keys(login_pw)  
    #driver.implicitly_wait(1000)
    driver.find_element_by_id("wp-submit").click()
    return driver


def write_post(driver,category,title, tag, post_content):
    
    ### step 2 , write els post title ###
    driver.get("http://fundingchoice.co.kr/wp-admin/post-new.php")
    #driver.find_element_by_xpath('//*[@id="post-title-0"]').send_keys(title)
    driver.find_element_by_xpath('//*[@id="title"]').send_keys(title)
    
    ### step 3, write tag ###
    driver.find_element_by_xpath(category).click()
    driver.find_element_by_xpath('//*[@id="new-tag-post_tag"]').send_keys(tag)
    driver.find_element_by_xpath('//*[@id="post_tag"]/div/div[2]/p/input[2]').click()
        
    ### step 4, write els post ###
    apost = post_content
    #print apost
    #textarea에 한방에 집어넣는거.. 신기하네. =_=
    a_post=driver.find_element_by_id("content")
    driver.execute_script("arguments[0].value = arguments[1];", a_post, apost)
    
    ### step 5, post submit ####
    driver.implicitly_wait(1000)
    sleep(1)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME) 
    driver.implicitly_wait(1000)
    
    publish_element = driver.find_element_by_xpath('//*[@id="publish"]')
    driver.execute_script("arguments[0].click();", publish_element)
    
    #driver.find_element_by_xpath('//*[@id="publish"]').send_keys('')
    #driver.find_element_by_xpath('//*[@id="publish"]').click()

def writeTstoryPost(category,title,tag,contents):
    '''
    $$$$카테고리 $$$$
    ELS 771976
        예금적금 771977
        주식 771978
        대출받기 771980
    '''
    url = 'https://www.tistory.com/apis/post/write'
    print url
    
    parameter = {'access_token' : 'cb08c8f727865836f77fd2fed9f4aef8_f76acdd266a3ec3bda480f948f4a3915',
                 'blogName': 'fundingchoice',
                 'title' : 'title'
                 }
    
    post_data = {'content' : '<br>contents</br>으아아아',
                 'tag' : '',
                 'visibility' : '3', 
                 'category' : '771976' }
    
    
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


############################
#### FundingChoice 포스팅
#### Chrome Driver 사용
############################

'''
fundingchoice.co.kr은 접었음.
'''
'''
driver = write_init()
#driver.maximize_window()
sleep(2)

try:
    
    print "els"
    write_post(driver,'//*[@id="in-category-61"]', els_title(), els_tag(),els_post())
    driver.implicitly_wait(1000)
    sleep(2)
    print "예금"
    write_post(driver,'//*[@id="in-category-62"]', saving_title(), saving_tag(), saving_post())
    driver.implicitly_wait(1000)
    sleep(2)
    print "적금"
    write_post(driver,'//*[@id="in-category-62"]', ins_saving_title(), ins_saving_tag(),ins_saving_post())
    driver.implicitly_wait(1000)
    sleep(2)   
    print "대출" 
    write_post(driver,'//*[@id="in-category-5"]', creditloan_title(), creditloan_tag(),creditloan_post())
    driver.implicitly_wait(1000)
    sleep(2)
    
    print "주식"
    write_post(driver,'//*[@id="in-category-63"]', stock_title(), stock_tag(),stock_post())
    sleep(2)
    
except:
    print "ERROR"
#driver.close()
driver.quit()
'''

####################
#### TISTORY 포스팅
#### Open API 사용
####################

try:
    
    title = ''.join(els_title())
    tag = ''.join(els_tag())
    post = ''.join(els_post())
    writeTstoryPost('771976',title,tag,post)
    
    title = ''.join(saving_title())
    tag = ''.join(saving_tag())
    post = ''.join(saving_post())
    writeTstoryPost('771977',title,tag,post)
    
    title = ''.join(ins_saving_title())
    tag = ''.join(ins_saving_tag())
    post = ''.join(ins_saving_post())
    writeTstoryPost('771977',title,tag,post)
    
    title = ''.join(creditloan_title())
    tag = ''.join(creditloan_tag())
    post = ''.join(creditloan_post())
    writeTstoryPost('771980',title,tag,post)
    
    title = ''.join(stock_title())
    tag = ''.join(stock_tag())
    post = ''.join(stock_post())
    writeTstoryPost('771978',title,tag,post)
    
except Exception as e:
    print(e)
    traceback.print_exc()
    print "###ERROR###"
