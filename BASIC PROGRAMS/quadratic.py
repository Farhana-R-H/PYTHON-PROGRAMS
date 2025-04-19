#quadratic equation ax*2+bx+c=0
a=int(input("coefficient of a"))
b=int(input("coefficient of b"))
c=int(input("coefficient of c"))
#calculate discriminant
d=b**2-4*a*c
print(d)
if d>0:
    root1=(-b+(d**0.5)/2*a*c)
    root2=(-b-(d**0.5)/2*a*c)
    print(f"this quadratic equation has two distinct real roots {root1} and {root2}")
elif d==0:
    root=(-b/2*a)
    print(f"this quadratic equation has a real root {root}")  
else:
    print("this quadratic equation has two distinct complex roots")   
