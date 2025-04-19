# palindrome
# num=int(input('value'))
# temp=num
# rev=0
# while num>0:
#     dig=num%10
#     num=num//10
#     rev=rev*10+dig
# print(rev)
# if temp==rev:
#     print(rev,"is palindrome")
# else:
#     print(rev,"is not palindrome")   

#checking substring occurance
txt=input("enter a string")
sub=input("enter a string")
if sub in txt:
    print(sub,"is a substring")
else:
    print(sub,"is not a substring")    














#palindrome btn 1 and 500
# for i in range(1,500):
#     rev=0
#     temp=i
#     while i>0:
#         dig=i%10
#         i=i//10
#         rev=rev*10+dig
#     if temp==rev:
#         print(temp)    