#check if a number is prime
# n=int(input("enter the value"))
# count=0
# for i in range(1,n+1):
#     count=count+1
# if count==2 or n==5:
#     print(n,"is prime")
# else:
#     print(n,"is not prime")     
















     
# check prime numbers from 1 to 100

# for i in range(1,100):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         print(i)    








# prime using flag
num=int(input("value:"))
flag=True
if num<2:
    flag=False
for i in range(2,(num//2+1)):
    if num%i==0:
        flag=False
        break
if flag==True:
    print(num,"is a prime")
else:
    print(num,"is not a prime")            

#prime numbers within limits
# l=int(input("enter lower limit"))
# n=int(input("enter upper limit"))
# for i in range(1,n):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#         if count==2:
#             print(i)   

