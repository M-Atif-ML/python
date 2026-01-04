# -------------------------------basic class concept---------------------------
# class myClass:
#     i = 1234
#
#     def f(self):
#         return "Hello world"
#
#
# obj = myClass()
# print(obj.f())
# #
# class Complex:
#     def __init__(self,realPart,imagPart):
#         self.r = realPart
#         self.i = imagPart
#
# complex_number = Complex(12,3)
# print(complex_number.r,complex_number.i)

#
# class A:
#     x = 0
#     def p(self):
#         print(self.x)
#
# a = A()
# a.p()
# a.x+=1
# a.x+=1
# print(a.x)
# b=  A()
# b.p()
# a.p();
#

# class B:
#     x = 0
#     def f(self):
#         print(self.x)
#
# c = B() # = B.f(c)
# cf = c.f
# c.x+=1
# cf()
#

# -------------class and instance variables-----------------
#
# class Dog:
#
#     def __init__(self,name):
#         self.name=name
#         self.tricks = []
#     def addNewTrick(self,trick):
#         self.tricks.append(trick)
#     def display(self):
#         print("Name: ",self.name)
#         print("Tricks:",self.tricks)
#
# d1=Dog("Simba")
# d1.addNewTrick("Jumping")
# d1.addNewTrick("Skimming")
# d1.display()
# d2 = Dog("Ted")
# d2.display()
#
#

# inheritance:
class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first =first
        self.last =last
        self.email = first+"."+last+"@gmail.com"
        self.pay =pay
    def fullName(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amt)

    def display(self):
        print("Name:",self.fullName())
        print("Email:",self.email)
        print("Pay:",self.pay)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang= prog_lang
    def display(self):
        Employee.display(self)
        print("Programming language:",self.prog_lang)


dev_1 = Developer("Corey","Schafer",5000,"Python")
dev_2 = Developer("Atif","Khan",9000,"Java")



dev_1.display()









