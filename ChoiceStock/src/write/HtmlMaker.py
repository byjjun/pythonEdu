# -*- coding: utf-8 -*-

'''
Created on 2020. 5. 21.

@author: 073860
'''


from datetime import datetime
from pytz import timezone
from src.util import Preference
from src.get import GetStockListfromHK

def makeSTOCKHtml(stock_dic_list):
    
    KST=datetime.now(timezone('Asia/Seoul'))
    time_info = KST.strftime('%Y-%m-%d %H:%M')
    
    stock_html = "<span style=\"font-size: 10pt;\">금일의 상승여력 랭킹</span><br>"\
    "<span style=\"font-size: 10pt;\">"+time_info+"기준 발행된 증권사 리서치 보고서 중 목표가와 현 주가의 괴리율이  큰 기업순위입니다.</span><br>"\
    "<br/>"\
    "&nbsp;" 
    
    pre_stockconsen_html =""
    
    count = 1
    for stock_dic in stock_dic_list:
        
        stock_html += \
        "<hr style=\"border: double 1px black;\">"\
        "<span style=\"font-size: 10pt;\"><span style=\"font-size: 18pt;\"><strong><a href=\"https://finance.naver.com/item/main.nhn?code="+stock_dic['stock_code'].encode('UTF-8')+"\" target=\"_blank\">" +stock_dic['stock_name'].encode('UTF-8')+"</a></strong></span>("+stock_dic['stock_code'].encode('UTF-8')+") 현재가 : "+ stock_dic['now_price'].encode('UTF-8')+"("+stock_dic['now_updown_rate'].encode('UTF-8')+")</br>"\
        "<a href=\""+stock_dic['companyinfo_url'].encode('UTF-8')+"\">[기업]</a><a href=\""+stock_dic['report_url'].encode('UTF-8')+"\">[report]</a></span><br>"
                                     
        stock_html += "<span style=\"font-size: 10pt;\"><span style=\"font-size: 12pt;\"><strong>목표가 대비 현재가 : "+stock_dic['diff_rate'].encode('UTF-8')+"%</strong></span> (현재 "+stock_dic['now_price'].encode('UTF-8')+" / <strong>목표"+stock_dic['new_price'].encode('UTF-8')+"</strong>)</span><br>"\
        "<span style=\"font-size: 10pt;\">"+stock_dic['analyst_company'].encode('UTF-8')+"("+stock_dic['analyst_name'].encode('UTF-8')+") : "+stock_dic['update_date'].encode('UTF-8')+"</span><br>"\
        "<span style=\"font-size: 10pt;\">   - "+stock_dic['title'].encode('UTF-8')+"</span>"

        pre_stockconsen_html=makePreSTOCKHtml(stock_dic['stock_code'])
        #print "."

        count = count+1

        stock_html += pre_stockconsen_html + '<br>'
        if (count > Preference.getStockRankCount()):
            break
                
    stock_html += \
    "<br><br>"\
    "<hr style=\"border: double 1px black;\">"\
    "<span style=\"font-size: 10pt;\">증권 투자는 원금손실의 가능성에 유의하시고, 투자자 본인의 판단과 책임하에 최종 결정을 하셔야 합니다. </span><br>"\
    "<span style=\"font-size: 10pt;\">본 자료는 어떠한 경우에도 증권투자 결과에 대한 법적 책임소재의 증빙자료로 사용될 수 없습니다.</span><br>"    
    
    return stock_html


'''
최근 2달 목표주가 html로 리턴
'''
def makePreSTOCKHtml(stockcode):
    
    stock_pre_consen_list = GetStockListfromHK.getPreStockConsenFromHK(stockcode)
   
    html_str = '<span style=\"font-size: 8pt;\">'
    html_str += '<table width=\"450\">'
    #html_str += '<tr>'
    
    for astock_pre_consen in stock_pre_consen_list:
        
        
        html_str += '<tr hight=\"8\">'
        html_str += '<td>'
        html_str += astock_pre_consen['update_date'].encode('UTF-8')
        html_str += '</td><td>'
        html_str += astock_pre_consen['consen_price'].encode('UTF-8')
        html_str += '</td><td>'
        html_str += astock_pre_consen['opinion'].encode('UTF-8').lstrip('\n').rstrip()
        html_str += '</td><td>'
        html_str += astock_pre_consen['analyst_company'].encode('UTF-8')
        html_str += '</td></tr>'
    
    html_str += '</table></span>'
        
    return html_str