import smtplib
from email.mime.text import MIMEText
SMTPserver = 'smtp.126.com'
sender = 'bobbylee0810@126.com'
password = 'smart2B!'
destination = '912151131@qq.com'
message = 'I send a message by Python. hello'
msg = MIMEText(message)
msg['Subject'] = 'Test Email by Python'
msg['From'] = sender
msg['To'] = destination
mailserver = smtplib.SMTP(SMTPserver, 25)
mailserver.sendmail(sender, [sender], msg.as_string())
mailserver.quit()
print('success!')