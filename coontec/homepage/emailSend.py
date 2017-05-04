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
    
    #try:
    send_email = EMAIL['id'] + '@coontec.com'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()

    server.login(send_email, EMAIL['password'])

    body = MIMEMultipart()
    body['subject'] = '홈페이지 문의 사항 입니다.'
    body['From'] = send_email
    body['To'] = send_email
    
    html = '<div align="center" style="width: 100%;">'
    html += '<table style="background-color: rgb(255, 255, 255); width: 500px; font-size: 9pt;"><tbody>'
    html += '<tr style="height: 2px;"><td colspan="3" style="background: rgb(0, 136, 178); height: 2px;"></td></tr>'
    html += '<tr style="height: 40px;"><td colspan="3" style="background: rgb(241, 241, 241);"><b>&nbsp;안녕하세요 쿤텍(주) 입니다.&nbsp <br>&nbsp;보내주신 문의사항은 다음과 같습니다.</b></td></tr>'
    html += '<tr style="height: 2px;"><td colspan="3" style="background: rgb(217, 217, 217); height: 2px;"></td></tr>'
    html += '<tr style="height: 31px;"><td style="width: 200px;"><b>&nbsp;이름 ( Name )</b></td><td>|</td><td>&nbsp;' + request.GET['name'] + '</td></tr>'
    html += '<tr style="height: 1px;"><td colspan="3" style="background: rgb(217, 217, 217); height: 1px;"></td></tr>'
    html += '<tr style="height: 32px;"><td><b>&nbsp;메일 ( E- mail )</b></td><td>|</td><td>&nbsp;' + request.GET['email'] + '</td></tr>'
    html += '<tr style="height: 1px;"><td colspan="3" style="background: rgb(217, 217, 217); height: 1px;"></td></tr>'
    html += '<tr style="height: 32px;"><td><b>&nbsp;제목&nbsp;(Subject ) </b></td><td>|</td><td>&nbsp;' + request.GET['name'] + '</td></tr>'
    html += '<tr style="height: 1px;"><td colspan="3" style="background: rgb(217, 217, 217); height: 1px;"></td></tr>'
    html += '<tr style="height: 32px;"><td colspan="3"><b>&nbsp;내용 ( Message )</b></td></tr>'
    html += '<tr style="height: 1px;"><td colspan="3" style="background: rgb(217, 217, 217); height: 1px;"></td></tr>'
    html += '<tr style="height: 50px;"><td colspan="3" style="height: 50px;">&nbsp;' + request.GET['message'] + '</td></tr>'
    html += '<tr style="height: 2px;"><td colspan="3" style="background: rgb(0, 136, 178); height: 2px;"></td></tr>'
    html += '</tbody></table></div>'
    
    msg = MIMEText(html, 'html')
    body.attach(msg)

    server.sendmail(from_addr=send_email,
                    to_addrs=[request.GET['email'], send_email],  # list, str 둘 다 가능
                    msg=body.as_string())

    server.quit()
    result_data = "success"
    print(result_data)
    #except:
    #    result_data="fail"
    
    return HttpResponse(result_data)
