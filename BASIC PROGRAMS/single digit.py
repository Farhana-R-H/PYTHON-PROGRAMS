#sum of digit until the sum is a single digit
# num=int(input("enter the digit"))
# sum=0
# while num>0:
#     dig=num%10
#     num=num//10
#     sum+=dig
#     if num==0 or num<10:
#         sum=num
#         sum+=dig

# print("sum of digit is",sum)    





#converting binary to decimal and vice versa
num=int(input("enter the binary number:"))
count=0
sum=0
while num>0:
    dig=num%10
    num=num//10
    count=count+1
    for i in range(count):
        dec=dig*(2**i)
    sum=sum+dec
print("decimal number is",sum)        



#spy number
# n=int(input("enter the number"))
# sum=0
# a=1
# while n>0:
#     dig=n%10
#     n=n//10
#     sum=sum+dig
#     a=a*dig
# if dig==a:
#     print("it is a spy number") 
# else:
#     print("it is not a spy number") 










#strong number
n=int(input("enter the value:"))
temp=n
sum=0
fact=1
while n>0:
    dig=n%10
    n=n//10
    for i in range(1,dig+1):
        fact=fact*i
    sum=sum+fact
    fact=1
if sum==temp:
    print(temp,"is a strong number")
else:
    print("not a strong number")            