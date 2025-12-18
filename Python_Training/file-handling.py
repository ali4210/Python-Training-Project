'''
file=open("abd.txt")
print(file.read())
file.close()

with open("abd.txt") as file:
    print(file.read())



with open("abd.txt") as file:
    data=file.readlines()
    for i in data:
        word=i.split()
        print(word)

'''
'''
with open("abd.txt",mode="w") as file:
    data=file.write("Hello Brother, How you doing man")
    print(data)
with open("abd.txt",mode="r") as file:
    data=file.read()
    print(data)
with open("abd.txt",mode="w") as file:
    file.write("Hello Brother, How you doing Mister\n")
    file.write("How you doing Mister\n")
    file.write("How you doing Brother\n")
with open("abd.txt",mode="a") as file:
    file.write("Hello Didi, Date pe chale\n")

with open("abd.txt",mode="r") as file:
    data=file.read()
    print(data)


mydata=["Python ","Java","C++","C#","JavaScript"]
with open("abd.txt",mode="a") as file:

    for i in mydata:
        word=i.split()
        print(word)
        file.write(i+"\n")

for i in range(11):
    with open("abd.txt",mode="a") as file:
        data=file.write(f"Line: {i}\n")
        print(data)
'''

