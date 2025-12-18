

import json

'''
with open("my.json", "r") as myfile:
    data = myfile.read()
    print(data)


jsonfile = "C:\\Users\\User\\PycharmProjects\\pythonProject3\\my.json"
print(jsonfile)


jsonfile = "C:\\Users\\User\\PycharmProjects\\pythonProject3\\my.json"
with open("my.json", "r") as myfile:
    my_dict=json.load(myfile)
    print(my_dict)
for key, value in my_dict.items():
    print(key,":",value)

password_nginx = (my_dict['password_nginx'])
print(password_nginx)

print(f"My NGINX password is:",password_nginx)
print(f"My NGINX password is: {password_nginx}")



jsonfile1=r"C:\Users\User\PycharmProjects\pythonProject3\user.json"
with open(jsonfile1, "r") as jf:
    my_dict1=json.load(jf)
    print(my_dict1)

for i in my_dict1:
    print(f"My Dictionary is: {i}")
    for key, value in i.items():
        print(key,":",value)

    for k,v in i.items():
        if v == 'Ubuntu':
            print("My Ubuntu version is ", i["Version"])
        if v == 'CentOS':
            print("My CentOS version is ", i["Version"])


myinfo = {
"server1" : {
"IBM": {
"datacenter":"Bangalore",
"env": {
"PR": "192.168.1.1",
"DR": "192.168.1.2"
}
}
    }
}

mypath="user_details.json"
with open(mypath, "w") as myfile:
    json.dump(myinfo, myfile,indent=4)
    
'''


