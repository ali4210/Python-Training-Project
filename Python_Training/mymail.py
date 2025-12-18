import smtplib
from email.message import EmailMessage


my_mail="saleemali.mohammad211126@gmail.com"
my_password="cpif twnk otqr osnc"
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=my_mail, password=my_password)


msg = EmailMessage()
msg['Subject'] = "SMTP Report Status"
msg['From'] = my_mail
msg['To'] = my_mail
msg['Cc'] = ["saleemali.mohammad@gmail.com","yousuf3597494@gmail.com"]

msg.set_content("Hi team ,this is saleem ali testing from python")


#This is Attachment Section
with open('abd.txt', 'rb') as file:
    attach = file.read()
    file_name=file.name
msg.add_attachment(attach, maintype='application', subtype='octet-stream',filename=file_name)

#This is alternative Html attachment
msg.add_attachment("""
<html>
<head> 
<b> Hi team This is mohammad saleem ali from team </b> 
</head>
<body>""",subtype='html')


connection.send_message(msg)
connection.close()


#SUBJECT = "Alnafi Practical Mail 2222"
#TEXT = "Hi , Team. This is a testing Mail via smtp server"
#abd='Subject: {}\n\n{}'.format(SUBJECT, TEXT)

#connection.sendmail(from_addrs=my_mail, to_addrs="saleemali.mohammad@gmail.com", msg=abd)
#connection.quit()


print("Your Mail has been sent")

