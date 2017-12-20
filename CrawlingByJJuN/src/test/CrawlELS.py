#-*- coding: utf-8 -*-

'''
Created on 2017. 12. 14.

@author: 073860
'''


import time
from selenium import webdriver
from bs4 import BeautifulSoup
from __builtin__ import file

PAUSE_TIME = 15


driver = webdriver.Chrome('lib\chromedriver.exe')
driver.get("http://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/etcann/DISDLSSubscribing.xml&divisionId=MDIS04007001000000&serviceId=SDIS04007001000")
time.sleep(PAUSE_TIME)
#driver.implicitly_wait(30)
#print(driver.page_source)


print("START")
tbody_main = driver.find_element_by_id("grdMain_body_tbody")
grid_body = tbody_main.find_elements_by_class_name("grid_body_row")

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    
    for body in grid_body:
        val1 = body.find_element_by_class_name("grdMain_columnstyle_1_")
        val2 = body.find_element_by_class_name("grdMain_columnstyle_2_")
        val3 = body.find_element_by_class_name("grdMain_columnstyle_3_")
        val4 = body.find_element_by_class_name("grdMain_columnstyle_4_")
        val5 = body.find_element_by_class_name("grdMain_columnstyle_5_")
        print(val1.get_attribute('innerHTML'))
        print(val2.get_attribute('innerHTML'))
        print(val3.get_attribute('innerHTML'))
        print(val4.get_attribute('innerHTML'))
        print(val5.get_attribute('innerHTML'))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
#print(len(grid_body))

#grid_body_row

#driver.find_element_by_xpath('//*[@id="gRow1"]')
src_els = driver.page_source

soup = BeautifulSoup(src_els, 'html.parser')
#print(soup.prettify('utf-8', "minimal"))

#print(soup.prettify())


#time.sleep(20)
print("########START########")
ff = open("d:\\temp\\crawdata.html",'w')
ff.write(soup.prettify().encode('utf-8'))
ff.close()



print("END")

#textindex = soup.find_all('nobr')
#textindex = soup.find_all('gRow1')
#print(textindex)
#for text in textindex:
    #print(text)


'''
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

'''

