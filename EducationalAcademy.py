from Building import Building


class EducationalAcademy(Building):
    def __init__(self, school_name):
        Building.__init__(self, school_name)
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def expel_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def get_students(self):
        return self.students

    def get_student_count(self):
        return len(self.students)

    def show_info(self):
        info = f"School Name: {self.name}, Number of Students: {len(self.students)}\n"
        info += "List of students:\n"
        for student in self.students:
            info += f"\t{student}\n"
        return info
