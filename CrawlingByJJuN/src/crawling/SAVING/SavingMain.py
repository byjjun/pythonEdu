#-*- coding: utf-8 -*-
'''
Created on 2018. 2. 6.

@author: 073860
'''
from datetime import datetime
from SAVING import MakeSAVINGHtml
from SAVING import JSONParser4SAVING

if __name__ == '__main__':
    pass

def str_saving():
    
    #은행
    #정기예금 - 우대포함
    str_return = datetime.today().strftime('%Y년 %m월 %d일 ')+'기준'  
    str_return += '은행 / 저축은행 정기예금  Top 10.'
    str_return +=  "<br/>"
    str_return +=  "<hr/>"
    str_return +=  "은행  12개월 정기예금    금리비교 - 우대금리 Top 10"
    str_return +=  "<br/>"
    topsaving_list=JSONParser4SAVING.savingparser('은행', '예금', 1)
    str_return += MakeSAVINGHtml.make_str_produchtml(topsaving_list)
    
    #정기예금 - 우대 비포함
    str_return +=  "<hr/>"
    str_return +=  "은행  12개월 정기예금   금리비교 - 단순금리  Top 10"
    str_return +=  "<br/>"
    topsaving_list=JSONParser4SAVING.savingparser('은행', '예금', 2)
    str_return += MakeSAVINGHtml.make_str_produchtml(topsaving_list)
    
    #저축은행
    #정기예금 - 우대포함
    str_return +=  "<hr/>"
    str_return +=  "저축은행 12개월 정기예금   금리비교 - 우대금리 Top 10"
    str_return +=  "<br/>"
    topsaving_list=JSONParser4SAVING.savingparser('저축은행', '예금', 1)
    str_return += MakeSAVINGHtml.make_str_produchtml(topsaving_list)
    #정기예금 - 우대비포함
    str_return +=  "<hr/>"
    str_return +=  "저축은행 12개월 정기예금   금리비교- 일반금리 Top 10"
    str_return +=  "<br/>"
    topsaving_list=JSONParser4SAVING.savingparser('저축은행', '예금', 2)
    str_return += MakeSAVINGHtml.make_str_produchtml(topsaving_list)
    
    return str_return


def str_inssaving():
     #은행
    #정기적금 - 우대포함
    str_return =  datetime.today().strftime('%Y년 %m월 %d일 ')+'기준  적금금리  Top 10 입니다.'
    str_return +=  "<br/>"
    str_return +=  "<hr/>"
    str_return +=  "은행  12개월 정기적금  금리비교 - 우대금리 Top 10"
    str_return +=  "<br/>"
    topsaving_list=JSONParser4SAVING.savingparser('은행', '적금', 1)
    str_return += MakeSAVINGHtml.make_str_produchtml(topsaving_list)
    #정기적금 - 우대 비포함
    str_return +=  "<hr/>"
    str_return +=  "은행  12개월 정기적금   금리비교 - 단순금리  Top 10"
    str_return +=  "<br/>"
    topsaving_list=JSONParser4SAVING.savingparser('은행', '적금', 2)
    str_return += MakeSAVINGHtml.make_str_produchtml(topsaving_list)
    
    #저축은행
    #정기적금 - 우대포함
    str_return +=  "<hr/>"
    str_return +=  "저축은행 12개월 정기적금   금리비교 - 우대금리 Top 10"
    str_return +=  "<br/>"
    topsaving_list=JSONParser4SAVING.savingparser('저축은행', '적금', 1)
    str_return += MakeSAVINGHtml.make_str_produchtml(topsaving_list)
    #정기적금 - 우대비포함
    str_return +=  "<hr/>"
    str_return +=  "저축은행 12개월 정기적금   금리비교 - 일반금리 Top 10"
    str_return +=  "<br/>"
    topsaving_list=JSONParser4SAVING.savingparser('저축은행', '적금', 2)
    str_return += MakeSAVINGHtml.make_str_produchtml(topsaving_list)
    return str_return

#print str_saving()
#print str_inssaving()
