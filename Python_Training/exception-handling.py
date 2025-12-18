try:
    1/0
except Exception as e:
    print("Something having issue----", e)

try:
    x = "ABD"
    print("My value is ", x)
    print("My value is ", y)
except:
    print("Something having issue")

#   mylist = [1, 2, 3]
#    print(mylist[4])

try:
    import oss
    os.system('dir')
except Exception as e:
    print('Something issue :' ,e)
#

try:
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))

    result= a/b
    print(result)
except Exception as e:
    print("Something issue:",e)



try:
    import os
    x = "ABD"
    y="Ali"
    print("My value is ", x)
    print("My value is ", y)
    mylist = [2, 7, 8, 9]
    print(mylist[3])
    os.system('hostname')
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))

    result = a / b
    print(result)
except NameError:
    print("Something having issue in your variable, Please check variable define or not")
except IndexError:
    print("Please check your data structure index value should be within range")
except ModuleNotFoundError:
    print("Please check module name or module available in your machine")
except ZeroDivisionError:
    print("Please check value , Zero you can not devide with any value ")
except ValueError:
    print("Value error because you can not divide value with string ")
except Exception as e:
    print("Something having issue within your Code," )
else:
    print("Everything Alright as else")
finally:
    print("This statement will print regardless")