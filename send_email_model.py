# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/18 14:24
@Author  : hejipei
"""

import os
import sys
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import make_header
from cl_api.output_excel_deal import deal_excel_pd_data
from cl_api.html_msg_model import get_data_html

send_msgs = {
            "log": {  # 登录信息
                "fromaddr": "",
                "smtpaddr": "",
                "password": ""
            },
            "address": {  # 收件人 抄送人
                "toaddrs": ["zhangsan@163.com"],
                "ccaddrs": []
            }, # 发送类型
            "msg_type": {
                "msg_txt": 1,
                "msg_excel": 0,
                "msg_html_table": 0,
                "msg_html_n":20
            },
            "data_text": {  # 主题 正文 附件名称 excel导出路径 发送数据
                "subject": "",
                "main_txt": "",
                "path": "",
                "file": "",
            },
            "date_interval":{
                "start_date":"",
                "end_date":""
            },
            "send_date":{
                "excel_data":"",
                "sheet_name":""
            }
        }

def send_email(send_msgs):

    start_date = send_msgs['date_interval']['start_date']
    end_date = send_msgs['date_interval']['end_date']
    now_date = datetime.datetime.now().strftime('%Y-%m-%d')
    if not start_date or not end_date:
        print('***请配置输入发送邮件的start_date和end_date***')
        sys.exit()
        print('已退出程序')
    elif end_date < start_date:
        print('***请确保end_date不小于end_date***')
        sys.exit()
        print('已退出程序')
    elif start_date <= now_date and end_date > now_date:
        pass
    else:
        print('***当前日期不再发送范围日期区间内***')
        sys.exit()
        print('已退出程序')

    subject = send_msgs['data_text']['subject']
    fromaddr = send_msgs['log']['fromaddr']
    smtpaddr = send_msgs['log']['smtpaddr']
    password = send_msgs['log']['password']
    toaddrs = send_msgs['address']['toaddrs']
    ccaddrs = send_msgs['address']['ccaddrs']

    mail_msg = MIMEMultipart()
    mail_msg['Subject'] = subject
    mail_msg['From'] = fromaddr
    mail_msg['To'] = ','.join(toaddrs)
    if ccaddrs:
        mail_msg['CC'] = ','.join(ccaddrs)
    # 添加文本信息
    if send_msgs['msg_type']['msg_txt']:
        msg_str = send_msgs['data_text']['main_txt']
        mail_msg.attach(MIMEText(msg_str, 'html', 'utf-8'))
    # 添加html表格
    if send_msgs['msg_type']['msg_html_table']:
        htmel_date  = send_msgs['send_date']['excel_data']
        html_suject = send_msgs['send_date']['sheet_name']
        num = send_msgs['msg_type']['msg_html_n']
        msg_html_str = get_data_html(htmel_date,html_suject,n=num)
        mail_msg.attach(MIMEText(msg_html_str, 'html', 'utf-8'))
    # 添加附件excel表格
    if send_msgs['msg_type']['msg_excel']:
        excel_date = send_msgs['send_date']['excel_data']
        path_file = os.path.join(send_msgs["data_text"]["path"], send_msgs["data_text"]["file"])
        deal_excel_pd_data(excel_date, path_file,Sheet_name = send_msgs['send_date']['sheet_name'])
        file = send_msgs['data_text']['file']
        with open(path_file, 'rb') as f:
            file_msg = MIMEText(f.read(), 'base64', 'UTF-8')
            file_msg["Content-Type"] = 'application/octet-stream;name="%s"' % make_header([(file, 'UTF-8')]).encode('UTF-8')
            file_msg["Content-Disposition"] = 'attachment;filename= "%s"' % make_header([(file, 'UTF-8')]).encode('UTF-8')
            mail_msg.attach(file_msg)
    try:
        # 登陆和发送信息
        s = smtplib.SMTP()
        s.connect(smtpaddr)  # 连接smtp服务器
        s.login(fromaddr, password)  # 登录邮箱
        s.sendmail(fromaddr, toaddrs + ccaddrs, mail_msg.as_string())  # 发送邮件
        s.quit()
        print('邮件发送成功，请查收邮箱。')
    except Exception as e:
        print("Error: unable to send email")

