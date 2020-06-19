# -*- coding: utf-8 -*-

'''
Created on 2020. 6. 19.

@author: 073860
'''

import sys
import traceback
from datetime import datetime
from pytz import timezone
from src.write import WriteWordPress, HtmlMaker
from src.util import Preference
from src.get import GetStockListfromHK


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
    
    GetStockListfromHK.tester()
    
except:
    print "except"
    
    