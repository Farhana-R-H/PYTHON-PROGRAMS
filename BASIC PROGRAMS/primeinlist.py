n=int(input("enter no of elements"))
list=[]
list1=[]
list2=[]
for i in range(n):
    num=int(input("enter elements"))
    list.append(num)
    if num%2==0:
        list1.append(num)
    else:
        num%2==1
        list2.append(num)
print(list)            
print("list of even numbers:",list1)
print("list of odd numbers:",list2)        
       
