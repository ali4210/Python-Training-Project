'''

def abd():
    print("this is a function")
    print("this is a way-bigfunction")
    print("this is a way-smallfunction")

print("222222222222222222there is a gap2222222222222222")
abd()
print("2222222222222222222there is a gap222222222222222222222")
abd()
print("222222222222222222222222there is a gap2222222222222222222222")
abd()


def first():
    print("My first  function")

def second():
    print("My second function")

first()
second()

def third():
    print("*"*30)
    print("\t\tSaleem Yousuf Ali")
    print("*"*30)
third()

def my(abd):
    print("*" * 30)
    print("\t\t" + abd)
    print("*" * 30)
my("This is a function")
my("This is a way-bigfunction")

def new():
    ali = 6
    print("My new function" , ali)



def old():
    ali = 2
    print("My old function" , ali)

def latest():
    global ali
    ali = 3
    print("My old function" , ali)


new()
old()
latest()
print("outside",ali)




def add(a,b):
    c = a + b
    #print(c)
    return c
def mycode():
    a=int(input("enter a"))
    b=int(input("enter b"))
    print(add(a,b))

#mycode()

def num(ali=3):
    print(ali)

num(1)
num(2)
num()


def mynew(server,ip,os):
    print(f"Server is : {server}\n IP is : {ip}\n OS is : {os}")
mynew("IBM","192.168.0.12","RHEL")



def myold(*data):
    print(f"Server is : {data[0]}\n IP is : {data[1]}\n OS is : {data[2]}")
#myold("IBM","192.168.0.12","RHEL")
mylist=["IBM","192.168.0.12","RHEL"]
myold(*mylist)

def mycode1(*mydata):
    for i in mydata:
        print(type(i))
        return None


mycode1(4,5,7)

def mycod2(**mydata):
    for k,v in mydata.items():
        print(k,v)

mydict={'server':'IBM','IP':'192.168.1.1','OS':'AIX'}
mycod2(**mydict)

'''

result=lambda a,b: a+b
print(result(1,2))

result=lambda a,b: a if (a >= b) else b
print(result(1,2))

import os
def mycode():
    print("This is my code function")

def main():
    print(os.listdir(os.getcwd()))
    print("My global print")

if (__name__ == "__main__"):
    main()
