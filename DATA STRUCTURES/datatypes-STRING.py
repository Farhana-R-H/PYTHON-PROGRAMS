#data types
# txt="how old are you?"
# print(len(txt))
# print(txt[5])
# print(txt[11])
# print(txt[15])
# print(txt[-2])
# txt="""who are
#  you?"""
# print(len(txt))
# print(txt[12])
# print(txt[-5])
# print(txt[-3])
# print(txt[9])

#concatenation and slicing
# txt1=str(input("word:"))
# txt2=str(input("word:"))
# print(txt1[0:2]+txt2[-2:])

#hello to oellh
# txt=str(input("word:"))
# wor1=txt[-1]
# wor2=txt[0]
# wor3=txt[1]+txt[2]+txt[3]
# print(wor1+wor3+wor2)

#
# txt1=str(input("word:"))
# txt2=str(input("word:"))
# wor1=txt1[1]+txt1[0]+txt1[2:]
# wor2=txt2[1]+txt2[0]+txt2[2:]
# print(wor1+" "+wor2)

#
# txt=str(input("word"))
# n=int(input("index to be removed:"))
# word=txt[:n]+txt[n+1:]
# print(word)

#
# txt=str(input("word:"))
# if len(txt)>=3:
#     if txt[-3:]=="ing":
#         print(txt[:-3]+"ly")
#     else:
#         print(txt+"ing")  
# else:
#     print(txt)    

#remove 1st and last charecter
# txt=str(input("word:"))
# print(txt[1:-1])

#to reverse a string
# txt=str(input("word:"))
# print(txt[::-1])
# print(txt[::2])
# print(txt[::-2])

#string method using built in functions
txt="my name is farhana"
c=txt.capitalize()
print(c)
print(txt.upper())
print(txt.lower())
print(txt.casefold())
print(txt.isupper())
print(txt.islower())
print(txt.isalpha())
print(txt.isdigit())
print(txt.count("e"))
print(txt.index("e"))
print(txt.rindex("e"))
print(txt.find("f"))
print(txt.rfind("f"))
print(txt.replace("farhana","mannana"))
print(txt.strip())
print(txt.split())
print(txt.swapcase())
