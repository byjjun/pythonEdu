# -*- coding: utf-8 -*-

'''
Created on 2020. 6. 8.

@author: 073860
'''

import smtplib
import sys
import HtmlMaker
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def sendMailtoGmail(title,contents):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "stockchoicebyjjun@gmail.com"
    receiver_email = "stockchoicebyjjun@gmail.com"
    
    password = sys.argv[1]
    print password
    
    message=MIMEMultipart("alternative")
    message["Subject"]=title
    message["From"]=sender_email
    message["To"]=receiver_email
    
    
    html=HtmlMaker.getStylesHtml() 
    html+=contents
    
    part2 = MIMEText(html, "html")
    message.attach(part2)
    
    smtp_session = smtplib.SMTP_SSL(smtp_server,port)
    smtp_session.login(sender_email, password)
    
    smtp_session.sendmail(sender_email,receiver_email, message.as_string())
    smtp_session.quit()

