# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/15 15:05
@Author  : hejipei
"""
import pandas as pd
import re
import sys
# 判断列宽
def Judge_str_type_num(x):
    ln = len(x)
    #提取字符串里的中文，返回数组
    pattern="[\u4e00-\u9fa5]+"
    regex = re.compile(pattern)
    results = regex.findall(x) # 找到所有中文
    length = len(''.join(results))
    str_len = length +ln
    return str_len

def deal_excel_pd_data(df, path_file,Sheet_name = None):
    """
    :param df: 为列表pandas
    :param path_file: 保存的目录，最好写绝对路径
    :param Sheet_name: sheet命名
    :return:
    """
    if  not isinstance(df, list):
        print("***请设置send_msgs['send_date']['excel_data']的变量为列表***")
        sys.exit()

    writer = pd.ExcelWriter(path_file)

    workbook = writer.book
    fmt = workbook.add_format({'font_size': 9,"font_name": u"微软雅黑"})
    border_format = workbook.add_format({'border': 1})
    amt_fmt = workbook.add_format({'num_format': '#,##0'})
    # 表头高亮
    header_fmt = workbook.add_format(
        {'bold': True, 'font_size': 9, 'font_name': u'微软雅黑', 'num_format': 'yyyy-mm-dd', 'bg_color': '#9FC3D1','valign': 'vcenter', 'align': 'center'})
    date_fmt = workbook.add_format({"font_name": u"微软雅黑",'num_format': 'yyyy'})

    for index, df_part in enumerate(df):
        l_end = len(df_part.index) + 1
        if Sheet_name:
            sh_name  = Sheet_name[index]
        else:
            sh_name = f"Sheet{index+1}"

        for index, col in enumerate(df_part.columns.values):
            if df_part[col].dtypes in ['int', 'int64', 'float64', 'float']:
                continue
            else:
                try:
                    df_part[col].astype("datetime64[ns]")
                    df_part[col] = df_part[col].astype("str")
                except:
                    continue

        df_part.to_excel(writer, sheet_name=sh_name, encoding='utf8', header=False, index=False, startcol=0,startrow=1)
        worksheet = writer.sheets[sh_name]
        # 表头设置格式
        for col_num, value in enumerate(df_part.columns.values):
            worksheet.write(0, col_num, value, header_fmt)

        # 设置列宽
        LANG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        LANG = [i for i in LANG]
        for index, col in enumerate(df_part.columns.values):
            # n = df_part[col].astype("str").str.len().max()
            n = df_part[col].apply(lambda x:Judge_str_type_num(str(x))).max()
            if n>40:
                n = 40 # 设置宽的最大值
            m = LANG[index]
            header_len = Judge_str_type_num(col)
            Num_fmt,Time_fmt,Str_fmt = [],[],[]
            # print('da',n,header_len,col)
            if df_part[col].dtypes in ['int','int64','float64','float']:
                Num_fmt.append(m)
                if n > header_len:
                    worksheet.set_column(f'{m}:{m}', n, fmt)
                else:
                    worksheet.set_column(f'{m}:{m}',  1.1* header_len, fmt)
            else:
                try:
                    df_part[col].astype("datetime64[ns]")
                    Time_fmt.append(m)
                    if n > header_len:
                        worksheet.set_column(f'{m}:{m}', 1*n, fmt)
                    else:
                        worksheet.set_column(f'{m}:{m}', 0.8* header_len, fmt)
                    # worksheet.conditional_format(f'{m}:{m}', {'type': 'no_errors', 'format': date_fmt})
                except:
                    Str_fmt.append(m)
                    if n > header_len:
                        worksheet.set_column(f'{m}:{m}', n , fmt)
                    else:
                        worksheet.set_column(f'{m}:{m}', 0.8* header_len, fmt)

            worksheet.conditional_format(f'A1:{m}%d' % l_end,
                                     {'type': 'no_errors', 'format': border_format})  # type 可以参考底层文件
            for i in Num_fmt:
                worksheet.conditional_format(f'{i}2:{i}%d' % l_end,
                                          {'type': 'cell', 'criteria': '>=', 'value': 1, 'format': amt_fmt})
    writer.save()
    print('excel处理成功')



