#occurence of a character in a string
# txt=str(input("name of string:"))
# a=str(input("name the character:"))
# print(txt.count(a))

#check a given substring present in the string
txt=str(input("name of the string:"))
a=str(input("name the character:"))
if txt.count(a)>=1:
    print("the substring is present")
else:
    print("the substring is not present")    