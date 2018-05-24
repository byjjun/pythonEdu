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

def write_init():
     ### write post ###
    ### step 1 , login ###
    driver = webdriver.Chrome('lib\chromedriver.exe')
    driver.get('http://fundingchoice.co.kr/wp-admin/')
    #driver.implicitly_wait(100)
    
    login_id = 'byjjun@gmail.com'
    login_pw = 'POCKTAN1'
    
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
    #driver.implicitly_wait(10000)
    driver.find_element_by_xpath('//*[@id="publish"]').send_keys('')
    driver.find_element_by_xpath('//*[@id="publish"]').click()
   

#write_post(userid, userpw)
driver = write_init()
sleep(2)
write_post(driver,'//*[@id="in-category-61"]', els_title(), els_tag(),els_post())
driver.implicitly_wait(1000)
sleep(2)
write_post(driver,'//*[@id="in-category-62"]', saving_title(), saving_tag(), saving_post())
driver.implicitly_wait(1000)
sleep(2)
write_post(driver,'//*[@id="in-category-62"]', ins_saving_title(), ins_saving_tag(),ins_saving_post())
