import os

for i in os.listdir():
    if i.endswith('.py'):
        print(i)

i=1
while True:
    print(i)
    i+=1
    if i>=5:
        break

for i in range(1,10):
    if i==5:
        break
    else:
        print(i)

for i in range(1,10):
    if i==5:
        continue
    else:
        print(i)

for i in range(1,10):
    if i==5:
        pass
   