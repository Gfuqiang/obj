import pathlib
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.163.com'
#163用户名
mail_user = 'fuqiang6261@163.com'
#密码(部分邮箱为授权码)
mail_pass = 'JJNKCHCKJKNDVPBA'
#邮件发送方邮箱地址
sender = 'fuqiang6261@163.com'
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['626181185@qq.com']

#设置email信息

#邮件内容设置
# message = MIMEText('content','plain','utf-8')
# #邮件主题
# message['Subject'] = 'title'
# #发送方信息
# message['From'] = sender
# #接受方信息
# message['To'] = receivers[0]

message = MIMEMultipart()
message['From'] = sender
message['To'] = receivers[0]
message['Subject'] = '带附件的邮件测试'
message.attach(MIMEText('这是用Python编写的邮件发送程序……', 'plain', 'utf-8'))
body = """
    <body>
      <h1>测试邮件内容</h1>
      <span>测试邮件正文....</span>
    </body>
"""
msgtext = MIMEText(body, 'html', 'utf-8')
message.attach(msgtext)

p = pathlib.Path('fies_dir')
html_file_path = p / 'test.html'


#通过MIMEApplication构造附件1
import tempfile
import pandas as pd
with tempfile.TemporaryFile() as fp:
    df = pd.DataFrame({"first": [1, 2, 3], "second": [4, 5, 6]})
    with pd.ExcelWriter(fp) as write:
        df.to_excel(write, sheet_name='第一页')
    fp.seek(0)
    att1 = MIMEApplication(fp.read())
    att1["Content-Type"]='application/octet-stream'
    #att1["Content-Disposition"] = 'attachment; filename="test1.html"'
    att1.add_header('content-disposition', 'attachment', filename='test.xlsx')
    message.attach(att1)


#通过MIMEText构造附件2文本
#Content-Type（内容类型）定义网络文件的类型和网页的编码，决定浏览器将以什么形式、什么编码读取这个文件
#[Content-Type介绍](https://www.runoob.com/http/http-content-type.html)
#application/octet-stream：二进制流数据（如常见的文件下载）
# Content-Disposition激活附件下载对话框。Content-Disposition有两种属性：inline 和 attachment
# inline:默认值，将文件内容直接显示在页面；
# attachment：弹出对话框，让用户下载
# filename：定义下载文件的文件名。
# att2=MIMEText(open('E:\\Path\\filename.txt','rb').read(),'base64','utf-8')
# att2["Content-Type"]='application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="fujian2.txt"'
# message.attach(att2)
#
#
# #通过MIMEImage构造附件3图片
# att3=MIMEImage(open('E:\\path\\filename.jpg','rb').read())
# att3["Content-Type"]='application/octet-stream'
# att3["Content-Disposition"] = 'attachment; filename="fujian3.jpg"'
# message.attach(att3)
#
#
# #通过MIMEAudio构造附件4。MEMEAudio需要定义音频类型
# #[不同音频对应的类型参考](http://https://www.cnblogs.com/zhongcj/archive/2008/11/03/1325293.html )
# att4=MIMEAudio(open('E:\\path\\filename.mp3','rb').read(),'audio')
# att4["Content-Type"]='application/octet-stream'
# att4["Content-Disposition"] = 'attachment; filename="fujian4.mp3"'
# message.attach(att4)

#登录并发送邮件
try:
    # smtpObj = smtplib.SMTP()
    smtpObj = smtplib.SMTP_SSL(host=mail_host)
    #连接到服务器
    # smtpObj.connect(mail_host,25)
    smtpObj.connect(mail_host,465)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass)
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    #退出
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误
