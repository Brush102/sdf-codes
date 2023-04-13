class Person:
    school="IT"
    counter_id=202020
    def __init__(self,f_name,l_name,email):
        self.f_name=f_name
        self.l_name=l_name
        self.email=email
        self.ID=Person.school+str(Person.counter_id)
        Person.counter_id+=1
    def __str__(self) -> str:
        return "First Name: "+self.f_name+"\nLast Name:"+self.l_name+"\nEmail:" + self.email + "\nID:"+ self.ID
    

class Student(Person):
    courses=[]
    def __init__(self, f_name, l_name, email,program):
        super().__init__(f_name, l_name, email)
        self.program=program
    def __str__(self) -> str:
        return "First Name: "+self.f_name+"\nLast Name:"+self.l_name+"\nEmail:" + self.email + "\nID:"+ self.ID + "\nProgram:"+self.program
    def enrol(self,course):
        self.courses.append(course)
class Course:
   students=[]
   def __init__(self,c_name):
       self.c_name=c_name
   def __str__(self):
       return "Course name:" + self.c_name
   def add_student(self, student):
       self.students.append(student)
class Main():
    students=[]
    courses=[]
    @staticmethod
    def main():
        
        while True:
            
            print("1. Create Student ")
            print("2. View Student ")
            print("3. Create Course ")
            print("4. View Course ")
            print("5. Enrol a student ")
            print("6. Display all courses of a student")
            print("7. Exit")

            option=int(input("Please select an option: "))

            match option:
                case 1:
                    f_name=input("Please enter first Name ")
                    l_name=input("Please enter last Name ")
                    email=input("Please enter email ")
                    program=input("Please enter program Name ")
                    student=Student(f_name,l_name,email, program)
                    print(student)
                    Main.students.append(student)
                case 2:
                    s_ID=input("Please enter student ID ")
                    student=None
                    for x in Main.students:
                         if x.ID == s_ID:
                            student=x
                            break
                       #student=  next((x for x in Main.students if x.ID == s_ID), None)
                    if student != None:
                        print(student)
                    else: 
                        print("No Student found with this ID ")
                case 3:
                    c_name=input("Please enter course Name ")
                    course=Course(c_name)
                    print(course)
                    Main.courses.append(course)
                case 4:
                    c_name=input("Please enter course name ")
                    course=None
                    for x in Main.courses:
                         if x.c_name == c_name:
                            course=x
                            break
                    if course != None:
                        print(course)
                    else:
                        print("No course found with this name ")
                case 5:
                     s_ID=input("Please enter student ID ")
                     c_name=input("Please enter course Name ")
                     student=None
                     for x in Main.students:
                         if x.ID == s_ID:
                            student=x
                            break
                     if student != None:
                        course=None
                        for x in Main.courses:
                         if x.c_name == c_name:
                            course=x
                            break
                        if course != None:
                            student.enrol(course)
                            course.add_student(student)
                            print(student.f_name, " Enrolled to ", course.c_name )
                        else:
                            print("No course found with this name ")
                     else:
                        print("No Student found with this ID ")
                case 6:
                    s_ID=input("Please enter student ID ")
                    student=None
                    for x in Main.students:
                        if x.ID == s_ID:
                            student=x
                            break
                    if student != None:
                        print(student.ID + "is registered in:")
                        for course in student.courses:
                            print(course)
                    else: 
                        print("No Student found with this ID ")
                case 7:
                    break
                case _:
                    print("Incorrect Option Selected ")
                    continue


Main.main()



