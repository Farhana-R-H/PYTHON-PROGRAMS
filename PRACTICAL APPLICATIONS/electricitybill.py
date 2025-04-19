#electricity bill
n=int(input("no of units"))
if 1<=n<100:
    bill=n*10
    print("bill is",bill)
elif 100<=n<200:
    bill=(99*10)+((n-99)*15)
    print("bill is",bill) 
elif 200<=n<300:
    bill=(99*10)+(99*15)+(n-199)*20
    print("bill is",bill)
elif n<=300:
    bill=(99*10)+(99*15)+(199*20)+(n-299)*25
    print("bill is",bill)      
