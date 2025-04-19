#check if a number is perfect 
n=int(input("enter the value"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")   

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#  


#check perfect numbers between 1 and 100
# for i in range(1,100):
#     sum=0
#     for j in range(1,i):
#         if i%j==0:
#             sum=sum+j
#     if sum==i:
#         print(i)    
    
