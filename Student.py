class Student:
    school="Software"
    def __init__(self,f_name,l_name,email):
        self.f_name=f_name
        self.l_name=l_name
        self.email=email
        
    def enrol(self):
        print("Student enrolled")


student1= Student("John","Smith","john@gmail.com")
student2= Student("John1","Smith","john@gmail.com")
student3= Student("John2","Smith","john@gmail.com")
student4= Student("John3","Smith","john@gmail.com")

print(student4.f_name, student1.f_name,Student.school)

student4.f_name="Ben"
Student.school="IT"

student1.enrol()
print(student4.f_name, student1.f_name,Student.school)