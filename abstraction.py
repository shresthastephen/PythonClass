# from abc import ABC, abstractmethod

# class Lecturer(ABC):
    
#     @abstractmethod
#     def introduce():
#         ...


# class FullTime(Lecturer):
#     def introduce():
#         pass

# FullTeacher = FullTime()



class Lecturer():
    def __init__(self,name,department):
        self.department=department
        self.name=name

    def job(self):
        print('I teach')

class Employee():
    ...

class FullTime(Lecturer, Employee):
    # def __init__(self, name, department,designation):
    #     super().__init__(name, department)
    #     self.degnation=designation

    def __init__(self, name, department,shift):
        Employee.__init__(self,name

        )


    def job(self):
        print('teach Fulltime')

lecturer=Lecturer('ABC','BCA')
print (lecturer.name)
print (lecturer.department)

flecturer = FullTime('dfg', 'BCA', 'HOD')
print(flecturer.name +":"+flecturer.degnation)