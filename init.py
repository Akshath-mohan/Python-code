"""class Student:
   def _init_(self, fname, lname, age, section):
       self.firstname = fname
       self.lastname = lname
       self.age = age
       self.section = section
       def _str_(self):
        return f"Student({self.firstname} {self.lastname}, Age: {self.age}, Section: {self.section})"
stu1 = Student("Sara","Ansh",22,"A2")
# print(stu1._init_(self,fname,lname,age,section))
print("ln",stu1.firstname)
print(stu1.lastname)
print(stu1.age)
"""

class Student:
   def __init__(self, fname, lname, age, section):
       self.firstname = fname
       self.lastname = lname
       self.age = age
       self.section = section

   def __str__(self):
       return f"Student({self.firstname} {self.lastname}, Age: {self.age}, Section: {self.section})"


stu1 = Student("Sara", "Ansh", 22, "A2")
print(stu1)    ##or the next line
print(stu1.firstname,stu1.lastname,stu1.age,stu1.section)
print("mohan\naksh")