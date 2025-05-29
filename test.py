""" Initialize the class"""
class Student:
    """Class that represents a student and their academic performance."""
    def __init__(self, student_id, name):
        """Initialize student with ID and name."""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "No"
        self.honor = "?"

    def add_grades(self, grade):
        """Add grades to student."""
        if isinstance(grade, (int,float)):
            self.grades.append(grade)

    def calc_average(self):
        """Calculate the average of the grades."""
        if not self.grades:
            return 0
        total = sum(self.grades)
        avg = total / len(self.grades)
        return avg

    def check_honor(self):
        """Check if the student deserves a mention of honor."""
        if self.calc_average() > 90:
            self.honor = "Yes"
        else:
            self.honor = "No"

    def delete_grade(self, index):
        """Delete the grade of a student."""
        if 0 <= index < len(self.grades):
            del self.grades[index]

    def report(self):  # broken format
        """Print a report of the student."""
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Grades Count:", len(self.grades))
        print("Average Grade:", self.calc_average())
        print("Honor Status:", self.honor)

def startrun():
    """Calculate the average of the student."""
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades(60)
    a.calc_average()
    a.check_honor()
    a.delete_grade(0)
    a.report()

startrun()
