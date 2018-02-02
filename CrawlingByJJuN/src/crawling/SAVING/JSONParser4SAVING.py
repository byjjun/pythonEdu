#-*- coding: utf-8 -*-

'''
Created on 2018. 1. 31.

@author: 073860
'''

from SAVING import GetSavingXML
import xml.etree.ElementTree as ET

def savingparser():
    
    savingxml = GetSavingXML.get_current_saving_xml()
    
    print "####"
    print savingxml
    
    tree = ET.fromstring(savingxml)
    
    
    for _result in tree.findall('result'):
        
        if _result.findall('err_code').text !='000':
            print "ERROR : Cannot get a xml file" 
            break
        
        saving_dic = {}
        
        for _product in _result.findall('products'):
            for baseinfo in _product.findall('baseinfo'):
                saving_dic['FINNAME'] = baseinfo.findall('kor_co_nm').text
            
            
            
        print '은행이름 : ',saving_dic['FINNAME']
            
        

savingparser()
    
'''
tree = ET.fromstring(elsxmldata)
    
    i=1
            
    els_dic_list = []
    
    for message in tree.findall('message'):
        for elslist in message.findall('DISDlsListDTO'):
            totalcount = elslist.find('dbio_total_count_')
            
            #if totalcount is not None:
                #print "총 개수: ",totalcount.text   
                
            for oneels in elslist.findall('DISDlsDTO'):
                #print("aaa")
                #print(i)
                #print(oneels)
                
                #Except ELS
                nowdate = datetime.today().strftime("%Y%m%d")
                if nowdate >= oneels.find('val26').text:
                    #print "X ELS"
                    continue
                                
                els_dic = {}
                # ELS
                elsname = oneels.find('val6')
                if elsname is not None:    
                    els_dic['ELSNAME']=elsname.text
                #
'''
    