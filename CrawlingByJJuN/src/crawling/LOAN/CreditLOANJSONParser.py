#-*- coding: utf-8 -*-

'''
Created on 2018. 1. 31.

@author: 073860
'''

from LOAN import CreditLoanGetJSON
import json
import pprint

def loanparser(finkind,svkind):
    
    #finkind = 은행, 저축은행
    #svkind = 예금, 적금   
    
    #TOP 몇개
    rank_count = 5 
    
    savingjson = CreditLoanGetJSON.get_current_loan_json(finkind,svkind)
    
    result_dic = json.loads(savingjson)
    list_dic = result_dic['result']
       
    '''
    product_dic : 상품정보
    fin_cmpy_dic : 판매 금융기관 정보
    '''
    product_dic_list = list_dic['optionList']
    fin_cmpy_dic_list = list_dic['baseList']
    
    product_list = []
    
    for creditloan in product_dic_list:
        if creditloan['crdt_lend_rate_type_nm'] == u'대출금리':
            product_list.append(creditloan)
    
    product_list_sorted = sorted(product_list, key=lambda k: float(k['crdt_grad_avg']), reverse=False)
    
    count = 1
    
    top5_result_dic_list= []
        
    for product in product_list_sorted:
        
        #print m12_product['fin_co_no']
        for fin_cmpy in fin_cmpy_dic_list:
            if ((product['fin_co_no'] == fin_cmpy['fin_co_no']) and (product['fin_prdt_cd'] == fin_cmpy['fin_prdt_cd'])):
                product['fin_compy_name'] = fin_cmpy['kor_co_nm']
                product['product_name'] = fin_cmpy['fin_prdt_nm']
                product['loan_name'] = fin_cmpy['crdt_prdt_type_nm']
        #product['spcl_cnd'] = fin_cmpy['spcl_cnd']
        #print m12_product['fin_prdt_cd']
        #print m12_product['intr_rate']
        #print m12_product['intr_rate2']
        #print m12_product['intr_rate_type_nm']
        #print m12_product['save_trm']
        #print '------------'
        
        count=count+1
        top5_result_dic_list.append(product)
        
        if count > rank_count:
            break
    
    #return top5_result_dic_list

    #for debug
    for top5_result_dic in top5_result_dic_list:
        #금융기관
        print top5_result_dic['fin_compy_name']
        #상품이름 
        print top5_result_dic['product_name']
        #대출종류
        print top5_result_dic['loan_name']
        #1-3등급
        print top5_result_dic['crdt_grad_avg']
        #1-3등급
        print top5_result_dic['crdt_grad_1']
        #1-3등급
        print top5_result_dic['crdt_grad_4']
        #1-3등급
        print top5_result_dic['crdt_grad_5']
        #1-3등
        print top5_result_dic['crdt_grad_6']
        #1-3등
        print top5_result_dic['crdt_grad_10']
        print '------------'
    
loanparser('저축은행','개인신용대출')


    
    

    