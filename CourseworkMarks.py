import getpass
import sys

password = '1234'
studentList = []


class Student:
    '''This is the class that holds the coursework marks for a particualr student'''

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courseworkOne = 0
        self.courseworkTwo = 0
        self.courseworkThree = 0


    def getName(self):
        return self.name

    def setCoursework(self, type, mark):
        if type == 1:
            self.courseworkOne = mark
        elif type == 2:
            self.courseworkTwo = mark
        else:
            self.courseworkThree = mark

    def getCoursework(self, type):
        if type == 1:
            return self.courseworkOne
        elif type == 2:
            return self.courseworkTwo
        else:
            return self.courseworkThree

def calculateModuleMark(courseworkOne, courseworkTwo, courseworkThree):
    return ((courseworkOne * 0.2) + (courseworkTwo * 0.3) + (courseworkThree * 0.5))


def displayStudentMarks():
    name = input('What is the name of the student that you want to see ? \n:')
    for x in studentList:
        if name == x.name :
            print(str("Student : " + x.name+"\nCoursework 1:" + str(x.courseworkOne) +"    Coursework 2: "+
                  str(x.courseworkTwo) +"   Coursework 3: "+ str(x.courseworkThree)+ "    Module Mark : "+
                         str(calculateModuleMark(x.courseworkOne, x.courseworkTwo, x.courseworkThree))))

def enterMarks(param):
    print(param)
    for x in studentList:
        mark = int(input("what is " + x.name + " coursework " + str(param) + " mark? \n :"))
        x.setCoursework(param,mark)




def mainmenu():
    ok = True
    while (ok == True):
        choice = int(input("\n1. Enter marks for course work 1 "+
                    "\n2. Enter marks for course work 2"+
                    "\n3. Enter marks for course work 3"+
                    "\n4. Display a particular student’s marks"+
                    "\n5. Supervisor mode"+
                    "\n6. Exit program\n"))
        if choice == 1:
            enterMarks(1)
        elif choice == 2:
            enterMarks(2)
        elif choice == 3:
            enterMarks(3)
        elif choice == 4:
            displayStudentMarks()
        elif choice == 5:
            supervisorMode()
        elif choice == 6:
            ok = False
        else:
            print("unrecognised input")


def changeStudentName():
    found = False
    currentName = ('Which student would you like to change')
    param = input('What is the new name')
    for x in studentList :
        if x.name == param:
            found == True
            print(x.name +"has been changed to " + param)
            x.name = param
    if found == False:
        print('name not found')


def changeParticularMark():
    studentname = input('what is the name of the student: ')
    found = False
    while found == False :
        for x in studentList:
            if studentname == x.name:
                found = True
    if found == False :
        print("Student not Found")
    else:
        changer = int(input("which mark would you like to change?"
                            "\nPress 1 for coursework 1"
                            "\nPress 2 for coursework 2"
                            "\nPress 3 for coursework 3\n: "))
        if changer != 1 or changer != 2 or changer != 3:
            print('unrecognised input')
        if changer == 1:
             enterMarks(changer)

def AddAStudent():
    number = studentList.length + 1
    name = input("What is the name of this student:")
    marksOne = float(input("what is the coursework One marks? "))
    marksTwo = float(input("what is the coursework Two marks? "))
    marksThree = float(input("what is the coursework Three marks? "))
    studentList.append(Student(number,name))
    for x in studentList:
        if x.name == name:
            x.courseworkOne = marksOne
            x.courseworkTwo = marksTwo
            x.courseworkThree = marksThree




def supervisorMode():
    sys.stdout.flush()
    passwordCheck = input("what is the password? : ")

    if passwordCheck == password:
        passedCheck = True
        ok = True
        while passedCheck and ok:
            arguement = input(" a) To change the pin number" +
                             "\n b) To change a particular mark" +
                             "\n c) To add a student" +
                             "\n d) To correct a student’s name." +
                             "\n e) To return to the main menu " +
                             "\n: ")


            if arguement == "a":
                changePin()
            elif arguement == "b":
                changeParticularMark()
            elif arguement == "c":
                 AddAStudent()
            elif arguement =="d":
                changeStudentName()
            elif arguement == "e":
                 ok = False
            else:
                print('Unrecognised input...')
                ok = False

    else:
        print("The Password is incorrect")


def changePin():
        newPin = input("enter the new password")
        password = newPin
        print("this pin has been changed")


def newStudent(name, number):
    studentList.append(Student(name, number))


def main():
    numberOfStudents = int(input("how many students are there ? :"))
    x = 0
    while x < numberOfStudents :
        newStudent(input("what is the name of the student?:  "), x)
        x = x+1
    mainmenu()


if __name__ == "__main__":

    main()
