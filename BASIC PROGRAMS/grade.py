#grade of students
sub1=int(input("mark1"))
sub2=int(input('mark2'))
sub3=int(input("mark3"))
average=((sub1+sub2+sub3)/3)
print(average)
if average>=90 and average<=100:
    print("A GRADE")
elif average>=80 and average<=89:
    print("B GRADE")
elif average>=70 and average<=79:
    print("C GRADE") 
elif average>=60 and average<=69:
    print("D GRADE") 
else:
    print("FAIL")              