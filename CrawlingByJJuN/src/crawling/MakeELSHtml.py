#-*- coding: utf-8 -*-

'''
Created on 2018. 1. 25.

@author: 073860
'''

def makeelshtml(els_dic_list):
    
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
    