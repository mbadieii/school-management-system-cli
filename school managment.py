class  Course:
    id:int=0
    name:str=""
    units:int=0
    score:float=0.0
    def __init__(self,id,name,units):
        self.id=id
        self.name=name
        self.units=units
    def __str__(self):
        return f"id:{self.id},name:{self.name},units:{self.units}"

    def __eq__(self, other):
            if isinstance(other,int):
                return self.id==other
            elif isinstance (other,Teacher):
                return self.id==other.id
            
            return False
    
class Student:
    id:int=0
    name:str=""
    family:str=""
    courses:list[Course]=[]

    def __init__(self,id,name,family):
            self.id=id
            self.name=name
            self.family=family

    def __str__(self):
        return f"id:{self.id},name:{self.name},family:{self.family}"

    def __eq__(self, other):
        if isinstance(other,int):
            return self.id==other
        elif isinstance (other,Student):
            return self.id==other.id
        
        return False


class Teacher:
    id:int=0
    name:str=""
    family:str=""
    grade:str=""
    courses:list[Course]=[]

    def __init__(self,id,name,family,grade):
        self.id=id
        self.name=name
        self.family=family
        self.grade=grade
    def __str__(self):
         return f"id:{self.id},name:{self.name},family:{self.family},grade:{self.grade}"

    def __eq__(self, other):
        if isinstance(other,int):
            return self.id==other
        elif isinstance (other,Teacher):
            return self.id==other.id
        
        return False
    
class Classroom:
    id:int=0
    name:str=""
    course:Course
    teacher:Teacher
    students:list[Student]=[]
    def __init__(self,id,name):
        self.id=id
        self.name=name
               

class School:
    name:str=""
    courses:list[Course]=[]
    teachers:list[Teacher]=[]
    students:list[Student]=[]
    def __init__(self,name):
        self.name=name

    def show_students(self):
        for student in self.students:
            print(student)
         

    def show_teachers(self):
         for teacher in self.teachers:
            print(teacher) 

    def show_courses(self):
        for course in self.courses:
            print(course)

    def add_student(self,s):
        if  s in self.students:
             print("already exist")
        else:
            self.students.append(s)

    def add_teacher(self,t):
        if t in self.teachers:
            print("already exist")
        else:
            self.teachers.append(t)   

    def add_course(self,c):
        if c in self.courses:
            print("already exist")
        else:
            self.courses.append(c)

    def delete_student(self,id):
        if id not in self.students:
            print("dosent exist")
        else:
            self.students.remove(id)
    
    def delete_teacher(self,id):
        if id not in self.teachers:
              print("dosent exist")
        else:
             self.teachers.remove(id)
    def delete_course(self):
        if id not in self.courses:
              print("dosent exist")  
        else:
              self.courses.remove(id)
           



sc1=School("sama")


level="root"
while True:
    if level== "root":
        print("1. students")
        print("2. teachers")
        print("3. courses")
        print("4. classrooms")
        print("5. save")
        print("0. exit")
        cmd=int(input(">>:"))
        if cmd == 1:
            level= "students"
        elif cmd == 2:
            level = "teachers"
        elif cmd == 3:
            level= "courses"
        elif cmd == 4:
            pass
        elif cmd == 5:
            pass
        elif cmd == 0:
            break

    elif level == "students" :
        print("1. show student")
        print("2. add student")
        print("3. edit student")
        print("4. delete student")
        print("5. select student")
        print("0. back")
        cmd =int(input(">>:"))
        if cmd == 1:
             sc1.show_students()
                #for student in sc1.students:
                     #print(student)
        elif cmd == 2:
                id=int(input("id :"))
                name=input("name :")
                family=input("family :")
                s1=Student(id,name,family)
                sc1.add_student(s1)
        elif cmd == 3:
                pass
        elif cmd == 4:
              id=input(int("id:"))       
              sc1.delete_student(id)
              #s1=Student(id,"","")
              #sc1.student.remove(s1)
        elif cmd == 5:
                pass
        elif cmd == 0:
                level ="root"
    elif level == "teachers":
            print("1. show teacher")
            print("2. add teacher")
            print("3. edit teacher")
            print("4. delete teacher")
            print("5. select teacher")
            print("0. back")
            cmd =int(input(">>:"))
            if cmd == 1:
                 sc1.show_teachers()
                 #for teacher in sc1.teachers:
                      #print(teacher)
            elif cmd == 2:
                id=int(input("id :"))
                name=input("name :")
                family=input("family :")
                grade=input("grade :")
                t1=Teacher(id,name,family,grade)
                sc1.add_teacher(t1)
            elif cmd == 3:
                pass
            elif cmd == 4:
                id=input(int("id:"))
                t1=Teacher(id,"","")
                sc1.teachers.remove(t1)
            elif cmd == 5:
                pass
            elif cmd == 0:
                    level ="root"    
    elif level == "courses":
            print("1. show courses")
            print("2. add courses")
            print("3. edit courses")
            print("4. delete courses")
            print("0. back")
            cmd =int(input(">>:"))
            if cmd == 1:
                 sc1.show_courses()
                #for course in sc1.course:
                    #print(course)
            elif cmd == 2:
                id=int(input("id :"))
                name=input("name :")
                units=input("units :")
                c1=Course(id,name,units)
                sc1.add_course(c1)
            elif cmd == 3:
                pass
            elif cmd == 4:
                id=input(int("id:"))
                c1=Course(id,"","")
                sc1.courses.remove(c1)
            elif cmd == 0:
                    level ="root"    


           