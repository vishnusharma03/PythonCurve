import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.ehlo()

with open('src/password.txt', 'r') as pw:
    password = pw.read()

server.login('vishnusharma.kr7488@gmail.com', password)

msg = MIMEMultipart('alternative')

msg['From'] = "Nobody"
msg['To'] = "You"
msg['Subject'] = "First email via Python Script."

with open('src/message.txt', 'r') as ms:
    message = ms.read()


msg.attach(MIMEText(message))

filename = "src/me.png"
img = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(img.read())

encoders.encode_base64(p)
p.add_header('Content-Desposition', f'Filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail('vishnusharma.kr7488@gmail.com', 'vishnusharmauss@gmail.com', text)
print("Send Successful!")




