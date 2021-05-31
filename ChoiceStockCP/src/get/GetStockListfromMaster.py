# -*- coding: utf-8 -*-

'''
Created on 2021. 5. 30.

@author: JJ
'''

import win32com.client
from src.get import GetStockListfromHK


def getStockListfromCreonPlus():
    '''
    1 전략 목록 가져오기
    '''
    ## 8357 종목검색Master 전략목록 Object
    cpsysdiblist = win32com.client.Dispatch("CpSysDib.CssStgList")
    
    ## 전략을 가져올 Type 세팅(나의전략:ord('1')
    cpsysdiblist.SetInputValue(0, ord('1'))  # '0' : 예제전략, '1': 나의전략
    
    ##Block모드로 
    cpsysdiblist.BlockRequest()
    
    ##불러오기
    count = cpsysdiblist.GetHeaderValue(0)    #0 : (long) 전략목록수
    flag =  cpsysdiblist.GetHeaderValue(1)    #1 : (char) 요청구분
    
    st_items = {}
    strategy_id = ''
    for i in range(count):    
        st_items['전략명'] = cpsysdiblist.GetDataValue(0,i);
        st_items['전략ID'] = cpsysdiblist.GetDataValue(1,i);
        #전략 찾아서 해당전략 ID를 가져옴
        if(st_items['전략명']==u'매집후거래상승'):
            strategy_id = st_items['전략ID']
    #print(strategy_id)
    
    
    
    '''
    2 전략 검색종목 가져오기
    '''
    ## 8357 종목검색Master 전략조회 Object
    cpsysdibfind = win32com.client.Dispatch("CpSysDib.CssStgFind")
    
    #매집후 거래상승 ID 요청
    cpsysdibfind.SetInputValue(0,strategy_id) 
    cpsysdibfind.BlockRequest()
    
    #검색된 결과 종목 수
    cnt = cpsysdibfind.GetHeaderValue(0)
    
    # 총 검색 종목 수
    totcnt = cpsysdibfind.GetHeaderValue(1)
    
    # 종목코드(종목명) 가져오기용 Object
    instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
    
    item_list = []
    for i in range(cnt):
        item={}
        #종목코드
        item['code'] = cpsysdibfind.GetDataValue(0,i)
        item['종목명'] = instCpStockCode.CodeToName(item['code'])
        item_list.append(item)
        
    #추출된 종목 보기
    #print(item_list)
    '''
    3. 종목 현재가 가져오기 
    '''
    # 주식 종목 현재가 가져오기용 Object
    now_price = win32com.client.Dispatch("Dscbo1.StockMst")
    
    # 매매 입체분석(투자주체별 현황) -> 수급조회용
    supplydemand = win32com.client.Dispatch("CpSysDib.CpSvr7254")
    
    
    # 마켓아이 -> 체결강도
    marketeye = win32com.client.Dispatch("CpSysDib.MarketEye")
    
    stocklist = []
    
    
    for i in range(len(item_list)):
        #print(item_list[i])
        #print(item_list[i]['code'])
        astock = {}
        
        
        ## 현재가 조회 
        now_price.SetInputValue(0,item_list[i]['code'])
        now_price.BlockRequest()
        
        ## 수급현황 조회 ##
        supplydemand.SetInputValue(0,item_list[i]['code'])  # 종목코드
        supplydemand.SetInputValue(1,6) # 일자별 조회
        supplydemand.SetInputValue(4,ord('0')) #순매수량 (1:매매비중) 
        supplydemand.SetInputValue(5,0) #전체투자자 조회
        supplydemand.SetInputValue(6,ord('1')) # 순매수량
        supplydemand.BlockRequest()
        
        stockcode = item_list[i]['code']
        stockcode = stockcode[1:len(stockcode)]
        stockname = item_list[i]['종목명']
        stockprice = now_price.GetHeaderValue(11)
        organ = supplydemand.GetDataValue(3,0)  #기관
        foriegner = supplydemand.GetDataValue(2,0)  #외국인
        
        astock['종목코드']=stockcode
        print stockcode
        astock['종목명']=stockname
        print stockname
        astock['현재가']=stockprice
        print stockprice
        
        #print('종목코드 : ', now_price.GetHeaderValue(0), ' | 종목명 : ' , item_list[i]['종목명'], ' | 현재가 : ', now_price.GetHeaderValue(11), ' | 전일대비 : ',now_price.GetHeaderValue(12) )
        #print('기관  : ', supplydemand.GetDataValue(3,0), '외국인  : ', supplydemand.GetDataValue(2,0), '개인  : ', supplydemand.GetDataValue(1,0))
        
        ## 마켓아이 종목정보 조회 ##
        
        # 10(거래량) , 24(체결강도),67(PER),  96(분기BPS), 110(분기부채비율), 116(프로그램순매수), 117(잠정외국인), 119(잠정기관)
        marketeye.SetInputValue(0, [10, 24, 67, 96, 110, 116, 117, 119 ])
        marketeye.SetInputValue(1, item_list[i]['code'])
        marketeye.Blockrequest()
        
        ## 마켓아이 
        # 종목 리턴 갯수
        #cnt = marketeye.GetHeaderValue(2)
        
        volume = marketeye.GetDataValue(0,0) # 거래량
        power = round(marketeye.GetDataValue(1,0),2) # 체결강도
        per = round(marketeye.GetDataValue(2,0),2) # PER
        bps = marketeye.GetDataValue(3,0) # 분기BPS
        
        if(bps == 0):
            pbr = 0.0
        else:
            pbr = round(now_price.GetHeaderValue(11)/bps,2) #PBR
        
        debt_rate = round(marketeye.GetDataValue(4,0),2) # 분기부채비율
        program_buy = marketeye.GetDataValue(5,0) # 프로그램 
        
        print ('거래량 : ', volume, '  |  체결강도 : ', power, '  |  PER : ', per, '  |  PBR : ', pbr) 
        print ('분기부채비율 : ', debt_rate, '  |  프로그램 : ', program_buy) 
        print ('-----')
        
        ### 최근 6개월 종목리포트 조회
        stock_pre_consen_list = GetStockListfromHK.getPreStockConsenFromHK(stockcode) 
        print(stock_pre_consen_list)
        
        stocklist.append(astock)
        
        
    return stocklist
        