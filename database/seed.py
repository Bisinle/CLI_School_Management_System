#!/usr/bin/env python3



import sys
import os

# Add the project_directory to the Python path
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_directory)

# Now you can import from models

from faker import Faker

import random


from database.Session_and_Base import *
from models.models import  *

if __name__ == '__main__':
    engine = create_engine('sqlite:///SMS.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    fake = Faker()


'''---------------------populate the teachers table-----------------------'''
session.query(Teacher).delete()
teachers_list=[]
for i in range(20):
    teacher = Teacher(
    first_name = fake.unique.first_name(),
    last_name = fake.unique.last_name(),
    salary = random.randint(3000,9000),
    bank_acount =random.randint(7382,4859845793485)

    )
    teachers_list.append(teacher)
session.add_all(teachers_list)
session.commit()



'''------------populating the courses table'''
courses_names = [
    "Mathematics",
    "Science",
    "History",
    "English",
    "Geography",
    "Computer Science",
    "Art",
    "Music",
    "Physical Education",
    "Spanish",
    "French",
    "German",
    "Chinese",
    "Japanese",
    "Italian",
    "Latin",
    "Algebra",
    "Geometry",
    "Chemistry",
    "Biology",
    "Physics",
    "Earth Science",
    "Environmental Science",
    "Economics",
    "Government",
    "Psychology",
    "Sociology",
    "Anthropology",
    "Astronomy",
    "Philosophy",
    "Ethics",
    "Literature",
    "Creative Writing",
    "Drama",
    "Theater Arts",
    "Home Economics",
    "Cooking",
    "Woodshop",
    "Auto Mechanics",
    "Physical Science",
    "Health Education",
    "Nutrition",
    "Political Science",
    "Business",
    "Accounting",
    "Marketing",
    "Foreign Relations",
    "Religious Studies",
    "Mythology",
]

# You can access these subjects like school_subjects[0] for "Mathematics".

session.query(Course).delete()
courses_list= []
for c in courses_names :
    random_teach_id= random.randint(0,19)
    course = Course(
        course_name = c,
        room = random.randint(100,900),
        credit_hours =3,
        teachers_id = teachers_list[random_teach_id].id
    ) 
    courses_list.append(course)

session.add_all(courses_list)
session.commit()
# for i in session.query(Course):
#     session.delete(i)
# session.commit ()



'''------------------populate the student restaurant-------------------'''
session.query(Student).delete()
students_list=[]
gender_list=['M','F']
for i in range(20):
    student = Student(
        first_name = fake.unique.first_name(),
        last_name = fake.unique.last_name(),
        gender = random.choice(gender_list),

    )
    students_list.append(student)
session.add_all(students_list)
session.commit()


# '''-------------POPULATINGA------------------A D M I N S----------------table'''
# admin_list = []
# for i in range(0,5):
#     admin =Admin(
#         name = fake.name(),
#         email = fake.email(),
#         password = fake.password()
#     )
#     admin_list.append(admin)
# print(admin_list)
# session.add_all(admin_list)
# session.commit()


# # get a student instance
# stud1 = session.query(Student).all()[0]
# stud2 = session.query(Student).all()[4]
# stud3= session.query(Student).all()[7]
# stud4 = session.query(Student).all()[3]
# stud5 = session.query(Student).all()[4]
# stud6= session.query(Student).all()[12]
# stud7 = session.query(Student).all()[5]
# stud8 = session.query(Student).all()[6]
# stud9 = session.query(Student).all()[7]
# stud10 = session.query(Student).all()[8]
# stud11= session.query(Student).all()[9]
# #get a course instance
# course1 = session.query(Course).all()[0]
# course2 = session.query(Course).all()[3]
# course3 = session.query(Course).all()[2]
# course4 = session.query(Course).all()[4]
# course5 = session.query(Course).all()[5]
# course6 = session.query(Course).all()[6]
# course7 = session.query(Course).all()[7]
# course8 = session.query(Course).all()[8]
# course9 = session.query(Course).all()[9]
# course10 = session.query(Course).all()[10]
# # print(stud1)
# # print('-----------------------------------')
# # print(course1)

# session.query(Grade).delete()
# # create a grade instance and use it to test
# grade1 = Grade(student= stud1, course=course1,mark=89, grade='A')
# grade2 = Grade(student= stud2, course=course2,mark=30, grade='E')
# grade3 = Grade(student= stud3, course=course3,mark=66, grade='C')
# grade4 = Grade(student= stud4, course=course4,mark=20, grade='F')
# grade5 = Grade(student= stud5, course=course5,mark=75, grade='A')
# grade6 = Grade(student= stud6, course=course6,mark=90, grade='A')
# grade7 = Grade(student= stud7, course=course7,mark=54, grade='C')
# grade8 = Grade(student= stud8, course=course8,mark=47, grade='D')
# grade9 = Grade(student= stud9, course=course9,mark=92, grade='A')
# grade10 = Grade(student= stud10, course=course10,mark=12, grade='F')

# session.add_all([grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8,grade9,grade10])
# session.commit()
# # print(grade1)


# # now that the association is set
# # --- let's get the stud.grade
# print(stud1.grade)
# print('-----------------------------------')
# # thru the association, we can access the courses the student is taking
# print(stud1.courses)
# print('-----------------------------------')
# # thru the association, we can access the students that are taking this course
# print(course2.students[0])
