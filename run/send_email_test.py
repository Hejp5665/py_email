# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/26 11:44
@Author  : hejipei
"""
import platform
import pandas as pd
from cl_api.send_email_model import send_email
from cl_api.send_email_model import send_msgs
import argparse
import warnings
warnings.filterwarnings("ignore")
from contextlib import contextmanager
import time

@contextmanager
def timer(title):
    t0 = time.time()
    yield
    print("{}：使用时间为{:.0f}s".format(title, time.time() - t0))

parser = argparse.ArgumentParser(description='用于test和online开发')
parser.add_argument('--online', action='store_true',default=False ,help ='False 为测试，True 为生产运行')
args = parser.parse_args()

# 自动切换路径

mac_path = '/Users/yourname/PycharmProjects/py_email/output'
linux_path = '/home/user/yourname/PycharmProjects/py_email/output_data'

def get_path_file(mac_path,linux_path):
    sys = platform.system()
    if sys == "Darwin":
        print("OS is 苹果电脑!!!")
        path = mac_path
        return path
    elif sys == "Linux":
        print("OS is Linux!!!")
        path = linux_path
    return path


data = {'指标1': [i for i in range(10000,10100)],
        '指标2字段比较长': [ i+0.1234 for i in range(1000,1100)],
        '指标3': ['abcdefg' for  i in range(1000,1100)],
        '指标4字段非常比较长': ['a这是一个测试，文本内容' for  i in range(1000,1100)],
        '指标5': ['2025-01-01'for i in range(1000,1100)]
        }

if __name__ == '__main__':
    # 获取数据
    with timer("运行数据"):
        df = pd.DataFrame(data)
    # 配置邮箱信息
    send_msgs['log']['fromaddr'] = "account@xxx.com"
    send_msgs['log']['smtpaddr'] = "smtp.exmail.xx.com"
    send_msgs['log']['password'] = "123456"

    if args.online:
        print('=====生产发送=====')
        send_msgs['address']['toaddrs'] = ["hejp@163.com"]  # 格式为列表
        send_msgs['address']['ccaddrs'] = ["hejp@163.com"]  # 格式为列表
    else:
        print('=====测试发送=====')
        send_msgs['address']['toaddrs'] = ["hejp@253.com"]  # 格式为列表
        send_msgs['address']['ccaddrs'] = []  # 格式为列表


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

    send_msgs['data_text']['path'] = get_path_file(mac_path,linux_path)
    send_msgs['data_text']['file'] = '测试附件excel.xlsx'

    send_msgs['date_interval']['start_date'] = '2020-03-01'
    send_msgs['date_interval']['end_date']   = '2025-06-05'

    send_msgs['send_date']['excel_data'] = [df,df]  # 格式为列表
    send_msgs['send_date']['sheet_name'] = ['testsheet1','testsheet2']  # 格式为列表

    send_email(send_msgs)