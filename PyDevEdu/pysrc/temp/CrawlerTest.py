'''
Created on 2017. 12. 7.

@author: 073860
'''

import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver


#req = rq.get("http://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/etcann/DISDLSSubscribing.xml&divisionId=MDIS04007001000000&serviceId=SDIS04007001000#!")
#html = req.text

driver = webdriver.Chrome('C:\GitArea\hub_pythonEdu\lib\chromedriver.exe')

driver.get("http://learning.daishin.co.kr")
driver.implicitly_wait(2)

driver.find_element_by_name("p_userid").send_keys("ds073860")
driver.find_element_by_name("p_pwd").send_keys("073860")
driver.find_element_by_xpath('//*[@class="submit"]').click()

driver.implicitly_wait(2)



#soup = BeautifulSoup(html, 'html.parser')

#print(soup)



