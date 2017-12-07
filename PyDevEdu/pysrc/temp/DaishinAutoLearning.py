'''
Created on 2017. 12. 7.

@author: 073860
'''

import requests as rq
from selenium import webdriver

driver = webdriver.Chrome('C:\GitArea\hub_pythonEdu\lib\chromedriver.exe')

driver.get("http://daishin.ubob.com/Account/Login")
driver.implicitly_wait(2)

#driver.find_element_by_id('Username').send_keys('ds073860')
driver.find_element_by_xpath('//input*[@id="Username"]').send_keys('ds073860')

#driver.find_element_by_name("Username").send_keys("ds073860")
driver.find_element_by_name("Password").send_keys("073860")
driver.find_element_by_xpath('//*[@class="login_btn"]').click()

driver.implicitly_wait(2)
