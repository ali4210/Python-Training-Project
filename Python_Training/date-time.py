import datetime
'''

print(datetime.datetime.today())
current_time = datetime.datetime.now()
print(current_time)
print(datetime.datetime.now())

print(dir(current_time))
print(current_time.date())
print(current_time.time())

print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.weekday())

print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.microsecond)
print(current_time.tzinfo)

print(current_time.ctime())
print(current_time.isoformat())
print(current_time.timetuple())


testdate=datetime.date(2020, 1, 1)
print(testdate)
print(testdate.day)
print(testdate.month)
print(testdate.year)


from datetime import datetime
current_time=datetime.now()
print(current_time)


import datetime
mytime=datetime.datetime.now()
print(mytime)


from datetime import datetime
start_time=datetime.strptime("2:13:57", "%H:%M:%S")
end_time=datetime.strptime("11:47:52", "%H:%M:%S")

print(start_time)
print(end_time)

get_diff = (end_time - start_time)
print(get_diff)
sec=get_diff.total_seconds()
print("Differnece in Seconds:",+sec)

min=sec/60
print("Differnece in Minutes:",+min)
hour=min/60
print("Differnece in Hours:",+hour)

import pytz
tz=pytz.timezone('Asia/Shanghai')
now=datetime.now(tz)
print(now)

'''
from datetime import datetime

current=datetime.now()
print(current)
year=current.strftime("%Y")
print(year)
month=current.strftime("%m")
print(month)
day=current.strftime("%d")
print(day)

time=current.strftime("%H:%M:%S")
print(time)
print(type(time))

new_time=datetime.strptime("11:47:52", "%H:%M:%S")
print(new_time)

latime=current.strftime("%H:%M:%S %d/%m/%Y %d-%m-%Y %I=%M=%S %A %a %p")
print(latime)
print(latime)
print(type(latime))


mydate='2022/09/05 13:20:52'
print(type(mydate))
myptime= (datetime.strptime(mydate,"%Y/%m/%d %H:%M:%S"))
print(myptime)
print(type(myptime))

import time
import datetime
print(time.localtime())
seconds=time.time()
print(seconds)
print(datetime.datetime.fromtimestamp(seconds))

localtime=time.ctime(seconds)
print(localtime)
print(time.gmtime())



import time
print("This is sample example")
time.sleep(5)
print("This is sample example1")
time.sleep(5)
print("This is sample example2")

