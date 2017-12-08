'''
Created on 2017. 12. 7.

@author: 073860
'''

import requests as rq
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from _ast import Pass


#req = rq.get("http://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/etcann/DISDLSSubscribing.xml&divisionId=MDIS04007001000000&serviceId=SDIS04007001000#!")
#html = req.text

driver = webdriver.Chrome('C:\GitArea\hub_pythonEdu\lib\chromedriver.exe')

driver.get("http://learning.daishin.co.kr")
driver.implicitly_wait(2)

driver.find_element_by_name("p_userid").send_keys("ds073860")
driver.find_element_by_name("p_pwd").send_keys("073860")
driver.find_element_by_xpath('//*[@class="submit"]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@class="btn01"]').click()

if(len(driver.window_handles) > 1):
    driver.switch_to_window(driver.window_handles[1])

while True:
    #c_url = driver.current_url
    #print(c_url)
    time.sleep(60)
    try :
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[1]').click()
    except:
        Pass
    print(driver.current_url)

#driver.implicitly_wait(30)
#c_url = driver.current_url
#print(c_url)
#soup = BeautifulSoup(html, 'html.parser')

#print(soup)
