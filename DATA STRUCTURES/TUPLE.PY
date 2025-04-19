#tuple
# tuple1=(1,3,5.5,"hi","hello",25)
# print(len(tuple1))
# print(tuple1[0])
# print(tuple1[-1])
# print(tuple1[:2])
# print(tuple1[3:])
# #merging
# tuple2=(35,45,65)
# tuple3=tuple1+tuple2
# print(tuple3)
# #count and indexing
# print(tuple1.count(5.5))
# print("indexing position is",tuple1.index(5.5))
# #converting tuple to list
# list1=list(tuple1)
# print(list1)
# #reconverting list to tuple
# tuple1=tuple(list1)
# print(tuple1)

#program to unpack a tuple
# tuple1=(10,20,30,"hi",100,"hello")
# a,b,c,d,e,f=tuple1
# print(a)
# print(f)

#tuple to string
# tuple1=("hi","hello","how","are","you")
# join=" ".join(tuple1)
# print(join)

#program to get 4th element from first and last
# tuple1=(1,2,3,4,"hi","hello",45)
# print(tuple1[3],tuple1[-4])

#repeated elements
tuple1=(10,20,20,30,45,45,60)
res=[]
rep=0
for i in tuple1:
    if i not in res:
        res.append(i)
    else:    
        rep+=1
print(rep)        

#remove an empty temple
# list1=[(),("a","b"),("a","b","c"),("d",),()]
# res=[]
# for i in list1:
#     if i!=():
#         res.append(i)
# print(res)   

# tuple1=(11,44,22,33,44,55,66,55)
# list1=list(tuple1)
# res=[]
# for i in list1:
#     if i==44 or i==55:
#         res.append(i)
# print(tuple(res))

#modify
# tuple1=(11,[22,33],44,55)
# list1=list(tuple1)
# list1[1][0]=222
# print(tuple(list1))        
        


