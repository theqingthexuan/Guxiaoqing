import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

mail_host = 'smtp.qq.com'
mail_user = '1314520@qq.com'
mail_pass = '（密钥）'

name = ['1314520@qq.com']

message = MIMEMultipart()
message["From"] = mail_user
message["To"] = ";".join(name)
message["Subject"] = "这是主题：SMTP邮件测试"
message.attach(
    MIMEText("<p>这是正文：图片及附件发送测试</p><p>图片演示：</p><p><img src=\"cid:image1\"></p>", "html", "utf-8"))

fp = open("1.png", "rb")
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header("Content-ID", "<image1>")
message.attach(msgImage)

att1 = MIMEText(open("file1.txt", "rb").read(), "base64", "utf-8")
att1["Content-Type"] = "application/octet-stream"
message.attach(att1)

att2 = MIMEText(open("file2.txt", "rb").read(), "base64", "utf-8")
att2["Content-Type"] = "application/octet-stream"
message.attach(att2)

try:
    smtp0bj = smtplib.SMTP()
    smtp0bj.connect(mail_host, 25)
    smtp0bj.login(mail_user, mail_pass)
    smtp0bj.sendmail(mail_user, name, message.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print(f"发送失败，错误原因：{e}")
