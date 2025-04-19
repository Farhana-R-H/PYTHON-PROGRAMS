#biggest digit of a number
# n=int(input("number:"))
# temp=n
# a=0
# while n>0:
#     dig=n%10
#     if dig>a:
#         a=dig
#     n=n//10
# print("biggest digit is",a)  

#reverse a number
num=int(input("enter the value"))
r=0
while num>0:
    dig=num%10
    r=r*10
    r=r+dig
    num=num//10
print(r)    

