#-*- coding: utf-8 -*-
'''
Created on 2018. 3. 17.

@author: 073860
'''

from selenium import webdriver
from time import time
from datetime import datetime


from ELS import XmlParser4ELS
from ELS import MakeELSHtml

def saving_title():
    #datetime.today().strftime('%Y년 %m월 %d일 '),'기준 '
    saving_title = datetime.today().strftime('%Y년 %m월 %d일 '),'은행/저축은행 예금, 적금 추천순위 Top5 '
    return saving_title
def saving_tag():
    saving_tag = '고금리, 예금, 예금추천, 정기예금, 적금, 특판, 우대금리'
    return saving_tag
def saving_post():
    
    saving_post= 'aa'
    return saving_post

def els_title():
    #datetime.today().strftime('%Y년 %m월 %d일 '),'기준 '
    els_title = datetime.today().strftime('%Y년 %m월 %d일 '),'-청약중인 ELS목록 모아보기 '
    return els_title
def els_tag():
    els_tag = 'ELS랭킹, ELS순위, ELS추천, 고금리, 예금, 적금, 투자, 특판, 청약','UTF-8'.decode('utf-8').encode('utf-8')
    return els_tag
def els_post():
    elsdiclist = XmlParser4ELS.elsparser()
    rate_sorted = sorted(elsdiclist, key=lambda k: k['elsrate'], reverse=True)
    els_post=MakeELSHtml.make_str_elshtml(rate_sorted, XmlParser4ELS.return_totalcount())
    
    print "############## debug ############"
    print els_post
    print "############## debug ############"
    
    return els_post

def write_post(login_id, login_pw):
    
    ### write post ###
    ### step 1 , login ###
    driver = webdriver.Chrome('lib\chromedriver.exe')
    driver.get('http://fundingchoice.co.kr/wp-admin/')
    driver.implicitly_wait(100)
    
    print login_id
    driver.find_element_by_id('user_login').send_keys(login_id)
    driver.find_element_by_id('user_pass').send_keys(login_pw)  
    driver.find_element_by_id("wp-submit").click()
    driver.implicitly_wait(10)
    
    ### step 2 , write els post title ###
    driver.get("http://fundingchoice.co.kr/wp-admin/post-new.php")
    driver.find_element_by_xpath('//*[@id="title"]').send_keys(els_title())
    
    ### step 3, write tag ###
    driver.find_element_by_xpath('//*[@id="category-17"]').click()
    driver.find_element_by_xpath('//*[@id="new-tag-post_tag"]').send_keys(els_tag())
    driver.find_element_by_xpath('//*[@id="post_tag"]/div/div[2]/p/input[2]').click()
        
    ### step 4, write els post ###
    apost = els_post()
    #print apost
    #textarea에 한방에 집어넣는거.. 신기하네. =_=
    a_post=driver.find_element_by_id("content")
    driver.execute_script("arguments[0].value = arguments[1];", a_post, apost)
    
    ### step 5, post submit ####
    driver.find_element_by_xpath('//*[@id="publish"]').click()
    
    '''
    #a_post.clear()
    #a_post.send_keys(apost)
    #a_post.submit()
    #driver.find_element_by_xpath('//*[@id="content"]').clear()
    #driver.find_element_by_xpath('//*[@id="content"]').send_keys(a_post)
    '''
    
    while True:
        time.sleep(1)
    #print(login_id, login_pw)

userid = 'byjjun@gmail.com'
userpw = 'POCKTAN1'

#write_post(userid, userpw)

write_post('byjjun@gmail.com', 'POCKTAN1')