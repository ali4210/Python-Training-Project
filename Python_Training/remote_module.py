import paramiko
hostname="192.168.0.150"
username="kali"
password="kali"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname,username=username,password=password)

mycmd = "df -h"


stdin,stdout,stderr = client.exec_command(mycmd)

mycmdout=stdout.readlines()
#print(mycmdout)

for line in mycmdout:
    print(line.strip('\n'))
