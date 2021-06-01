# -*- coding: utf-8 -*-

'''
Created on 2021. 5. 31.

@author: JJ
'''

import sys
import traceback
from datetime import datetime
from pytz import timezone
from src.write import WriteWordPress, HtmlMaker
from src.util import Preference
from src.get import GetStockListfromHK, GetStockListfromMaster


def main(login_pw):
    
    #환경세팅
    Preference.setPhantomjsPath()
    Preference.setChromedriverPath()
    Preference.setWebDriverInit()
    
    try:
        
        #이전목표주가는 몇개까지 표출
        Preference.setPrePriceCount(7)
        
        stock_dic_list = GetStockListfromMaster.getStockListfromCreonPlus()
        
        for astock in stock_dic_list:
            print(astock['종목명'])
            print(astock['종목코드'])
        
        #print result_html 
        
        '''
        
        print "--------------------------------"
        
        KST=datetime.now(timezone('Asia/Seoul'))
        title_name = KST.strftime('%Y년 %m월 %d일 %H시 '),' 상승여력 랭킹 '
        
        driver = Preference.getWebDriver()
        WriteWordPress.write_post(WriteWordPress.write_init(driver,login_pw), Preference.getCategory("상승여력"), title_name, "", result_html)
        print "--------------------------------"
        
        '''
        
    except Exception as e:
        print('--- stack ---')
        traceback.print_stack()
        print('--- exec ---')
        traceback.print_exc()
        print('--- e ---')
        print(e)
        print("exception")
        
    finally:
        #Driver 닫기
        Preference.setWebDriverClose()
        

if __name__ == '__main__':
    print("==========================")
    print("========[ START ]=========")    
    print("==========================")
    
    main(sys.argv[1])

    print("==========================")
    print("========[ SUCCESS ]=========")    
    print("==========================")
