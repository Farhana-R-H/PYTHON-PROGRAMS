#to find the largest among three numbers
# a=int(input("enter first value:"))
# b=int(input("enter second value:"))
# c=int(input("enter third value:"))
# if a>b and a>c:
#     print(a,"is the largest number")
# elif b>a and b>c:
#     print(b,"is the largest number")   
# else:
#     print(c,"is the largest number") 


#nested if
a=int(input('value')) 
b=int(input('value'))
c=int(input('value')) 
if a>=b:
    if a>=c:
        print(a,"is larger")
    else:
        print(c,"is larger")
else:
    if b>=c:
        print(b,"is larger")
    else:
        print(c,"is larger")    
