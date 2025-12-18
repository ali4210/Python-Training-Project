import schedule
import time as t
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from datetime import datetime


def abd():
    day = datetime.today()
    time = datetime.now()

    my_custom = day.strftime("%B %d %Y")
    current_time = time.strftime("%I:%M:%S %p")

    filename = r"/Python_Training/abd.txt"
    mylogo = r"C:\Users\User\PycharmProjects\pythonProject3\mahir.JPG"

    msg = MIMEMultipart()

    my_mail = "saleemali.mohammad211126@gmail.com"
    my_password = "cpif twnk otqr osnc"
    msg['Subject'] = f"Citrix connection alert {my_custom} {current_time}"
    msg['From'] = my_mail
    msg['To'] = my_mail
    msg['Cc'] = 'saleemali.mohammad@gmail.com'

    body = """
    <html><p> <b> <i>Hi Team,<br> This is testing email server via python script. <b> <i> <br> <img src="cid:alogo" width="100" height="60"></p> </html>
    """
    msg.attach(MIMEText(body, 'html'))

    ###LOGO section
    filelogo = open(mylogo, 'rb')
    msgIMAGE = MIMEImage(filelogo.read())
    filelogo.close()
    msgIMAGE.add_header('Content-ID', '<alogo>')
    msg.attach(msgIMAGE)

    # ATTACHMENT section
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())  # Fixed: removed extra parentheses around attachment
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename=abd.txt")  # Fixed: use only filename, not full path
    msg.attach(part)
    attachment.close()

    # FIXED: Added port 587 to SMTP connection
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()  # TLS transport layer security

    connection.login(user=my_mail, password=my_password)

    # FIXED: Specify recipients when using send_message
    recipients = [my_mail, "saleemali.mohammad@gmail.com"]
    connection.send_message(msg, to_addrs=recipients)

    connection.close()
    print("Mail has been sent")


# FIXED: Remove parentheses - pass function reference, don't call it immediately
schedule.every(10).seconds.do(abd)

while True:
    schedule.run_pending()
    t.sleep(1)