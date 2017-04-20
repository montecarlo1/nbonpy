import smtplib
sender = '912151131@qq.com'
receivers =['bobbylee0810@126.com']
message = """From: From Person<912151131@qq.com>
To:To Person<bobbylee0810@126.com>
Subject:SMTP e-mail test
This is a test-email message:"""
try:
    smptObj = smtplib.SMTP('localhost')
    smptObj.sendmail(sender, receivers, message)
    print "Successfully sent the email"
except smtplib.SMTPException:
    print "Error: unable to send the email"
