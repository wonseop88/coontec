'''
Created on 2017. 4. 24.

@author: 원섭
'''
# -*- coding: utf-8 -*-
import smtplib  
import json
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
from django.http import HttpResponse
from homepage.config import EMAIL


def send_email(request):
    
    try:
        send_email = EMAIL['id']+'@coontec.com'
    
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
    
        server.login(send_email, EMAIL['password'])
    
        body = MIMEMultipart()
        body['subject'] = '홈페이지 문의 사항 입니다.'
        body['From'] = send_email
        body['To'] = send_email
        
        html = "이름 : " + request.GET['name'] + "<br>"
        html += "Email : " + request.GET['email'] + "<br>"
        html += "제목 : " + request.GET['subject'] + "<br>"
        html += "내용 : <br><div>"+request.GET['message']+"</div>"
        
        msg = MIMEText(html, 'html')
        body.attach(msg)
    
        server.sendmail(from_addr=send_email,
                        to_addrs=[send_email],  # list, str 둘 다 가능
                        msg=body.as_string())
    
        server.quit()
        result_data="success"
    except:
        result_data="fail"
    
    return HttpResponse(result_data)
