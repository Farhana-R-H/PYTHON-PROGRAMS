#extract the digit 456
# num=456
# while num>0:
#     dig=num%10
#     num=num//10
#     print(dig)

#calculate the sum of the digit 456
# sum=0
# num=456
# while num>0:
#     dig=num%10
#     num=num//10
#     sum=sum+dig
# print(sum)    

#calculate the sum of any digit
# num=int(input("enter a value"))
# sum=0
# while num>0:
#     dig=num%10
#     num=num//10
#     sum=sum+dig
#     print(sum)

def sum_of_digits():
    num=int(input('enter a value:'))
    sum=0
    while num>0:
        dig=num%10
        num=num//10
        sum=sum+dig
print("sum of digits is",sum)
sum_of_digits()        

#numbers btn 1000 and 3000 such that each idigit if the number is even

# for i in range(1000,3001):
#     flag=True
#     temp=i
#     while i>0:
#         dig=i%10
#         if dig%2==0:
#             flag=False
#     i=i//10
#     if flag==True:
#         print(temp)   
        
         
