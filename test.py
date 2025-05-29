"""Initialize the class"""
class Student:
    """Class that represents a student and their academic performance."""

    def __init__(self, student_id, name):
        """Initialize student with ID and name."""
        if not student_id or not name:
            raise ValueError("Student ID and name cannot be empty.")
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "No"
        self.honor = "No"
        self.letter_grade = "N/A"

    def add_grade(self, grade):
        """Add a valid grade to the student."""
        if not isinstance(grade, (int, float)):
            print("❌ Grade must be a number.")
            return
        if grade < 0 or grade > 100:
            print("❌ Grade must be between 0 and 100.")
            return
        self.grades.append(grade)

    def calc_average(self):
        """Calculate the average of the grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self):
        """Determine the letter grade based on average."""
        avg = self.calc_average()
        if avg >= 90:
            self.letter_grade = "A"
        elif avg >= 80:
            self.letter_grade = "B"
        elif avg >= 70:
            self.letter_grade = "C"
        elif avg >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

    def determine_pass_fail(self):
        """Check if the student passed based on average."""
        avg = self.calc_average()
        self.is_passed = "Yes" if avg >= 60 else "No"

    def check_honor(self):
        """Check if the student deserves a mention of honor."""
        self.honor = "Yes" if self.calc_average() >= 90 else "No"

    def remove_grade_by_index(self, index):
        """Remove a grade by its index."""
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"❌ Invalid index: {index}.")

    def remove_grade_by_value(self, value):
        """Remove the first occurrence of a specific grade."""
        if value in self.grades:
            self.grades.remove(value)
        else:
            print(f"❌ Grade value {value} not found.")

    def generate_summary(self):
        """Update all computed properties before reporting."""
        self.determine_letter_grade()
        self.determine_pass_fail()
        self.check_honor()

    def report(self):
        """Print a detailed student summary report."""
        self.generate_summary()
        print("\n📋 STUDENT REPORT")
        print("--------------------------")
        print("ID:            ", self.student_id)
        print("Name:          ", self.name)
        print("Grades:        ", self.grades)
        print("Grades Count:  ", len(self.grades))
        print("Average Grade: ", f"{self.calc_average():.2f}")
        print("Letter Grade:  ", self.letter_grade)
        print("Passed:        ", self.is_passed)
        print("Honor Roll:    ", self.honor)
        print("--------------------------\n")

def startrun():
    """Run the program to evaluate."""
    try:
        student = Student("001", "Alice")
        student.add_grade(95)
        student.add_grade(88)
        student.add_grade(72)
        student.add_grade(60)
        student.add_grade(105)  # ❌ Invalid
        student.add_grade("bad")  # ❌ Invalid
        student.remove_grade_by_index(10)  # ❌ Invalid index
        student.remove_grade_by_value(100)  # ❌ Not found
        student.remove_grade_by_value(72)  # ✅ Valid
        student.report()
    except ValueError as e:
        print(f"❌ Error: {e}")

startrun()
