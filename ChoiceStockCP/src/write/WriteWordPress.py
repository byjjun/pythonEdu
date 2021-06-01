# -*- coding: utf-8 -*-

'''
Created on 2020. 5. 12.

@author: 073860
'''
from selenium import webdriver
from time import time, sleep
from datetime import datetime
from selenium.webdriver.common.keys import Keys


from selenium import webdriver
from time import time, sleep
from datetime import datetime
from selenium.webdriver.common.keys import Keys


def write_init(driver, login_pw):
     ### write post ###
    
    '''
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    opt.add_argument("--disable-gpu")
         
    driver = webdriver.Chrome(chromedrv, chrome_options=opt)
    '''
    ### step 1 , login ###
    driver.get('http://choicestock.cafe24.com/wp-admin/')
    driver.implicitly_wait(100)
    
    login_id = 'choicestock'
    
    
    print(login_id)
    driver.implicitly_wait(1000)
    driver.find_element_by_id('user_login').click()
    driver.find_element_by_id('user_login').send_keys(login_id)
    #driver.implicitly_wait(1000)
    driver.find_element_by_id('user_pass').click()
    driver.find_element_by_id('user_pass').send_keys(login_pw)  
    driver.implicitly_wait(1000)
    driver.find_element_by_id("wp-submit").click()
    return driver


def write_post(driver,category,title, tag, post_content):
    
   
    ### step 2 , write els post title ###
    driver.get("http://choicestock.cafe24.com/wp-admin/post-new.php")
    
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.ALT + Keys.SHIFT + 'M')
    #driver.find_element_by_xpath('//*[@id="post-title-0"]').send_keys(title)
    driver.find_element_by_xpath('//*[@id="post-title-1"]').send_keys(title)
    
    ### step 3, write tag ###
    
    #driver.find_element_by_xpath('//*[@id="new-tag-post_tag"]').send_keys(tag)
    #driver.find_element_by_xpath('//*[@id="post_tag"]/div/div[2]/p/input[2]').click()
        
    ### step 4, write els post ###
    apost = post_content
    #print apost
    
    #textarea에 한방에 집어넣는거.. 신기하네. =_=
    a_post=driver.find_element_by_xpath('//*[@id="post-content-0"]')
    driver.execute_script("arguments[0].value = arguments[1];", a_post, apost)
    sleep(5)
    
    driver.find_element_by_xpath('//*[@id="post-content-0"]').send_keys(Keys.ENTER)
    sleep(10)
        
    ### step 5, select category ####
    driver.implicitly_wait(1000)
    sleep(1)
    
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME) 
    driver.implicitly_wait(1000)

    driver.find_element_by_xpath('//*[@id="editor"]/div/div/div/div[4]/div/div[3]/div[2]/h2/button').click()
    sleep(1)
    driver.find_element_by_xpath(category).click()
    sleep(1)
    
    ### step 6, post submit ####
    
    
    driver.find_element_by_xpath('//*[@id="editor"]/div/div/div/div[1]/div[2]/div[1]/button').click()
    driver.implicitly_wait(1000)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="editor"]/div/div/div/div[3]/div/div/div[1]/div/div/button').click()
    driver.implicitly_wait(1000)
    sleep(5)
    #publish_element = driver.find_element_by_xpath('//*[@id="publish"]')
    #driver.execute_script("arguments[0].click();", publish_element)