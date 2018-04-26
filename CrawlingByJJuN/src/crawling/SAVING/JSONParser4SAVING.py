#-*- coding: utf-8 -*-

'''
Created on 2018. 1. 31.

@author: 073860
'''

from SAVING import GetSavingJSON
import json
import pprint

def savingparser(finkind,svkind,sortcode):
    
    #finkind = 은행, 저축은행
    #svkind = 예금, 적금   
    #sortcode = 1 : 우대금리포함
    #sortcode = 2 : 우대금리미포함
    
    
    if sortcode is None:
        sortcode = 1
    #TOP 몇개
    rank_count = 10 
    
    #savingjson = GetSavingJSON.get_current_saving_json('은행','예금')
    savingjson = GetSavingJSON.get_current_saving_json(finkind,svkind)
    
    result_dic = json.loads(savingjson)
    list_dic = result_dic['result']
       
    '''
    product_dic : 상품정보
    fin_cmpy_dic : 판매 금융기관 정보
    '''
    product_dic_list = list_dic['optionList']
    fin_cmpy_dic_list = list_dic['baseList']
    #pprint.pprint(baselist_dic)
    #pprint.pprint(product_dic)
    #print "#################"
    
    m12_product_list = []
    
    for _12m_produc in product_dic_list:
        if _12m_produc['save_trm'] == u'12':
            m12_product_list.append(_12m_produc)
        
    #m12_product_list.sort(cmp=None, key=None, reverse=False)    
    
    if sortcode == 1:
        m12_product_list_r2sorted = sorted(m12_product_list, key=lambda k: k['intr_rate2'], reverse=True)
    else:
        m12_product_list_r2sorted = sorted(m12_product_list, key=lambda k: k['intr_rate'], reverse=True)
        
    top5 = 1
    
    top5_result_dic_list= []
        
    for m12_product in m12_product_list_r2sorted:
        
        #print m12_product['fin_co_no']
        for fin_cmpy in fin_cmpy_dic_list:
            if ((m12_product['fin_co_no'] == fin_cmpy['fin_co_no']) and (m12_product['fin_prdt_cd'] == fin_cmpy['fin_prdt_cd'])):
                m12_product['fin_compy_name'] = fin_cmpy['kor_co_nm']
                m12_product['product_name'] = fin_cmpy['fin_prdt_nm'].replace('\n',' ')
                m12_product['spcl_cnd'] = fin_cmpy['spcl_cnd']         
        #print m12_product['fin_prdt_cd']
        #print m12_product['intr_rate']
        #print m12_product['intr_rate2']
        #print m12_product['intr_rate_type_nm']
        #print m12_product['save_trm']
        #print '------------'
        
        top5=top5+1
        top5_result_dic_list.append(m12_product)
        
        if top5 > rank_count:
            break
    
    
    return top5_result_dic_list

    #for debug
    for top5_result_dic in top5_result_dic_list:
        #금융기관
        print top5_result_dic['fin_compy_name']
        #상품이름 
        print top5_result_dic['product_name']
        #기본금리
        print top5_result_dic['intr_rate']
        #우대금리
        print top5_result_dic['intr_rate2']
        #단리/복리
        print top5_result_dic['intr_rate_type_nm']
        #우대조건
        print top5_result_dic['spcl_cnd']
        print '------------'
    


    
    
    
    
    

    