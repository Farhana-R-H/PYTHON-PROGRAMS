#
# class Student:
#     def __init__(self):
#         self.name=" "
#         self.rollno=" "
#         self.mark1=" "
#         self.mark2=" "
#         self.mark3=" "
#         self.average=0
#         self.grade=" "
#         self.total_marks=0

#     def student_data(self):
#         self.name=str(input("enter name"))
#         self.rollno=int(input("enter roll no"))
#         self.mark1=int(input("mark1:"))
#         self.mark2=int(input("mark2:"))
#         self.mark3=int(input("mark3:"))
#     def calculation(self):
#         self.average=(self.mark1+self.mark2+self.mark3)/3
#         self.total_marks=self.mark1+self.mark2+self.mark3
#     def student_grade(self):
#         if self.average>=90 and self.average<=100:
#             self.grade="A"
#         elif self.average>=80 and self.average<=89:
#             self.grade="B"
#         elif self.average>=70 and self.average<=79:
#             self.grade="C" 
#         elif self.average>=60 and self.average<=69:
#             self.grade="D" 
#         elif self.average<60:
#             self.grade="FAIL"                   
#     def print_data(self):
#         print(self.name,"\t",self.rollno,"\t",self.total_marks,"\t",self.grade,"\t",)
# students=[]
# n=int(input("enter no of students"))
# for i in range(n):
#     obj=Student()
#     students.append(obj)
# for i in students:
#     i.student_data()
#     i.calculation()
#     i.student_grade()
# print("name","\t","roll no","\t","total","\t","grade","\t")    
# for i in students:
#     i.print_data()


#voting
class Vote:
    def __init__(self):
        self.name=" "
        self.age=" "
        self.eligible=" "
    def vote_data(self):
        self.name=str(input("enter name"))
        self.age=int(input("enter age"))
    def voter_age(self):
        if self.age>=18:
            self.eligible="ELIGIBLE"
        else:
            self.eligible="NOT ELIGIBLE"
    def print_data(self):
        print(self.name,"\t",self.eligible,"\t")        
vote=[]
n=int(input("no of voters"))
for i in range(n):
    obj=Vote()
    vote.append(obj)
for i in vote:
    i.vote_data()
    i.voter_age()
print("name \t\t eligibility")    
for i in vote:
    i.print_data()        







    

