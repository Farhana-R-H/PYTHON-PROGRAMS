#print all numbers btn 1 and n that are divisible by both 3 and 5
n=int(input("enter the value"))
for i in range(1,n):
    if i%3==0 and i%5==0:
        print(i,"is divisible by 3 and 5")    