#write a fun to check if two strings are balanced,for example two strings have same charecters in it position doesnt matter
# def function():
#     s1=(input("enter the first sentence:"))
#     s2=(input("enter the second sentence:"))
#     flag=True
#     for i in s1:
#         if i not in s2:
#             flag=False
#     if flag==True:
#         print("two strings are balanced")
#     else:
#         print("two strings are not balanced")                            
# function()

#write a program to arrange the charecters of a string so that all lowercase letters should come first
# def function():
#     str=input("enter the string")
#     list1=[]
#     list2=[]
#     for i in str:
#         if i.islower()==True:
#             list1.append(i)
#         else:
#             list2.append(i)
#     res=" ".join(list1+list2)
#     print(res)
# function()

#write a program to return the sum of digits that appear in the string ignoring all other charecters
# def function():
#     s=input("enter value")
#     sum=0
#     for i in s:
#         if i.isdigit()==True:
#             sum+=int(i)
#     print(sum)
# function()            

def function():
    str=input('enter sentence')
    res=""
    for i in str:
        if i.isalnum()==False:
            res+="#"
        else:
            res+=i 
    print(res)
function()                          
