#-*- coding: utf-8 -*-

'''
Created on 2018. 1. 25.

@author: 073860
'''
from datetime import datetime

def makeelshtml(els_dic_list, totalcount):
    
    '''
        for elsdic in els_dic_list:
        print '-----------------------------------'
        print '��ǰ�� : ',elsdic['ELSNAME']
        print '�ǸŻ� : ',elsdic['salecompany']
        print '�����ڻ� : ',elsdic['asset']
        print '������ : ',elsdic['startdate']," , ",'������ : ',elsdic['enddate']
        print 'û�������: ',elsdic['sale_s_date']," , ",'û�������� : ',elsdic['sale_e_date']
        print '������ : ',elsdic['elsrate'],'%'
        print '���� : ',elsdic['elstruct']
        print 'link : ',elsdic['sitelink']
        
        if elsdic['elsnote'] is not None:
            print '��� : ',elsdic['elsnote']
        else:
            print '���: '
    
    '''
    
    #print datetime.today().strftime('%Y.%m.%d'),' 청약중  ELS 목록'
    
    #print datetime.today().strftime('%Y'),'년',datetime.today().strftime('%m'),'월',datetime.today().strftime('%d'),'일'
    
    
    print datetime.today().strftime('%Y년 %m월 %d일 '),'기준 '
    print "청약 가능한 ELS로 총 ",totalcount,"개가 검색되었습니다."
    print "자세한 목록은 아래를 참조해 주세요."
    print "<br/>"
    print "금융투자협희 공시정보를 사용하였으며, 투자추천이나 권유는 아닙니다."
    print "각 상품의 자세한 정보는 상세정보를 통하여 각 판매사 사이트를 참조해 주시기 바랍니다."
    print "<br/>"
    
    for elsdic in els_dic_list:
        
        print "<hr />"
        print "<table style=\"height: 91px;\" width=\"475\">"
        print "<tbody>"
        print "<tr style=\"height: 29px;\">"
        print "<td style=\"width: 343px; height: 29px; background-color: #d7d6a5;\" colspan=\"3\">",elsdic['ELSNAME'],"</td>"
        print "<td style=\"width: 116px; height: 29px; background-color: #dba67b;\">",elsdic['elsrate'],"% </td>"
        print "</tr>"
        print "<tr style=\"height: 29px;\">"
        print "<td style=\"width: 109px; height: 29px; background-color: #c4e7e7;\">판매종료</td>"
        print "<td style=\"width: 114px; height: 29px; background-color: #f2ede4;\">",elsdic['sale_e_date'],"</td>"
        print "<td style=\"width: 108px; height: 29px; background-color: #c4e7e7;\">만기일</td>"
        print "<td style=\"width: 116px; height: 29px; background-color: #f2ede4;\">",elsdic['enddate'],"</td>"
        print "</tr>"
        print "<tr style=\"height: 30px;\">"
        print "<td style=\"width: 109px; height: 30px; background-color: #c4e7e7;\">기초자산</td>"
        print "<td style=\"width: 350px; height: 30px; background-color: #f2ede4;\" colspan=\"3\">",elsdic['asset'],"</td>"
        print "</tr>"        
        print "<tr style=\"height: 30px;\">"
        print "<td style=\"width: 109px; height: 30px; background-color: #c4e7e7;\">ELS구조</td>"
        print "<td style=\"width: 350px; height: 30px; background-color: #f2ede4;\" colspan=\"3\">",elsdic['elstruct'],"</td>"
        print "</tr>"
        print "<tr style=\"height: 30px;\">"
        print "<td style=\"width: 109px; height: 30px; background-color: #c4e7e7;\"><a href=\"",elsdic['sitelink'],"\" target=\"_blank\" rel=\"noopener\">상세정보(Click)</a></td>"
        print "<td style=\"width: 350px; height: 30px; background-color: #f2ede4;\" colspan=\"3\">",elsdic['elsnote'],"</td>"
        print "</tr>"       
        print "</tbody>"
        print "</table>"
    
    
def make_str_elshtml(els_dic_list, totalcount):
    
    
    
    str_elshtml = datetime.today().strftime('%Y년 %m월 %d일 ')+'기준 ' \
    "청약 가능한 ELS로 총 "+totalcount+"개가 검색되었습니다." \
    "<br>자세한 목록은 아래를 참조해 주세요."\
    "<br>*투자추천이나 권유가 아닙니다."\
    "<br>각 상품의 자세한 정보는 상세정보를 통하여 각 판매사 사이트를 참조해 주시기 바랍니다."\
    "<br/>"
    
    for elsdic in els_dic_list:
        
        if elsdic['sitelink'] is None:
            elsdic['sitelink'] = ' '
        
        str_elshtml += \
        "<hr />"\
        "<table style=\"height: 91px;\" width=\"475\">"\
        "<tbody>"\
        "<tr style=\"height: 29px;\">"\
        "<td style=\"width: 343px; height: 29px; background-color: #d7d6a5;\" colspan=\"3\">"+elsdic['ELSNAME'].encode('UTF-8')+"</td>"\
        "<td style=\"width: 116px; height: 29px; background-color: #dba67b;\">"+elsdic['elsrate'].encode('UTF-8')+"% </td>"\
        "</tr>"\
        "<tr style=\"height: 29px;\">"\
        "<td style=\"width: 109px; height: 29px; background-color: #c4e7e7;\">판매종료</td>"\
        "<td style=\"width: 114px; height: 29px; background-color: #f2ede4;\">"+elsdic['sale_e_date'].encode('UTF-8')+"</td>"\
        "<td style=\"width: 108px; height: 29px; background-color: #c4e7e7;\">만기일</td>"\
        "<td style=\"width: 116px; height: 29px; background-color: #f2ede4;\">"+elsdic['enddate'].encode('UTF-8')+"</td>"\
        "</tr>"\
        "<tr style=\"height: 30px;\">"\
        "<td style=\"width: 109px; height: 30px; background-color: #c4e7e7;\">기초자산</td>"\
        "<td style=\"width: 350px; height: 30px; background-color: #f2ede4;\" colspan=\"3\">"+elsdic['asset'].encode('UTF-8')+"</td>"\
        "</tr>"\
        "<tr style=\"height: 30px;\">"\
        "<td style=\"width: 109px; height: 30px; background-color: #c4e7e7;\">ELS구조</td>"\
        "<td style=\"width: 350px; height: 30px; background-color: #f2ede4;\" colspan=\"3\">"+elsdic['elstruct'].encode('UTF-8')+"</td>"\
        "</tr>"\
        "<tr style=\"height: 30px;\">"\
        "<td style=\"width: 109px; height: 30px; background-color: #c4e7e7;\"><a href=\""+elsdic['sitelink'].encode('UTF-8')+"\" target=\"_blank\" rel=\"noopener\">상세정보(Click)</a></td>"\
        "<td style=\"width: 350px; height: 30px; background-color: #f2ede4;\" colspan=\"3\">"+elsdic['elsnote'].encode('UTF-8')+"</td>"\
        "</tr>"\
        "</tbody>"\
        "</table>"
    
        #print "-------"
        #print str_elshtml
        #print "-------"
        
    return str_elshtml