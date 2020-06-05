# -*- coding: utf-8 -*-


'''
Created on 2020. 5. 21.

@author: 073860
'''

import sys
from datetime import datetime
from pytz import timezone
from src.write import WriteWordPress, HtmlMaker
from src.util import Preference
from src.get import GetStockListfromHK


def main(login_pw):
    
    #환경세팅
    Preference.setPhantomjsPath()
    Preference.setChromedriverPath()
    Preference.setWebDriverInit()
    
    try:
        #최근 몇개 주식을 가지고 올것이냐(250)
        Preference.setStockLoadCount("250")
        #250
        #괴리율 랭킹 몇등까지 표출
        Preference.setStockRankCount(30)
        #20
         #이전목표주가는 몇개까지 표출
        Preference.setPrePriceCount(7)
        #7
        #몇일전 보고서 까지 찾을꺼냐
        Preference.setStockDaysCount(14)
        #14
            
        stock_dic_list = GetStockListfromHK.getUpturnStockFromHK()
        
        result_html = HtmlMaker.makeUpturnStockHtml(stock_dic_list)
        
        print "  "
        print "--------------------------------"
        print "  "
        
        print result_html 
        
        print "--------------------------------"
        
        KST=datetime.now(timezone('Asia/Seoul'))
        title_name = KST.strftime('%Y년 %m월 %d일 %H시 '),' 목표가 상향기업 '
        
        driver = Preference.getWebDriver()
        WriteWordPress.write_post(WriteWordPress.write_init(driver,login_pw), Preference.getCategory("목표상향"), title_name, "", result_html)
        print "--------------------------------"
        
        
    except Exception as e:
        print "exception"
        print(e)
        
    finally:
        #Driver 닫기
        Preference.setWebDriverClose()
        

if __name__ == '__main__':
    print "=========================="
    print "========[ START ]========="    
    print "=========================="
    
    main(sys.argv[1])

    print "=========================="
    print "========[ SUCCESS ]========="    
    print "=========================="
