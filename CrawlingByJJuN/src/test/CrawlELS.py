#-*- coding: utf-8 -*-

'''
Created on 2017. 12. 14.

@author: 073860
'''


import time
from selenium import webdriver
from bs4 import BeautifulSoup
from __builtin__ import file


driver = webdriver.Chrome('lib\chromedriver.exe')
driver.get("http://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/etcann/DISDLSSubscribing.xml&divisionId=MDIS04007001000000&serviceId=SDIS04007001000")
time.sleep(20)
#driver.implicitly_wait(30)
#print(driver.page_source)

driver.find_element_by_xpath('//*[@id="gRow1"]')
src_els = driver.page_source

soup = BeautifulSoup(src_els, 'html.parser')
print(soup.prettify('utf-8', "minimal"))

#print(soup.prettify())


#time.sleep(20)
print("########START########")
ff = open("d:\\temp\\crawdata.html",'w')
ff.write(soup.prettify().encode('utf-8'))
ff.close()

print("########END########")

#textindex = soup.find_all('nobr')
#textindex = soup.find_all('gRow1')
#print(textindex)
#for text in textindex:
    #print(text)




