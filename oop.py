# # # print("hello! i am Om. I study python.")
# # # name = " Om Ratna"
# # # subject = "BCA"
# # # def main(name,subject):
# # #     studet=getStudent()
# # #     print(f'myname is {name} my faculty is {subject}')

# # # def getStudent():
# # #     return 'name','python'
# # # name, subject = getStudent()
# # # result = main(name,subject)
# # # print(result)

# # # if(__name__=='__main__'):
# # #     main()
# # # name = input("enter a name")
# # # roll=input("enter a roll")
# # # print(name,roll)
# # def main():
# #     student=getstudent()
# #     student[0]="hari"
# #     print(f"hii om{student[0]},{student[1]}")

# #     def getstudent():
# #         return("om",'python')
# # if(__name__=='__main__'):
# #      main()

# class student():
#     def __init__(self):
#         self.name=input("enter name  ")
#         self.subject=input('subject')

# Student=student()
# print(f'{Student.name}')
# # print(type(student))



# # name = input "input the name"
# # roll = input "name"
# # print(f'i am {name},i study {roll}')
    

class Student:
    offered = ['AI', 'SPM', 'EGOV', 'DBA']  # Class-level list of offered subjects

    def __init__(self, name, subject):
        if not name:
            raise ValueError('naaaaam khai')
        else:
            self.name = name
        
        if subject not in Student.offered:
            raise ValueError('Please Select given options')
        else:
            self.subject = subject  # This will call the setter

    def __str__(self):
        return f'''
Name: {self.name}
Elective is: {self.subject}
'''

    @property
    def subject(self):
        return self._subject  # Access the private variable

    @subject.setter
    def subject(self, subject):
        if subject in Student.offered:
            self._subject = subject
        else:
            raise ValueError('Please Select from the given options')

def getStudent():
    name = input("name: ")
    subject = input("Subject: ")
    
    return Student(name, subject)

# Test the implementation
student = getStudent()
student.name=''
print(f'I am {student.name}. I have selected {student.subject}')
print(student)

# You can also test changing the subject if needed
# student.subject = "networking"  # This will raise an error if it's not valid



