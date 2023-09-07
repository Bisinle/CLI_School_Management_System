

import sys
import os

# Add the project_directory to the Python path
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_directory)
from sqlalchemy.inspection import inspect

# Now you can import from models
from models.models import *




from database.Session_and_Base import *
import click
import random

@click.group(name='student-commands')
def student_section():
    '''student related commans'''
    pass

''' ------------------S T U D E N T_________S E C T I O N-----------------'''
# '''------------------------ A D D student------------------------'''
@student_section.command()
@click.option("--first_name" ,'-fn',prompt='Enter FNAME', type = str)
@click.option("--last_name" ,'-ln',prompt='Enter LNAME', type = str)
@click.option("--gender",'-g',prompt='Enter GENDER', type = str)
def add_student( first_name,last_name,gender):
    ''' add a new student'''
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

@student_section.command()
@click.option("--student_full_name",'-sfn', prompt = 'Enter student full name')
def delete_student(student_full_name):
    '''delete a student by passing their name'''
    #destructure and split the name to first and last
    fname,lname= (student_full_name.split(' '))        
    stud_instance = session.query(Student).filter(Student.first_name.like(f"%{fname.title()}%"), Student.last_name.like(f"%{lname.title()}%")).first()
    
    # delete the student fron student table
    if stud_instance is not None:
        session.delete(stud_instance)
        # session.commit()
        #check if the student with this id exists in the grade table and delete it
        stud_record= session.query(Grade).filter_by(student_id = stud_instance.id)
        
        stud_record.delete()
        session.commit()
       
        click.echo(click.style('\nstudent deleted successfully',fg='white',bg='green'))
    else:
        click.echo(click.style('\n----------!! E R R O R R !!----------------',fg='red')) 
        click.echo(click.style('student does not exist',fg='red')) 

    # # we need to delete the the sutdent record from the association table aswell
    # # i could not figure cascasde out


    # inspector= inspect(engine)
    # print( [col['name'] for col in inspector.get_columns(Grade.__table__.name)])
    


# '''------------------------U P D A T E  student------------------------'''

@student_section.command()
@click.option("--target_full_name", prompt = 'Enter the name you want to  change')
@click.option("--new_full_name", prompt = 'Enter the name you want to change it to ')
# @click.option("--sid", prompt = 'Enter student last name to update')

def update_student(target_full_name,new_full_name):
    ''' update a student by entering full names seperated by space '''
    # check if the name contain first and last name
    if all(len(name.split(' '))==2 for name in (target_full_name, new_full_name)):
        target_fname, target_lname = target_full_name.split(' ')      
        new_fname, new_lname = new_full_name.split(' ')
    
    
        stud = session.query(Student).filter(Student.first_name.like(f"%{target_fname}%"), Student.last_name.like(f"%{target_lname}%")).update({
        Student.first_name : new_fname,
        Student.last_name : new_lname })        
         
        print(f"{target_full_name} was updated to  {new_full_name}")
    else:
        click.echo('\n-----!! E R R O R R !!----------')
        click.echo('Enter full names please')

    session.commit()  
    



# '''------------------------D I S P L A Y students------------------------'''
@student_section.command()
def display_all_students():
    '''display all the students in our records'''
    for student in session.query(Student).all():
        click.echo(click.style(student,fg='cyan',bold=True))

# ---------------------- S T U D E N T courses---------------------
@student_section.command()
@click.option("--student_full_name", prompt = 'Enter student full name')
def student_courses(student_full_name):
    '''display all the courses a particular student is taking'''
    fname,lname= (student_full_name.split(' '))        
    student = session.query(Student).filter(Student.first_name.like(f"%{fname.title()}%"), Student.last_name.like(f"%{lname.title()}%")).first()
    
    click.echo( f"--- studetn is taking {len(student.courses)} courses, ")
    for course in student.courses:
        print('---------------')
        click.echo(course.course_name)




def greeting():
    # print('greeting is printed')
    student_section()
if __name__ == '__main__':
    greeting()
