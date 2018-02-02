#-*- coding: utf-8 -*-

'''
Created on 2017. 12. 22.

@author: 073860
'''

from datetime import datetime
#from operator import eq
from ELS import GetElsXML
import xml.etree.ElementTree as ET
#from astropy.units import one
#from collections import namedtuple
#from _ast import Continue
#print(GetElsXML.get_current_els_xml())

def elsparser():
    elsxmldata = GetElsXML.get_current_els_xml()
    
    #debug XML DATA
    #print(elsxmldata)
    
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
                salecompany = oneels.find('val4')          
                if salecompany is not None:    
                    els_dic['salecompany']=salecompany.text
                    #if salecompany.text=='한국투자증권'.encode('UTF-8'):
                    #    els_dic['ELSNAME']=salecompany.text,' ',elsname.text
                                                
                #    
                asset = oneels.find('val8')
                if asset.text is not None:
                    els_dic['asset']=asset.text.replace('<br/>',', ')
                else:
                    els_dic['asset']=''
                #
                startdate = oneels.find('val26')
                if startdate is not None:
                    els_dic['startdate']=startdate.text
                #
                enddate = oneels.find('val14')
                if enddate is not None:
                    els_dic['enddate']=enddate.text
                #
                sale_s_date = oneels.find('val16')
                if sale_s_date is not None:
                    els_dic['sale_s_date']=sale_s_date.text
                #
                sale_e_date = oneels.find('val17')
                if sale_e_date is not None:
                    els_dic['sale_e_date']=sale_e_date.text
                #
                elsrate = oneels.find('val15')
                if elsrate is not None:
                    els_dic['elsrate']=elsrate.text
                #
                elstruct = oneels.find('val18')
                if elstruct is not None:
                    els_dic['elstruct']=elstruct.text
                #
                sitelink = oneels.find('val20')
                if sitelink is not None:
                    els_dic['sitelink']=sitelink.text
                #
                elsnote = oneels.find('val21')
                if elsnote is not None:
                    els_dic['elsnote']=elsnote.text    
                                                
                els_dic_list.append(els_dic)
                i=i+1
    
    return els_dic_list
#print els_dic_list

def debug_els_dic(els_dic_list):
    print datetime.today().strftime('%Y.%m.%d'),' 청약중  ELS 목록'
    print '총 갯수 : ', len(els_dic_list)
    
    for elsdic in els_dic_list:
        print '-----------------------------------'
        print '상품명 : ',elsdic['ELSNAME']
        print '판매사 : ',elsdic['salecompany']
        print '기초자산 : ',elsdic['asset']
        print '발행일 : ',elsdic['startdate']," , ",'만기일 : ',elsdic['enddate']
        print '청약시작일: ',elsdic['sale_s_date']," , ",'청약종료일 : ',elsdic['sale_e_date']
        print '이자율 : ',elsdic['elsrate'],'%'
        print '구조 : ',elsdic['elstruct']
        print 'link : ',elsdic['sitelink']
        
        if elsdic['elsnote'] is not None:
            print '비고 : ',elsdic['elsnote']
        else:
            print '비고: '
        
