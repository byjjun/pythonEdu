#-*- coding: utf-8 -*-

'''
Created on 2018. 6. 7.

@author: 073860
'''
from LOAN import CreditLoanGetJSON
from LOAN import CreditLOANJSONParser


from datetime import datetime

def make_creditloan_hello():
    str_hello = ''
    str_hello += \
    str(datetime.today().strftime('%Y년 %m월 %d일 '))+'신용대출 최저금리 리스트 입니다.' \
    "<br>자세한 목록은 아래를 참조해 주세요." \
    "<br/>"\
    "<br>FundingChoice에서는 최신자료로 매일 업데이트 됩니다"\
    "<br>오늘자 정보가 아니면 "\
    "<font size=5><a href=\"http://fundingchoice.co.kr/?cat=5\">[여기]</a></font>에서 최신 비교자료를 확인하세요"\
    "<br/>"\
    "&nbsp;"
    return str_hello

def mkhtml_creditloan():
    
    bankloanlist = CreditLOANJSONParser.loanparser('은행','개인신용대출',5)
    creditloan_htmlstr = ''
    creditloan_htmlstr += '<br><font size = \"5\">[ 은행 신용대출 및 마통 최저금리 Top 5 ]</font><br>'
    for _bankloaninfo in bankloanlist:
        creditloan_htmlstr += \
        "<table>"\
        "<tr>"\
        "<th colspan=\"2\"><strong>"+_bankloaninfo['fin_compy_name'].encode('UTF-8')+"</th>"\
        "<th colspan=\"2\"><strong>"+_bankloaninfo['loan_name'].encode('UTF-8')+"</th>"\
        "</tr>"\
        "<tr>"\
        "<td colspan=\"2\"><strong>평균대출금리</td>"\
        "<td colspan=\"2\"><strong>"+str(_bankloaninfo['crdt_grad_avg']).encode('UTF-8')+"%</td>"\
        "</tr>"\
        "<tr>"\
        "<td>1~2등급</td>"\
        "<td>"+str(_bankloaninfo['crdt_grad_1']).encode('UTF-8')+"%</td>"\
        "<td>3~4등급</td>"\
        "<td>"+str(_bankloaninfo['crdt_grad_4']).encode('UTF-8')+"%</td>"\
        "</tr>"\
        "<tr>"\
        "<td>5~6등급</td>"\
        "<td>"+str(_bankloaninfo['crdt_grad_5']).encode('UTF-8')+"%</td>"\
        "<td>7~8등급</td>"\
        "<td>"+str(_bankloaninfo['crdt_grad_6']).encode('UTF-8')+"%</td>"\
        "</tr>"\
        "</table>"\
        "<hr/>"
        
    #otherloan_list = CreditLOANJSONParser.loanparser('보험','개인신용대출',3)
    #otherloan_list.append(CreditLOANJSONParser.loanparser('저축은행','개인신용대출',3))
    #otherloan_list.append(CreditLOANJSONParser.loanparser('캐피탈','개인신용대출',3))
    #otherloan_list = sorted(otherloan_list, key=lambda k: float(k['crdt_grad_avg']), reverse=False)
    
    otherloan = []
    templist = CreditLOANJSONParser.loanparser('보험','개인신용대출',3)
    for _tmp in templist:
        otherloan.append(_tmp)
        
    templist = CreditLOANJSONParser.loanparser('저축은행','개인신용대출',3)
    for _tmp in templist:
        otherloan.append(_tmp)
    
    templist = CreditLOANJSONParser.loanparser('캐피탈','개인신용대출',3)
    for _tmp in templist:
        otherloan.append(_tmp)
    otherloan_list = sorted(otherloan, key=lambda k: float(k['crdt_grad_avg']), reverse=False)
    
    creditloan_htmlstr += "&nbsp;"
    creditloan_htmlstr += '<br><font size = \"5\">[ 보험 / 저축은행 / 캐피탈 신용대출 최저금리 리스트 ]</font><br>'
    
    count = 1
    for _otherloaninfo in otherloan_list:
        
        if(count == 8):
            break
        
        creditloan_htmlstr += \
        "<table>"\
        "<tr>"\
        "<th colspan=\"2\"><strong>"+_otherloaninfo['fin_compy_name'].encode('UTF-8')+"</th>"\
        "<th colspan=\"2\"><strong>"+_otherloaninfo['loan_name'].encode('UTF-8')+"</th>"\
        "</tr>"\
        "<tr>"\
        "<td colspan=\"2\"><strong>평균대출금리</td>"\
        "<td colspan=\"2\"><strong>"+str(_otherloaninfo['crdt_grad_avg']).encode('UTF-8')+"%</td>"\
        "</tr>"\
        "<tr>"\
        "<td>1~3등급</td>"\
        "<td>"+str(_otherloaninfo['crdt_grad_1']).encode('UTF-8')+"%</td>"\
        "<td>4등급</td>"\
        "<td>"+str(_otherloaninfo['crdt_grad_4']).encode('UTF-8')+"%</td>"\
        "</tr>"\
        "<tr>"\
        "<td>5등급</td>"\
        "<td>"+str(_otherloaninfo['crdt_grad_5']).encode('UTF-8')+"%</td>"\
        "<td>6등급</td>"\
        "<td>"+str(_otherloaninfo['crdt_grad_6']).encode('UTF-8')+"%</td>"\
        "</tr>"\
        "</table>"\
        "<hr/>"
        
        count = count+1
         
    return creditloan_htmlstr
    
def creditloanmain():
    return make_creditloan_hello() + mkhtml_creditloan() 
    
#print creditloanmain()