class  Course:
    id:int=0
    name:str=""
    units:int=0
    score:float=0.0
    def __init__(self,id,name,units):
        self.id=id
        self.name=name
        self.units=units
    
class Student:
    id:int=0
    name:str=""
    family:str=""
    courses:list[Course]=[]

    def __init__(self,id,name,family):
            self.id=id
            self.name=name
            self.family=family
        



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
                pass
        elif cmd == 2:
                id=int(input("id :"))
                name=input("name :")
                family=input("family :")
                s1=Student(id,name,family)
                sc1.students.append(s1)
        elif cmd == 3:
                pass
        elif cmd == 4:
                pass
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
                pass
            elif cmd == 2:
                id=int(input("id :"))
                name=input("name :")
                family=input("family :")
                grade=input("grade :")
                t1=Teacher(id,name,family,grade)
                sc1.teachers.append(t1)
            elif cmd == 3:
                pass
            elif cmd == 4:
                pass
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
                pass
            elif cmd == 2:
                id=int(input("id :"))
                name=input("name :")
                units=input("units :")
                c1=Course(id,name,units)
                sc1.courses.append(c1)
            elif cmd == 3:
                pass
            elif cmd == 4:
                pass
            elif cmd == 0:
                    level ="root"    
    