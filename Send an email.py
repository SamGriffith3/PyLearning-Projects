import smtplib
import email.utils
from email.mime.text import MIMEText
import socket

print (socket.getfqdn('https://google.mail.com'))
# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', 'samgriffith3@gmail.com'))
msg['From'] = email.utils.formataddr(('Author', 'garfunkelnator@gmail.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP()

try:
    server.sendmail('garfunkelnator@gmail.com', ['samgriffith3.com'], msg.as_string())
finally:
    print('email delivered')

