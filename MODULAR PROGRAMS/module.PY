#module
#import to another file
# import newmodule
# newmodule.difference()
# print(newmodule.tuple1)

# #from import
# from newmodule import difference,tuple1,myfunc
# myfunc()
# difference()
# print(tuple1)

# from newmodule import*  #all function,data
# difference()
# myfunc()


#buit-in modules
import math
print(math.sqrt(49))  #square root
print(math.fabs(-7))   #absolute value of a number
print(math.ceil(4.3))  #round to next integer
print(math.floor(2.9))   #round down to next integer
print(math.factorial(5))  #factorial
print(math.pow(2,5))  #power of a number

# list1=[1,2,3,4,5,6]
# print(math.prod(list1))
# print(sum(list1))
# print(max(list1))
# print(min(list1))
# print(math.pi())

# import random
# #number generating
# print(random.randint(1,5)) #include upper and lower limit
# print(random.randrange(1,10)) #exclude upper limit
# #string
# txt1="farhana"
# print(random.choice(txt1)) #randomly choosing a charecter from a string

# import datetime
# x=datetime.datetime.now()
# print(x)
# print(x.strftime("%A"))
# print(x.strftime("%B"))
# print(x.strftime("%Y"))
# print(x.month)
# print(x.day)
# print(x.year)
# y=datetime.datetime(2003,4,27)
# print(y.strftime("%A"))

#exception handling:using try-except
# try:
#     a=10
#     b="hi"
#     s=a+b
#     print(s)
# except NameError:
#     print("undefined variable")
# except TypeError:
#     print("type mismatch")
# except ValueError:
#     print("value not defined") 
# try:          
# except Exception as e:
#      print(e)