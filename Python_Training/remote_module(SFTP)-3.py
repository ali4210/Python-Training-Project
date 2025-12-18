import paramiko

hostname="192.168.0.150"
username="kali"
password="kali"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname,username=username,password=password)

mysftp = client.open_sftp()
#mysftp.get('/home/kali/server.csv','test.csv')
#mysftp.put('test.csv','/home/kali/Downloads/test1.csv')
mysftp.chdir('/home/kali/Downloads/')
mysftp.put('test.csv','test4.csv')
#file=mysftp.open('test4.csv','a')
#file.write("RamzanKhan\nSaleem Khan\n", )
file=mysftp.open('test4.csv','r')
print(file.read())


#print(mysftp.listdir())

#print(mysftp.stat('test4.csv').st_size)
#print(mysftp.stat('test4.csv'))


mysftp.close()
client.close()