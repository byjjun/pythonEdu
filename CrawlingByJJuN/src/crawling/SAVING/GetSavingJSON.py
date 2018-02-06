# -*- coding: utf-8 -*-

'''
Created on 2018. 1. 30.

@author: 073860
'''


import requests



def get_current_saving_json(finGrpNo,svkind):

    apikey = 'c00ce82f75408d5a4d3bbe6c8db89dd2'
    if finGrpNo is None:
        grpNo = '020000'
    elif finGrpNo == '은행':
        grpNo = '020000'
    elif finGrpNo == '저축은행':    
        grpNo = '030300'
    else: 
        print 'ERROR : Unknown FinGrpNo'    
    
    if svkind is None:
        kind = 'depositProductsSearch'
    elif svkind == '예금':
        kind = 'depositProductsSearch'
    elif svkind == '적금':
        kind = 'savingProductsSearch'
    else: 
        print 'ERROR : Unkown Saving kind'
        
    request_url = 'http://finlife.fss.or.kr/finlifeapi/'+kind+'.json?auth='+apikey+'&topFinGrpNo='+grpNo+'&pageNo=1'
    #print request_url
    data = requests.post(request_url).content
    #print data
    return data
    
get_current_saving_json('은행','예금')