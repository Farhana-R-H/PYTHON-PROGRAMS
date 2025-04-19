#FOLDER
# def myfunction():
#     print("helloo")
# myfunction()    

# def add():
#     a=int(input("enter the value"))
#     b=int(input("enter the value"))
#     sum=a+b
#     print(sum)
# add()    

# def sub():
#     a=int(input("enter 1st value"))
#     b=int(input("enter 2nd value"))
#     diff=a-b
#     print("difference is",diff)
# sub()    

# def display_name(name):
#     print("my name is",name)
# display_name("farhana")    

# list1=[1,34,23,"hi","good"]
# def show_list(list1):
#     for i in list1:
#         print(i)
# show_list(list1)        

#sum of elements in a list
# def sum_of_elements__oflist():
#     n=int(input("enter numbers"))
#     sum=0
#     list1=[]
#     for i in range(n):
#         list1.append(i)
#         sum+=i
#     print(sum)
# sum_of_elements__oflist()        

# #
# def add():
#     a=int(input('value:'))
#     b=int(input("value:"))
#     s=a+b
#     return s
# x=add()
# print(x)

#factorial of an number 
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# x=factorial(3)
# print(x)    


# def add():
#     a=int(input("value"))
#     b=int(input('value:'))
#     s=a+b,a*b,a-b
#     return s
# x,y,z=add()
# print(x,y,z)

#palindrome checking with function
# txt=str(input("enter the word"))
# def palindrome(txt):
#     rev=txt[::-1]
#     if rev==txt:
#         return txt,"is palindrome"
#     else:
#         return txt,"is not palindrome"
# p=palindrome(txt)
# print(p)    

#sort words of sentence in ascending order
# txt=str(input("enter the word"))
# list=[]
# def sorting(txt):
#     list=txt.split()
#     list.sort()
#     return list
# s=sorting(txt)
# print(s)

#ARGUMENT PASSING TECHNICS
#1.ARBITRARY ARGUMENTS(tuple):
# def myfunction(*args):
#     for i in args:
#         print(i)
# myfunction(1,2,3,)


# def myfunction(*args):
#      print (args[2]) #tuple indexing position
# myfunction(1,2,3,4)

#KEYWORD ARGUMENTS
# def myfunction(a,c,d,b):
#     print(d)
# myfunction(a=10,b=34,c=90,d=88)

#ARBITRARY KEYWORD ARGUMENT
# def function(**args):
#     print(args["b"])
# function(c=10,b=30,a=20)    
    
#RECURSION(a function which call itself)
#EXAMPLE1:
# num=int(input("enter value:"))
# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
# f=factorial(num)
# print(f) 

#EXAMPLE2:
# num=int(input("enter value"))
# def sum(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num+sum(num-1)
# s=sum(num)
# print(s)

#REVISION


#phonebook using functions
# phonebook={}
# def addcontact():
#     name=input("enter name")
#     if name in phonebook:
#             print("contact already exist")
#     else:
#         phone=input("enter phone number")
#         phonebook.update({name:phone})
#         print(phonebook)
# def deletecontact():
#     name=input("enter name")
#     phone=input("enter phone number")
#     phonebook.pop(name)
#     print(phonebook)
# def updatecontact():
#     print("1.name \n 2.phone ")
#     option2=int(input("enter the option"))
#     if option2==1:
#             oldname=input("enter name")
#             newname=input("enter name")
#             phonebook[newname]=phonebook.pop(oldname)
#             print(phonebook)
#     if option2==2:
#             oldnumber=input("enter phone number")
#             newnumber=input("enter new number")
#             phonebook[newnumber]=phonebook.pop(oldnumber)
#             print(phonebook)
# def displaycontact():
#       print(phonebook)
# while(True):
#       print("MENU \n 1.Add \n 2.Delete \n 3.Update \n 4.Display \n 5.Exit")
#       option=int(input("enter choice"))
#       if option==1:
#             addcontact()
#       elif option==2:
#             deletecontact()
#       elif option==3:
#             updatecontact()
#       elif option==4:
#             displaycontact()
#       elif option==5:
#             exit()     
# 
# EXPENSE TRACKER USING FUNCTIONS
# exptracker={}
# wallet=1000
# def addexpense():
#      global wallet
#      expname=input("enter the expense name:")
#      if expname in exptracker:
#          amount1=int(input("enter the amount1:"))
#          amount=exptracker[amount]+amount1
#          exptracker.update({expname:amount1})
#          wallet=wallet-amount1
#          print(wallet)
#          print(exptracker)
#      else:
#       amount=int(input("enter the amount"))
#       if amount>wallet:
#             print("unsufficient balance")
#             print("current balance",wallet)
#       else:
#             exptracker.update({expname:amount})
#             wallet=wallet-amount
#             print(exptracker)
#             print("balance is:",wallet)
# def addbalance():
#      global wallet
#      newbalance=int(input("enter new balance"))
#      wallet=wallet+newbalance
#      print(wallet)
# def viewbalance():
#      print("total expenses:",exptracker)
# while(True):
#      print("MENU \n 1.add expense \n 2.add balance \n 3.view balance \n 4.exit")
#      option=int(input("enter the choice"))
#      if option==1:
#           addexpense()
#      elif option==2:
#           addbalance()
#      elif option==3:
#           viewbalance()
#      elif option==4:
#           exit()                         
#REVISION


# n=int(input('enter the number:'))
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# f=factorial(n)
# print(f)    


def sum_dig(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_dig(n//10)
print("sum of digits:",sum_dig(123))   
             

                  
          
             

                   
        


