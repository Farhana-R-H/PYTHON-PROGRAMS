#find factorial of a number
# factorial=1
# for i in range(1,3):
#     factorial=factorial*i
# print(factorial)    






# n=int(input("enter the value:"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#       print("factorial's are",i) 

 #sum of factors
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
   if i%2==0:
      print(i)
      sum=sum+i
print("sum of factors are:",sum)      
           