# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/26 11:44
@Author  : hejipei
"""
import platform
import pandas as pd
from cl_api.send_email_model import send_email
from cl_api.send_email_model import send_msgs
import warnings
warnings.filterwarnings("ignore")

mac_path = '/Users/hejipei/PycharmProjects/CL_project/cl_api/py_email/output'

data = {'指标1': [i for i in range(10000,10100)],
        '指标2字段比较长': [ i+0.1234 for i in range(1000,1100)],
        '指标3': ['abcdefg' for  i in range(1000,1100)],
        '指标4字段非常比较长': ['a这是一个测试，文本内容' for  i in range(1000,1100)],
        '指标5': ['2025-01-01'for i in range(1000,1100)]
        }
if __name__ == '__main__':
    # 获取数据
    df = pd.DataFrame(data)
    # 配置邮箱信息
    send_msgs['log']['fromaddr'] = "youreamil@163.com"
    send_msgs['log']['smtpaddr'] = "smtp.163.com"
    send_msgs['log']['password'] = "123456"

    print('=====测试发送=====')
    send_msgs['address']['toaddrs'] = ["send_email@163.com"]  # 格式为列表
    send_msgs['address']['ccaddrs'] = ["cc_email@163.com"]  # 格式为列表


    send_msgs['data_text']['subject'] = f"test主题"
    send_msgs['data_text']['main_txt'] = f"""
                                        <body >
                                        各位好：<br/>
                                        &emsp;&emsp;以下是test正文，详情请查收附件！</br>
                                        如有问题请随时联系，感谢！<br>

                                        <div><font><br></font></div><div><sign signid="1"><div>
                                        <div style="color:#909090;font-family:Arial Narrow;font-size:12px">------------------</div></div><div style="font-size:14px;font-family:Verdana;color:#000;">
                                        <div><div><font color="#808080">张三&nbsp;大数据开发部</font></div>
                                        <div><font color="#808080">手机：13130012345</font></div>
                                        <div><font color="#999999">地址：上海市陆家嘴 上海金融大厦</font>
                                        <br><font color="#999999">微信：zhangsan&nbsp; 邮箱：zhangsan@163.com
                                        <br>企业官网：www.123.com</font></div></div>

                                        </body>
                                        """
    send_msgs['msg_type']['msg_txt'] = 1
    send_msgs['msg_type']['msg_excel'] = 1
    send_msgs['msg_type']['msg_html_table'] = 1
    send_msgs['msg_type']['msg_html_n'] = 20

    send_msgs['data_text']['path'] = mac_path
    send_msgs['data_text']['file'] = '测试附件excel.xlsx'

    send_msgs['date_interval']['start_date'] = '2020-03-01'
    send_msgs['date_interval']['end_date']   = '2025-06-05'

    send_msgs['send_date']['excel_data'] = [df,df]  # 格式为列表
    send_msgs['send_date']['sheet_name'] = ['testsheet1','testsheet2']  # 格式为列表

    send_email(send_msgs)