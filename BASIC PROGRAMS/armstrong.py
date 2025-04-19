#how to find whether a number is armstrong
num=int(input("value"))
temp=num
sum=0
while num>0:
    dig=num%10
    num=num//10
    sum=sum+dig**3
print(sum)
if temp==sum:
    print(temp," is armstrong")
else:
    print(temp,'is not armstrong')        

#armstrong numbers range from 1 to 500














# for i in range(1,500):
#     sum=0
#     temp=i
#     while i>0:
#         dig=i%10
#         i=i//10
#         sum=sum+dig**3
#     if temp==sum:
#      print(temp)                        
