
### 线上连接服务器
* 服务器地址： linux  



#### send_msgs参数说明 
| 参数 | 参数说明| 参数类型 |
 --------|---------|:--------------:|
fromaddr         | 登录的邮箱账号| str
smtpaddr         | 域名服务器|str
password         | 登录密码| str
toaddrs          | 接收人邮箱|list
ccaddrs          | 抄送人邮箱|list
msg_txt          | 是否有正文，  1代表是，0代表否 |int
msg_excel        | 是否有文本附件，1代表是，0代表否|int
msg_html_table   | 是否有正文标签 ，1代表是，0代表否|int
msg_html_n       | 正文表格展示的行数 ，1代表是，0代表否|int
subject          | 主题|str
main_txt         | 正文|str
path             | 附件的发送路径|str
file             | 附件的发送文件 格式为:***.xlsx|str
start_date       | 定制邮件的开始日期:格式xxxx-xx-xx|str
end_date         | 定制邮件的结束日期:格式xxxx-xx-xx|str
excel_data       | 发送的数据,格式为数据框型的列表 [dataframe]|list
sheet_name       | 发送数据对应的文本名称|list

关注我的博客[hejpei](https://blog.csdn.net/hejp_123)

#### 安装
```  命令行
python setup.py install
```
#### 导入模块
``` 命令行
import cl_api
```

```python

data = {'指标1': [i for i in range(10000,10100)],
      '指标2字段比较长': [ i+0.1234 for i in range(1000,1100)],
      '指标3': ['chuanglan@253' for  i in range(1000,1100)],
      '指标4字段非常比较长': ['chuanglan@253' for  i in range(1000,1100)],
      '指标5': ['2020-01-01'for i in range(1000,1100)]}

df = pd.DataFrame(df)

send_msgs = {
            "log": {  # 登录信息
                "fromaddr": "",
                "smtpaddr": "",
                "password": ""
            },
            "address": {  # 收件人 抄送人
                "toaddrs": [""],
                "ccaddrs": [""]
            }, # 发送类型
            "msg_type": {
                "msg_txt": 1,
                "msg_excel": 1,
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

```





