#sum of first 10 numbers
# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print(sum)    
#factorial
# n=int(input("enter value"))
# i=1
# factorial=1
# while i<=n:
#     factorial=factorial*i
#     i=i+1
# print(factorial)  

#sum of even numbers
n=int(input("enter the number"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i
print("sum of even number is",sum)
