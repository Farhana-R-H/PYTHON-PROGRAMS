#write a program that tells if a number is "weird" or not
num=int(input("enter the value"))
if num%2==1 or 6<num<20:
    print(num,"is a weird number")
else:
    print(num,"is not weird")    