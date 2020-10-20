# -*- coding: utf-8 -*-

'''
Created on 2017. 12. 7.

@author: 073860
'''

import time
from selenium import webdriver

from _ast import Pass

def webmodule(login_id,login_pw):
    #print(login_id)
    #print(login_pw)
    
    #driver = webdriver.Chrome('C:\GitArea\hub_pythonEdu\lib\chromedriver.exe')
    
    driver = webdriver.Chrome('lib\chromedriver.exe')
    driver.get("http://learning.daishin.co.kr")
    driver.implicitly_wait(2)
    
    #print(login_id, login_pw)
    
    driver.find_element_by_name("p_userid").send_keys(login_id)
    driver.find_element_by_name("p_pwd").send_keys(login_pw)
    driver.find_element_by_xpath('//*[@class="submit"]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@class="btn01"]').click()
    
    # 새 탭이 만들어지면 거기로 핸들러 이동
    if(len(driver.window_handles) > 1):
        driver.switch_to_window(driver.window_handles[1])
    else:
        return 0
    time.sleep(60)
    
    #try :
    #print("start speedup")
    try :
        driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
        driver.implicitly_wait(5)
        #print(driver.page_source)
        #javascript 직접 호출
        driver.execute_script("return changeSpeedRate(0.2)")
        driver.implicitly_wait(1)
        driver.execute_script("return changeSpeedRate(0.2)")
        driver.switch_to_default_content()
    except:
        Pass    
    #print("end speedup")
    
    #driver.implicitly_wait(10)
    #driver.find_element_by_css_selector("#btn_speed_up").click()
    #driver.switch_to_default_content()
    #print("end speedup")
    #except:
     #   Pass
#


#int ok_size=driver.findElements(By.xpath("//button[text()='OK']")).size();
#driver.findElements(By.xpath("//button[text()='OK']")).get(ok_size-1).click();

#    driver.find_element_by_xpath('//*[@id="btn_speed_up"]').click()
#    
    while True:
        
        # 강의 끝났을때 나오는 다음강의 버튼 추출 / 없으면 다시 Pass 후 60초 대기
        try :
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[1]').click()
            driver.implicitly_wait(5)
            driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
            driver.implicitly_wait(5)
            driver.execute_script("return changeSpeedRate(0.2)")
            driver.implicitly_wait(1)
            
            driver.execute_script("return changeSpeedRate(0.2)")
            driver.switch_to_default_content()
            
        except:
            Pass
                
        # 잘 되고있는지 현재 URL 출력
        #print(driver.current_url)
        
        #초기 세팅시간 60초 기다름 / 이후 60초에 버튼 체크
        time.sleep(60)

#input_id="ds073860"
#input_pw="073860"
#webmodule(input_id,input_pw)


