class Person:
    def _init_(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id

class Student(Person):
    def _init_(self, name, age, student_id, grade):
        super()._init_(name, age, student_id)
        self.grade = grade
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

class Teacher(Person):
    def _init_(self, name, age, teacher_id, subject):
        super()._init_(name, age, teacher_id)
        self.subject = subject
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)

class Course:
    def _init_(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def calculate_average_grade(self):
        if not self.students:
            return 0
        total_grades = sum(student.grade for student in self.students)
        return total_grades / len(self.students)

class School:
    def _init_(self):
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
            course.add_student(student)
            student.enroll(course)
            print(f"Enrolled {student.name} in {course.course_name}.")
        else:
            print("Student or Course not found.")

    def assign_teacher_to_course(self, teacher_id, course_id):
        teacher = next((t for t in self.teachers if t.person_id == teacher_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if teacher and course:
            teacher.assign_course(course)
            print(f"Assigned {teacher.name} to {course.course_name}.")
        else:
            print("Teacher or Course not found.")

    def view_students_in_course(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            print(f"Students enrolled in {course.course_name}:")
            for student in course.students:
                print(f"- {student.name}")
        else:
            print("Course not found.")

    def view_courses_of_student(self, student_id):
        student = next((s for s in self.students if s.person_id == student_id), None)
        if student:
            print(f"Courses enrolled by {student.name}:")
            for course in student.courses:
                print(f"- {course.course_name}")
        else:
            print("Student not found.")

# Example Usage
if _name_ == "_main_":
    # Create a school
    school = School()

    # Add students
    student1 = Student("Alice", 18, "S001", 85)
    student2 = Student("Bob", 19, "S002", 90)
    school.add_student(student1)
    school.add_student(student2)

    # Add teachers
    teacher1 = Teacher("Mr. Smith", 40, "T001", "Math")
    teacher2 = Teacher("Ms. Johnson", 35, "T002", "Science")
    school.add_teacher(teacher1)
    school.add_teacher(teacher2)

    # Add courses
    course1 = Course("Mathematics", "C001")
    course2 = Course("Science", "C002")
    school.add_course(course1)
    school.add_course(course2)

    # Enroll students in courses
    school.enroll_student_in_course("S001", "C001")
    school.enroll_student_in_course("S002", "C002")

    # Assign teachers to courses
    school.assign_teacher_to_course("T001", "C001")
    school.assign_teacher_to_course("T002", "C002")

    # View students in a course
    school.view_students_in_course("C001")

    # View courses of a student
    school.view_courses_of_student("S002")

    # Calculate average grade in a course
    print(f"Average grade in {course1.course_name}: {course1.calculate_average_grade()}")