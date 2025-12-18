import re
'''
myword="Abdeali Dodiya   from bangalore\n , python\n    python6 We are learning saleem@gmail.com and in thiscoursewe will 34 learn two version such python2 and python3, We will learn Python selenium in this course courses courses"

#pattern='python[23]'
#pattern="python[23]?"
#pattern='python?'
#pattern='course$'
#pattern='\\bcourse'
#pattern='\\bcourse\\b'
#pattern=r'\bcourse\b'
#pattern=r'\bcourses{1}\b'
pattern=r"\bpython\d\b"

#pattern='\\Bcourse\\B'
#pattern=r'\Bcourse\B'
#pattern="\\t"
#pattern="\\n"


#pattern="python|python2|python3|Python"
#pattern="\w"
#pattern="\w\w\w"
#pattern=("\w\w\w\w\w")
#pattern="\W"
#pattern="\S"
#pattern="\d"
#pattern="\d\d"
#pattern="."
#pattern=".."
#pattern="..."
#pattern="\.\w\w\w"
#pattern="\@\w\w\w\w\w\.\w\w\w"


print(re.findall(pattern,myword))

print("########################################################")

'''
import re

mytext="""
My Broadcast Address is 255.255.255.255 and jboss server ip address is 192.168.1.8 
My Docker server ip address is 192.168.1.11 
my invalid ip is 192.168.000.12546 
0..0.12548 and 0..1.3
"""

#pattern=r"\d\d\d.\d\d\d.\d.\d\d"
#pattern=r"\d\d\d.\d\d\d.\d.\d"
#pattern=r"\d{3}.\d{3}.\d{1}.\d{2}"
#pattern=r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
#pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
pattern=r"\d{1,}.\d{1,}.\d{1,}.\d{1,}"
#pattern=r"\d+.\d+.\d+.\d+"
#pattern=r"\d*\.\d*\.\d*\.\d*"
#pattern=r"\d?\.\d?\.\d?\.\d?"
#pattern=r"^My"


print(re.findall(pattern,mytext,re.M))
print("##########################################################################")
print(re.findall(pattern,mytext,re.M|re.I))
print("##########################################################################")
print(re.findall(pattern,mytext))
print("##########################################################################")
print(len(re.findall(pattern,mytext)))
print("##########################################################################")


myiter=(re.finditer(pattern,mytext))
print(myiter)
for match in myiter:
    #print(match)
    print("My match string is : ",  match.group())

print("##########################################################################")


import re
mytext1="We are learning python automation course, In devops course python is very important"

pattern2=re.compile('course')

print(type(pattern2))

print(re.findall(pattern2,mytext1))

print("##########################################################################")

import re
mytext2="My 192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"

pattern3=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

myfind=(re.search(pattern3,mytext2))
print("we have found some string from pattern" ,myfind.group())
print("Starting Index" ,myfind.start())
print("Ending Index" ,myfind.end())
print("Search Length is :" ,myfind.end()-myfind.start())

if myfind:
    print("We have found some string from Pattern",myfind.group())
else:
    print("Sorry , no match found")


print("##########################################################################")

#You can find character string more than 7 to 8 character
import re
abd="Abdeali"
pattern=r".{1,}"
print(re.search(pattern,abd))


#You can check whether your string is upper case or not
import re
abd="ABDEALI"
pattern=r"[A-Z]"
print(re.search(pattern,abd))



print("##########################################################################")


import re
mytext="My 192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myfind=(re.findall(pattern,mytext))
print(myfind)

import re
mytext="My 192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myfind=(re.search(pattern,mytext))
print(myfind)

import re
mytext="My 192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myfind=(re.findall(pattern,mytext))
print(myfind)
print(re.match(pattern,mytext))

import re
mytext="192.168.1.8 My jboss server ip address is "
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
print(mytext)
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
print(re.match(pattern,mytext))

print("##########################################################################")


import re
mytext="192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

print(re.match(pattern,mytext))


import re
mytext="192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

print(re.search(pattern,mytext,re.M))

print("##########################################################################")

import re
mytext="192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

mymatch=(re.split(pattern,mytext))
print(mymatch)
for i in mymatch:
       print(i)

print("##########################################################################")

import re
print(re.split('[a-c]','0a2ALI7',re.I))

import re
myword= "Abdeali Dodiya from bangalore, We are leaning python course and in this python course will lear two version like python2 and python3 course"
pattern=r"\bcourse\b"
print(re.sub(pattern,'COURSE',myword))


import re
myword= "Abdeali Dodiya from bangalore, We are leaning python course and in this python course will lear two version like python2 and python3 course"
pattern=r"\bcourse\b"
print(re.subn(pattern,'COURSE',myword))

