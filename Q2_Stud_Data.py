# Sample student data with subjects Java, Python, and MEAN Stack
student_data = [
    {"student_name": "Avadhoot", "grades": {"Java": 85, "Python": 92, "MEAN Stack": 78}},
    {"student_name": "Omkar",    "grades": {"Java": 88, "Python": 79, "MEAN Stack": 95}},
    {"student_name": "Pradeep",  "grades": {"Java": 70, "Python": 85, "MEAN Stack": 80}},
    {"student_name": "Sagar",    "grades": {"Java": 90, "Python": 93, "MEAN Stack": 88}},
    {"student_name": "Chetan",   "grades": {"Java": 60, "Python": 75, "MEAN Stack": 70}},
]

# Function to calculate the average grade for each student
def calculate_average_grades(data):
    """Calculate the average grades for each student."""
    averages = {}  # Dictionary to hold average grades
    for student in data:
        grades = student["grades"]  # Get the grades dictionary for the student
        # Calculate average by summing grades and dividing by number of subjects
        avg_grade = sum(grades.values()) / len(grades)
        # Store the average grade in the averages dictionary
        averages[student["student_name"]] = avg_grade
    return averages  # Return the dictionary with average grades

# Function to find the top-performing student
def find_top_student(averages):
    """Identify the student with the highest average grade."""
    top_student = max(averages, key=averages.get)  # Find the student with max average
    return top_student, averages[top_student]  # Return the name and grade of top student

# Function to calculate grade distribution for each course
def calculate_grade_distribution(data):
    """Create a distribution of grades for each course."""
    distribution = {}  # Dictionary to hold lists of grades for each course
    for student in data:
        for course, grade in student["grades"].items():  # Iterate through each student's grades
            # Check if course already has an entry in distribution
            if course in distribution:
                distribution[course].append(grade)  # Append the grade to the existing list
            else:
                distribution[course] = [grade]  # Initialize a new list for the course
    return distribution  # Return the grade distribution

# Function to find highest and lowest grades in each course
def find_highest_lowest_grades(distribution):
    """Identify the highest and lowest grades for each course."""
    highest_lowest = {}  # Dictionary to hold highest and lowest grades
    for course, grades in distribution.items():
        highest_lowest[course] = {
            "highest": max(grades),  # Get the highest grade for the course
            "lowest": min(grades)     # Get the lowest grade for the course
        }
    return highest_lowest  # Return the dictionary with highest and lowest grades

# Running the analysis
average_grades = calculate_average_grades(student_data)  # Calculate average grades
top_student, top_grade = find_top_student(average_grades)  # Find the top student
grade_distribution = calculate_grade_distribution(student_data)  # Get grade distribution
highest_lowest_grades = find_highest_lowest_grades(grade_distribution)  # Find highest/lowest grades

# Printing the results
print("Average Grades per Student:")
for student, avg in average_grades.items():
    print(f"  {student}: {avg:.2f}")  # Print each student's average grade formatted to 2 decimal places

print(f"\nTop-Performing Student: {top_student} with an average grade of {top_grade:.2f}")  # Print top student info

print("\nGrade Distribution by Course:")
for course, grades in grade_distribution.items():
    print(f"  {course}: {grades}")  # Print the list of grades for each course

print("\nHighest and Lowest Grades per Course:")
for course, grades in highest_lowest_grades.items():
    print(f"  {course}: Highest = {grades['highest']}, Lowest = {grades['lowest']}")  # Print highest and lowest grades
