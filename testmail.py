import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "jay842803@gmail.com"
receiver = ["sjs120235874@gmail.com","jay842803@gmail.com"]
passwd = "jmnc ddau ygqr uilx"

for i in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = i
    msg["subject"] = Header("Test send email","utf-8").encode()

    msg_text=MIMEText("This is send by python\n你好嗎")
    msg.attach(msg_text)
    c = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
        server.login(sender,passwd)
        server.sendmail(sender,i,msg.as_string())
print("success send mail 成功寄送")