#-*- coding: utf-8 -*-

'''
Created on 2018. 2. 6.

@author: 073860
'''

from datetime import datetime

def makesavinghello():
    str_hello = \
    datetime.today().strftime('%Y년 %m월 %d일 '),'기준  예금금리  Top 5 입니다.' \
    "자세한 목록은 아래를 참조해 주세요." \
    "<br/>" 
    return str_hello


def makeproduchtml(topsaving_list):        
    for top_product in topsaving_list:
        #print "<hr />"
        print "<table style=\"height: 91px;\" width=\"475\">"
        print "<tbody>"
        print "<tr>"
        print "<td style=\"width: 120px; background-color: #d7d6a5;\" colspan=\"2\">",top_product['fin_compy_name'],"</td>"
        print "<td style=\"width: 220px; background-color: #f2ede4;\" colspan=\"3\">",top_product['product_name'],"</td>"
        print "</tr>"
        print "<tr>"
        print "<td style=\"width: 60px; background-color: #c4e7e7;\">일반금리</td>"
        print "<td style=\"width: 60px; background-color: #dba67b;\">",top_product['intr_rate'],"%</td>"
        print "<td style=\"width: 80px; background-color: #c4e7e7;\">우대금리</td>"
        print "<td style=\"width: 60px; background-color: #dba67b;\">",top_product['intr_rate2'],"%</td>"
        print "<td style=\"width: 60px; background-color: #f2ede4;\">",top_product['intr_rate_type_nm'],"</td>"
        print "</tr>"
        print "<tr>"
        print "<td style=\"width: 440px; background-color: #f2ede4;\" colspan=\"5\">",top_product['spcl_cnd'],"</td>"
        print "</tr>"
        print "</tbody>"
        print "</table>"
        

def make_str_produchtml(topsaving_list):        
    str_savhtml = ''
    for top_product in topsaving_list:
        str_savhtml += \
        "<table style=\"height: 91px;\" width=\"475\">" \
        "<tbody>" \
        "<tr>" \
        "<td style=\"width: 120px; background-color: #d7d6a5;\" colspan=\"2\">"+top_product['fin_compy_name'].encode('UTF-8')+"</td>" \
        "<td style=\"width: 220px; background-color: #f2ede4;\" colspan=\"3\">"+top_product['product_name'].encode('UTF-8')+"</td>" \
        "</tr>" \
        "<tr>" \
        "<td style=\"width: 60px; background-color: #c4e7e7;\">일반금리</td>" \
        "<td style=\"width: 60px; background-color: #dba67b;\">"+str(top_product['intr_rate'])+"%</td>" \
        "<td style=\"width: 80px; background-color: #c4e7e7;\">우대금리</td>" \
        "<td style=\"width: 60px; background-color: #dba67b;\">"+str(top_product['intr_rate2'])+"%</td>" \
        "<td style=\"width: 60px; background-color: #f2ede4;\">"+top_product['intr_rate_type_nm'].encode('UTF-8')+"</td>" \
        "</tr>" \
        "<tr>" \
        "<td style=\"width: 440px; background-color: #f2ede4;\" colspan=\"5\">" + top_product['spcl_cnd'].encode('UTF-8') + "</td>" \
        "</tr>" \
        "</tbody>" \
        "</table>" 
    return str_savhtml