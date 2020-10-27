#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""


class student:

    # properties should be listed first
    name = ""
    studentNumber = ""
    grade = 0
    listCourses = []
    listGrades = []

    # You will need to create your own input parameters for all methods
    def __init__(self, name, studentNumber, grade, listCourses=[], listGrades=[]):
        self.name = name
        self.studentNumber = studentNumber
        self.grade = grade
        self.listCourses = listCourses
        self.listGrades = listGrades

    def average(self):
        averageGrade = sum(self.listGrades) / len(self.listGrades)
        return averageGrade

    def getHonorRoll(self):
        self.listGrades.sort()
        self.listGrades.reverse()
        averageGrades5 = (self.listGrades[0] + self.listGrades[1] + self.listGrades[2] + self.listGrades[3] + self.listGrades[4]) / 5
        if averageGrades5 >= 86:
            return True
        else:
            return False

    def showCourses(self):
        print(self.listCourses)

    def index(self):
        index = input("Enter a index: ")
        return int(index)

    def showGrade(self, index):
        print(self.listCourses[index])
        print(self.listGrades[index])

    def getCourses(self, listCourses):
        self.listCourses = listCourses

    def getGrades(self, listGrades):
        self.listGrades = listGrades

    def constructor(self):
        print(self.name + " " + str(self.studentNumber) + " " + self.grade)


def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath", "91334", 11)
    st1.getCourses(["English", "Math", "PE", "Computers",
                    "History", "Biology", "Japanese"])
    st1.getGrades([91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox", "12346", 11)
    st1.getCourses(["English", "Math", "Physics", "Computers",
                    "Geography", "Chemistry", "French"])
    st1.getGrades([71, 98, 93, 95, 68, 81, 71])


main()
