# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/19 15:37
@Author  : hejipei
"""

import pandas as pd
import sys

def get_data_html(data_list, data_txt_list=None,n= 20):
    # css格式设置

    if  not isinstance(data_list, list):
        print('***get_data_html函数中请配置输入数值为列表***')
        sys.exit()
    if len(data_list) != len(data_txt_list):
        print('***请确认输入的DataFrame列表和标题列表长度一致***')
        sys.exit()

    css_style_01 = """
    <caption> </caption>
        <!-- CSS goes in the document HEAD or added to your external stylesheet -->
    <style type="text/css">
    table.gridtable {
        font-family: verdana,arial,sans-serif;
        font-size:12px;
        color:#333333;
        border-width: 1px;
        border-color: #666666;
        border-collapse: collapse;
    }
    table.gridtable th {
        border-width: 1px;
        padding: 8px;
        border-style: solid;
        border-color: #666666;
        background-color: #003366;    
    }
    table.gridtable td {
        border-width: 1px;
        padding: 8px;
        border-style: solid;
        border-color: #666666;
        background-color: #ffffff;
    }
    </style>
    <!-- Table goes in the document BODY -->
    <!-- <table class="gridtable"> -->
    """
    msg_html_str_all = css_style_01
    for index, msg_data in enumerate(data_list):
        if msg_data.shape[0]>n:
            msg_data =msg_data.head(n)
        msg_html_str = msg_data.to_html(header=True, index=False, border=1)
        if data_txt_list:
            replace_html = f"""<table class="gridtable"  align="center">
                            <caption><h3>{data_txt_list[index]}</h3></caption>
                            """  # 添加标题
        else:
            replace_html = f"""<table class="gridtable"  align="center">
                            <caption><h3></h3></caption>
                            """  # 添加标题
        msg_html_str = msg_html_str.replace('<table border="1" class="dataframe">', replace_html)  # 替换为指定的格式和标题
        msg_html_str = msg_html_str.replace("right", "center ")  # 标题居中
        msg_html_str = msg_html_str.replace("<th>", '<th><font size="2" color="white">')  # 更改颜色和大小
        msg_html_str = msg_html_str.replace("</th>", '</font></th> ')  # 添加结束符
        t = '<br/>'
        msg_html_str_all = msg_html_str_all + msg_html_str + t * 3

    return msg_html_str_all


