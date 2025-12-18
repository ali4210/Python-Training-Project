import os
import sys

print(os.sep)
print(os.getpid())
print(os.getcwd())
#print(os.getgid())


myfiles=os.listdir()
print(myfiles)
print(myfiles[2])


myext=myfiles[4].split('.')
print(myext[0])

print(os.popen('dir').read())

mypath="C:\\Users\\User\\Desktop\\Python"
print(f"my path is: {mypath}")
print(f"my base path is: {os.path.basename(mypath)}")
print(f"my parent path is: {os.path.dirname(mypath)}")
mylist=os.path.split(mypath)
print(mylist)
print(mylist[1])
print(f"my dir is : {mylist[0]}")

print(os.path.isfile(mypath))
print(os.path.isdir(mypath))
if os.path.isfile(mypath):
    print(f"file {mypath} exists")
else:
    print(f"file {mypath} does not exist")
print(os.path.exists(mypath))
if os.path.exists(mypath):
    if os.path.isdir(mypath):
        print(f"directory {mypath} exists")
    else:
        print(f"file {mypath} does not exist")



print(os.path.getsize(mypath))
print(os.path.normpath(mypath))
print(os.path.normcase(mypath))
print(os.path.samefile(mypath, mypath))
import platform
print(dir(platform))

print(platform.architecture())
print(platform.machine())
print(platform.platform())
print(platform.processor())
print(platform.system())
print(platform.version())
print(platform.python_implementation())
print(platform.python_build())
print(platform.node())
print(platform.uname())

if platform.system() == 'Windows':
    os.system("ipconfig")
elif platform.system() =='Linux':
    os.system("ifconfig")
else:
    print("Sorry, Please check with admin")


print(platform.python_implementation())
print(platform.python_version())
print(sys.version)
print(sys.platform)
print(sys.executable)
print(sys.path)
sys.exit()

