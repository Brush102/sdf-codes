class Student:
    country="NZ"
    def __init__(self,name, email, address, campus):
        self.name=name
        self.email=email
        self.address=address
        self.campus=campus+Student.country
    def printStudent(self):
        print("Student Name:", self.name)
        print("Student email",self.email)
        print("Student campus",self.campus)
    def changeCampus(self,campus):
        self.campus=campus+Student.country

student1=Student("BEn","ben@gasg","10B Some street", "W")

student1.printStudent()
student1.changeCampus("Auck")
student1.printStudent()