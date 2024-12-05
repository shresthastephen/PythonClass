class Student:
    offered = ['AI', 'SPM', 'EGOV', 'DBA']  # Class-level list of offered subjects

    def __init__(self, name, subject):
        # Validate the name during initialization
        self.name = name  # This will call the setter for name
        # Validate the subject during initialization
        self.subject = subject  # This will call the setter for subject

    def __str__(self):
        return f'''
Name: {self.name}
Elective is: {self.subject}
'''

    @property
    def name(self):
        return self._name  # Access the private variable for name

    @name.setter
    def name(self, value):
        if not value:  # If the name is empty, raise an error
            raise ValueError('naaaaam khai')  # Validation message
        self._name = value  # Set the private _name variable

    @property
    def subject(self):
        return self._subject  # Access the private variable for subject

    @subject.setter
    def subject(self, subject):
        if subject in Student.offered:  # If the subject is valid, set it
            self._subject = subject
        else:
            raise ValueError('Please Select from the given options')  # Validation message

def getStudent():
    name = input("name: ")
    subject = input("Subject: ")
    return Student(name, subject)

# Test the implementation
try:
    # Test case 1: Creating a valid student
    student = getStudent()  # Let the user input name and subject
    print(f'I am {student.name}. I have selected {student.subject}')
    print(student)
    
    # Test case 2: Try to set the name to an empty string
    student.name = ''  # This will raise an error since name cannot be empty
except ValueError as e:
    print(e)

# Test case 3: Try to set the subject to an invalid subject
try:
    student.subject = "networking"  # This will raise an error if it's not a valid subject
except ValueError as e:
    print(e)
