#-*- coding: utf-8 -*-

'''
Created on 2018. 1. 31.

@author: 073860
'''

from SAVING import GetSavingJSON
import json
import pprint

def savingparser():
    
    savingjson = GetSavingJSON.get_current_saving_json()
    
    result_dic = json.loads(savingjson)
    baselist_dic = result_dic['result']
    #pprint.pprint(baselist_dic)
    
    product_dic = baselist_dic['optionList']
        
    #pprint.pprint(product_dic)
    m12_product_list = []
    
    for _12m_produc in product_dic:
        if _12m_produc['save_trm'] == u'12':
            m12_product_list.append(_12m_produc)
        
    m12_product_list.sort(cmp=None, key=None, reverse=False)    
    
    m12_product_list_r2sorted = sorted(m12_product_list, key=lambda k: k['intr_rate2'], reverse=True)
    for m12_product in m12_product_list_r2sorted:
        print m12_product['fin_co_no']
        print m12_product['fin_prdt_cd']
        print m12_product['intr_rate']
        print m12_product['intr_rate2']
        print m12_product['intr_rate_type_nm']
        print m12_product['save_trm']
        print '----------'
    
     
        
    
    
    
    
    '''
    for _result in tree.findall('result'):
        
        if _result.findall('err_code').text !='000':
            print "ERROR : Cannot get a xml file" 
            break
        
        saving_dic = {}
        
        for _product in _result.findall('products'):
            for baseinfo in _product.findall('baseinfo'):
                saving_dic['FINNAME'] = baseinfo.findall('kor_co_nm').text
            
            
            
        print '은행이름 : ',saving_dic['FINNAME']
    '''
        

savingparser()
    

    