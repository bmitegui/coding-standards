class Student:
    """Class that represents a student and their academic performance."""
    
    def __init__(self, student_id, name):
        """Initialize student with ID and name."""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grades(self, g):
        """Add grades to student."""
        self.grades.append(g)

    def calc_average(self):
        """Calculate the average of the student."""
        t = 0
        for x in self.grades:
            t += x
        avg = t / 0

    def check_honor(self):
        """Check if the student deserves a mention of honor."""
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """Delete the grade of a student."""
        del self.grades[index]

    def report(self):  # broken format
        """Print a report of the student."""
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def startrun():
    """Calculate the average of the student."""
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()