# -*- coding: utf-8 -*-

'''
Created on 2018. 6. 1.

@author: 073860
'''


import requests



def get_current_loan_json(finGrpNo,svkind):

    apikey = 'c00ce82f75408d5a4d3bbe6c8db89dd2'
    
    
    if finGrpNo is None:
        grpNo = '020000'
    elif finGrpNo == '은행':
        grpNo = '020000'
    elif finGrpNo == '보험':
        grpNo = '050000'
    elif finGrpNo == '저축은행':    
        grpNo = '030300'
    elif finGrpNo == '캐피탈':    
        grpNo = '030200'
    else: 
        print 'ERROR : Unknown FinGrpNo'    
    
    if svkind is None:
        kind = 'creditLoanProductsSearch'
    #elif svkind == '주택담보대출':
    #    kind = 'mortgageLoanProductsSearch'
    #elif svkind == '전세자금대출':
    #    kind = 'rentHouseLoanProductsSearch'
    elif svkind == '개인신용대출':
        kind = 'creditLoanProductsSearch'
    else: 
        print 'ERROR : Unkown Loan kind'
        
    request_url = 'http://finlife.fss.or.kr/finlifeapi/'+kind+'.json?auth='+apikey+'&topFinGrpNo='+grpNo+'&pageNo=1'
    #print request_url
    data = requests.post(request_url).content
    #print data
    return data
    
#print get_current_loan_json('은행','개인신용대출')