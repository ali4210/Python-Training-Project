print(list(range(1,11)))
for i in range(1,11):
    print(i)
    print("Ali")

mylist=['apple','banana','orange']
for item in mylist:
    print(item)
    print(f"my list value is:{item}")


myinfo={"name":"ABD","age":44,"city":"bangalore"}

for k,v in myinfo.items():
    print(f"My key is : {k}")
    print(f"My value is : {v}")
for k in myinfo.keys():
    print(f"My key is : {k}")
for k in myinfo.values():
    print(f"My value is : {k}")






i=1
while i<10:
    print(i)
    i+=1

i=10
while i>=0:
    print(i)
    i-=1

import os
#print((list(os.walk(os.getcwd()))))
for roots,dirs, files in (list(os.walk(os.getcwd()))):
   if len(files)>0:
        print(roots)
        for i in files:
            print(os.path.join(roots,i))