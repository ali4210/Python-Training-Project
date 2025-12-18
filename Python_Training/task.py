import json

from pandas.conftest import multiindex_year_month_day_dataframe_random_data

jsonfile=r"C:\Users\User\PycharmProjects\pythonProject3\fruits.json"
with open(jsonfile, "r") as jf:
    my_dict=json.load(jf)
    print(my_dict)
mydata=[]
for i in my_dict:
    if i['price'] >=1:
        total_count=(len(i.keys()))
        mydata.append(i['name'])

print(mydata)
print(total_count)
myfruits=' '.join(mydata)
print(myfruits)