import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
from datetime import datetime, date
import time as t
my_mail = "saleemali.mohammad211126@gmail.com"
my_password = "cpif twnk otqr osnc"
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=my_mail, password=my_password)

msg = MIMEMultipart()
day=date.today()
time=datetime.now()

my_custom=day.strftime("%B %d, %Y")
current_time=time.strftime("%I:%M:%S %p")
filename = r"/Python_Training/abd.txt"
mylogo=r"C:\Users\User\PycharmProjects\pythonProject3\mahir.JPG"

msg['Subject'] = f"Citrix Connection Alert {my_custom} {current_time}"
msg['From'] = my_mail
msg['To'] = my_mail
# FIX: CC should be a comma-separated string, not a list
msg["Cc"] = "saleemali.mohammad@gmail.com"



body = """<html>
<head>
<p><b><i>Hi team This is mohammad saleem ali from team </i></b> <br> <img src="cid:logo" width="100" height="60" </p>
</head>
</html>"""
msg.attach(MIMEText(body, 'html'))


## This is LOGO Section
filelogo=open(mylogo,"rb")
msgIMAGE = MIMEImage(filelogo.read())
msgIMAGE.add_header('Content-ID', '<logo>')
msg.attach(msgIMAGE)



# Attachment Section
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
# FIX: Use only the filename, not the full path
part.add_header('Content-Disposition', "attachment", filename="abd.txt")
msg.attach(part)

# FIX: When using send_message, you need to specify recipients
# Combine To and CC recipients
recipients = [my_mail, "saleemali.mohammad@gmail.com"]
connection.send_message(msg, to_addrs=recipients)
connection.close()
print("Your Mail has been sent")