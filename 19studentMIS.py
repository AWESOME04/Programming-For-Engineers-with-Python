# A class is a blue-print for creating objects.
# In this code implementation of OOP in Python, 
# we shall implement an object-oriented database for the UG Student MIS


# SECTION ONE
# 1. Define a class for Person
# 2. Create a person object from the Person class
# 3. Use the constructor method to define attribute for the Person class
# 4. Write a full_name method that returns the full name of the object


# SECTION TWO
# 1. Define a class Student which inherites from the Person class
# 2. Define extra attributes for student, such as hall of residence and courses
# 3. Create a student object from the Student  class

"""
4. Write a add_course, drop_course, print_all_courses method to mimic 
a real-world use-case of activities of adding a course, 
deleting a course and printing registered courses respectively
a student will perform on the Student MIS 

"""

# SECTION ONE
# Define a class for Person
class Person:
    # Constructor method to define attributes for the Person class
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = f"{first_name[0]}.{last_name}@st.ug.edu.gh"

    # Method to return the full name of the object
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Method to return the initials of the object
    def name_initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}"


# Create person objects from the Person class
person1 = Person("John", "Doe", 20)
person2 = Person("Jane", "Doe", 19)
print(person1.email)


# Test the full_name and name_initials methods
print(person1.full_name())  # Output: John Doe
print(person2.name_initials())



# SECTION TWO
# Define a class for Person
class Person:
    # Constructor method to define attributes for the Person class
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Method to return the full name of the object
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# Define a class for Student which inherits from the Person class
class student(Person):
    # Constructor method to define attributes for the Student class
    def __init__(self, first_name, last_name, hall_of_residence, courses):
        super().__init__(first_name, last_name)
        self.hall_of_residence = hall_of_residence
        self.courses = courses



# ALT
class Student(Person):
    def __init__(self, first_name, last_name, age, hall, courses=None):
        super().__init__(first_name, last_name, age)
        self.hall = hall
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course_title):
        if course_title not in self.courses:
            self.courses.append(course_title)

    def drop_course(self, course_title):
        if course_title in self.courses:
            self.courses.remove(course_title)

    def print_all_courses(self):
        print(f"{self.full_name()} has registered {len(self.courses)} courses:")
        print("-"*35)
        for course in self.courses:
            print(course)

student1 = Student("Kwame", "Nkrumah", 20, "Legon")

# Adding courses
student1.add_course("Python")
student1.add_course("Calculus")
student1.add_course("African Studies")
student1.add_course("Project Work")
print(student1.courses)

# Deleting courses
# student1.drop_course("Python")

# Printing out all the courses
student1.print_all_courses()



# Create a student object from the Student class
# st = student("Jane", "Doe", "Smith Hall", ["Mathematics", "Physics", "Chemistry"])

# Test the inherited full_name method
# print(student.full_name())  # Output: Jane Doe

# Test the extra attributes for Student
# print(student.hall_of_residence)  # Output: Smith Hall
# print(student.courses)  # Output: ["Mathematics", "Physics", "Chemistry"]


# SECTION THREE
# Adding and dropping courses

# OTHER
class Student(Person):
    # Constructor method to define attributes for the Student class
    def __init__(self, first_name, last_name, hall_of_residence, courses=None):
        super().__init__(first_name, last_name)
        self.hall_of_residence = hall_of_residence
        self.courses = [] if courses is None else courses

    # Method to add a course to the list of courses
    def add_course(self, course):
        self.courses.append(course)

    # Method to drop a course from the list of courses
    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found in courses.")

    # Method to print all registered courses
    def print_all_courses(self):
        print(f"Courses registered by {self.full_name()}:")
        for course in self.courses:
            print(f"- {course}")


# Magic Methods
# Overwrite string method