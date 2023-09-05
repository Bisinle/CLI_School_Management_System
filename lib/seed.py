#!/usr/bin/env python3

from faker import Faker

import random

from sqlalchemy import create_engine,Table
from sqlalchemy.orm import sessionmaker

from models import  *

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





'''------populating the student_courses Association table-------'''
session.query(student_course).delete()
# this is many to many so we are free to choose the range
for i in range(100):
    # in each range, choose a random course
    random_course= random.randint(0,len(courses_list)-1)
    random_student= random.randint(0,len(students_list)-1)
    # choos a random student
    students_list[random_student].courses.append(courses_list[random_course])

session.commit()



