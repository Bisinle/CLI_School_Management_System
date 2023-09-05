#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Course, Teacher,Student
import click


engine = create_engine('sqlite:///SMS.db')
Session = sessionmaker(bind=engine)
session =Session()


'--------------------O B J E C T S -----------------------------------'
student1 = session.query(Student).first()
# print(len(student1.courses))
# print(student1.id)
# teacher1 = session.query(Teacher).first()
# print(len(teacher1.course))
# course1 = session.query(Course).first()
# print(len(course1.students))
'---------------------------------------------------------------------'


'''#  check if a student can be posted without the commands first    # '''
#     # student1 = Student(
#     #     first_name='Hana',
#     #     last_name='Baker',
#     #     gender='F'
#     # )
#     # session.add(student1)
#     # session.commit()
# # print(session.query(Course).all())


'--------------------C L I C K----G R O U P S---------------------------'
@click.group()
def mycommands():
    pass


'''------------------------ A D D student------------------------'''
@mycommands.command()
@click.argument("first_name" , type = str)
@click.argument("last_name" , type = str)
@click.argument("gender", type = str)
def add_student( first_name,last_name,gender):
    ''' add a new student, first_name last_name gender'''
    if first_name.isalpha() and last_name.isalpha() and gender.isalpha():
        student = Student(
            first_name=first_name.title(),
            last_name=last_name.title(),
            gender=gender
        )
    else:
        click.echo( '-------student credentials should be a string----------')
    student_exists = session.query(Student).filter_by(

        first_name = student.first_name,
        last_name = student.last_name,
        gender = student.gender,
    ).first()
    
    if student_exists is  None:
        session.add(student)
        session.commit()
        click.echo('student added successfully ')
    else:
        click.echo('student already exists in the database ')

            

    # click.echo(all_students)
        




# '''------------------------D E L E T E student------------------------'''

# @mycommands.command()
# @click.option("--sid",type=int, prompt = 'Enter student id')
# def delete_student(sid):
#     '''delete a student by passing their id'''
#     stud = session.query(Student).filter_by(id=sid).first()
#     session.delete(stud)
#     session.commit()
#     click.echo('student deleted successfully')

# '''------------------------U P D A T E  student------------------------'''
# @mycommands.command()
# # @click.option("--sid",type=int, prompt = 'Enter student id')
# @click.option("--target_full_name", prompt = 'Enter the name you want to  change')
# @click.option("--new_full_name", prompt = 'Enter the name you want to change it to ')
# # @click.option("--sid", prompt = 'Enter student last name to update')
# def update_student(target_full_name,new_full_name):
#     ''' update a student by entering full names seperated by space '''
#     target_full_name_splitted = target_full_name.split(' ')
#     new_full_name_splitted = new_full_name.split(' ')
#     print(f"{target_full_name_splitted} was updated to  {new_full_name_splitted}")
    
#     ## delet or update the student that matches the id
#     # stud = session.query(Student).filter_by(id=sid).update({
#     #     Student.gender : 'U'
#     # })
#     stud = session.query(Student).filter_by(first_name=target_full_name_splitted[0], last_name = target_full_name_splitted[1]).update({
#         Student.first_name : new_full_name_splitted[0],
#         Student.last_name : new_full_name_splitted[1] })

#     session.commit()  
#     click.echo('updated  successfully')

# '''------------------------D I S P L A Y students------------------------'''
# # @mycommands.command()
# # @click.option()



if __name__ == "__main__":
    # # delete_student()
    # update()
    mycommands()