
### 线上连接服务器
* 服务器地址： linux/window 

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

关注我的博客[hejipei](https://blog.csdn.net/hejp_123)

#### 使用方法
在run/send_eamil_test.py 中配置你的邮箱账号密码就能直接运行结果

然后运行
```python
python send_eamil_test.py
```


