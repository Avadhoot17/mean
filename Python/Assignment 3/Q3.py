class Person:
    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id


class Student(Person):
    def __init__(self, name, age, person_id, grade):
        super().__init__(name, age, person_id)
        self.grade = grade
        self.enrolled_courses = []

    def enroll_course(self, course):
        self.enrolled_courses.append(course)
        course.enroll_student(self)

    def get_courses(self):
        return [course.course_name for course in self.enrolled_courses]


class Teacher(Person):
    def __init__(self, name, age, person_id, subject):
        super().__init__(name, age, person_id)
        self.subject = subject
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)
        course.assign_teacher(self)


class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []
        self.teacher = None

    def enroll_student(self, student):
        self.enrolled_students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def average_grade(self):
        if not self.enrolled_students:
            return 0
        total_grade = sum(student.grade for student in self.enrolled_students)
        return total_grade / len(self.enrolled_students)


class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student_in_course(self, student_id, course_id):
        student = next((s for s in self.students if s.person_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if student and course:
            student.enroll_course(course)

    def assign_teacher_to_course(self, teacher_id, course_id):
        teacher = next((t for t in self.teachers if t.person_id == teacher_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if teacher and course:
            teacher.assign_course(course)

    def view_students_in_course(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            return [student.name for student in course.enrolled_students]
        return []

    def view_courses_of_student(self, student_id):
        student = next((s for s in self.students if s.person_id == student_id), None)
        if student:
            return student.get_courses()
        return []

    def average_grade_of_course(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            return course.average_grade()
        return 0


# Example usage:
if __name__ == "__main__":
    school = School()

    # Creating students
    student1 = Student("Alice", 15, "S001", 90)
    student2 = Student("Bob", 16, "S002", 85)

    # Creating teachers
    teacher1 = Teacher("Mr. Smith", 40, "T001", "Math")

    # Creating courses
    course1 = Course("Algebra", "C001")
    course2 = Course("Geometry", "C002")

    # Adding students, teachers, and courses to the school
    school.add_student(student1)
    school.add_student(student2)
    school.add_teacher(teacher1)
    school.add_course(course1)
    school.add_course(course2)

    # Enrolling students in courses
    school.enroll_student_in_course("S001", "C001")
    school.enroll_student_in_course("S002", "C001")
    school.enroll_student_in_course("S001", "C002")

    # Assigning teacher to a course
    school.assign_teacher_to_course("T001", "C001")

    # Viewing students in a course
    print("Students in Algebra:", school.view_students_in_course("C001"))

    # Viewing courses of a student
    print("Courses for Alice:", school.view_courses_of_student("S001"))

    # Calculating average grade of a course
    print("Average grade in Algebra:", school.average_grade_of_course("C001"))
