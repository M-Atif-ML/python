from pygments.lexer import default


class Student:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age =age
    def show(self):
        print("Id: ",self.id)
        print("Name: ",self.name)
        print("Age: ",self.age)
        


class SeniorStudent(Student):
    def __init__(self, id, name, age, fypTitle, fypSupervisor):
        Student.__init__(self, id, name, age)
        self.fypTitle = fypTitle
        self.fypSupervisor = fypSupervisor
    def show(self):
        Student.show(self)
        print("Fyp title: ",self.fypTitle)
        print("Fype supervisor: ",self.fypSupervisor)



class DataBase:
    def __init__(self):
        self.data = []

    def add(self,id,name,age,fypTitle,fypSupervisor):
        self.data.append(SeniorStudent(id,name,age,fypTitle,fypSupervisor))

    def display(self):
        if(len(self.data) < 1):
            print("Nothing to display")
            return None
        for info in self.data:
            print(info.show())
    def age_filter(self,threshold , direction = 'f' ):
        if(direction == 'f' or direction == 'F'):
            return self.data[threshold:]
        elif(direction == 'b' or direction == 'B'):
            return self.data[:threshold+1]


def main():
    students = DataBase()

    while True:
        choice = input("Enter choice: ")
        if(choice == 'a' or choice =='A'):
            id = input("Enter Student id: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            fypTitle=input("Enter fyp title: ")
            fypSupervisor=input("Etner supervisor name: ")
            students.add(id,name,age,fypTitle,fypSupervisor)

        elif(choice == 'd' or choice =='D'):
            students.display()
        elif(choice =='e' or choice =='E'):
            break

main()