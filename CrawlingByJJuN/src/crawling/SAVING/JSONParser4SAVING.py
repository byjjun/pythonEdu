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
    
    pprint.pprint(baselist_dic)
    
    
    
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
    

    