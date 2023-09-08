import sys
import os
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_directory)

# Now you can import from models
from models.models import *
from database.Session_and_Base import *
import click
import random



@click.group(name='course')
def courcommand():
    '''courses related commands'''
    pass
# '''------------------ A D D COURSES---------------------'''
@courcommand.command()
@click.option("--course_name" ,'-cn',prompt='Enter the course_name', type = str)
@click.option("--room",'-r',prompt='Enter the venu', type = int)
@click.option("--credit_hours",'-ch',prompt='Enter credit_hours', type = int)
@click.option("--teacher_full_name",'-tn',prompt='Assign to a teacher', type = str)
def add_course(course_name, teacher_full_name,room,credit_hours):
    ''' add a new course'''
    
    if isinstance(course_name,str) and isinstance(teacher_full_name,str) and isinstance(room,int) and isinstance(credit_hours,int):
        # split the full name to get first and last names 
        fname,lname = teacher_full_name.split(' ')
        # filter using the splitted fullname---goal is to optian the teacher id to pass to the course table
        teacher = session.query(Teacher).filter_by(first_name=fname.title(), last_name = lname.title()).first()
        if teacher is not None:
            course = Course(
                    course_name=course_name.title(),
                    room=room,
                    credit_hours= credit_hours,
                    teachers_id=teacher.id,
            )
            

            course_exists = session.query(Course).filter_by(

                course_name = course.course_name.title(),
                teachers_id = course.teachers_id,
                room = course.room,
                credit_hours = course.credit_hours
            ).first()

            if course_exists is  None:
                session.add(course)
                session.commit()
                click.echo(click.style('course  added successfully ',fg='green',bg='green', bold=True))
            else:
                click.echo(click.style('\n--------- !! E R R O R !! ---------------------',fg='red',bold=True))  
                click.echo(click.style('course  already exists in the database ',fg='red',bold=True))




        else:
            click.echo(click.style('\n--------- !! E R R O R !! ---------------------',fg='red',bold=True))  
            click.echo(click.style("Teacher does not exist",fg='red',bold=True))
    else:
        click.echo( '-------please enter the credentials using the correct data types----------')
  
    
  


'''------------- D E L E T E_________COURSES -------------------'''
@courcommand.command()
@click.option("--course_name" ,'-cn',prompt='Enter the course_name', type = str)
def delete_course(course_name):
    '''---------delete a course from the database'''
    #check if the course name exists in out database
    course_existing = session.query(Course).filter_by(course_name=course_name.title()).first()
    if course_existing is not None:
        session.delete(course_existing)
        session.commit()

        click.echo(click.style("course deleted successfully ",fg='white',bg='green',bold=True))



    else:
        click.echo(click.style('\n--------- !! E R R O R !! ---------------------',fg='white',bold=True))  
        click.echo(click.style("corse does not exist",fg='red',bold=True))










'''------------------- C O U R S E_______R E G I S T E R ----------- '''

@courcommand.command()
@click.option('--student_full_name' , '-sn', prompt = 'Enter student_full_name you want to register')
# @click.option('--course_name' , '-cn', prompt = 'Enter the course name for the student', type=click.Choice(course_options))
def course_registrations(student_full_name):
        '''register a student for a course'''
        # get the course names from the table 
        cours_names= session.query(Course.course_name).all()
        # print(cours_names)
        #declare an empty dictto populate with numbers as keys and  the course_names values
        course_options = {}
        for num , course in zip(range(1,len(cours_names)+1), cours_names):
            course_options.update({num:course})



        if isinstance(student_full_name,str) :
            #split the name to first and last
            splitted_stud_name = (student_full_name.split(' '))         
            # filter using the splitted fullname---goal is to optian the user id to pass to the course table
            stud_instance = session.query(Student).filter_by(first_name=splitted_stud_name[0].title(), last_name = splitted_stud_name[1].title()).first()
            if stud_instance is not None:
                # # display the courses for the student to choose
                for  key,course, in course_options.items():
                    click.echo(f" {key}--{course[0]}")
                
                # enter the number corresponding to the course you want
                key = int((click.prompt('choose a course number')))
                # if the course key exist, then get the course isntance from the table
                if (key) in course_options.keys() :
                        chosen_course = (course_options[key])
                        cours_instance = session.query(Course).filter_by(course_name = chosen_course[0]).first()
                        # click.echo(cours_instance)
                        
                        #-------------------------------------------------------------
                        # brefore we add to the table, check if the record EXIST                       
                        does_record_exist= session.query(student_course).filter_by(students_id = stud_instance.id, courses_id = cours_instance.id).first()
                        #if does not exist, add to the table
                        if does_record_exist  is None:
                            stud_instance.courses.append(cours_instance)
                            session.commit()
                            click.echo(click.style('\n-----registrations successfull------',fg='green'))
                        
                        else:# elsethe record already exist in the table
                            click.echo(click.style('\n--------- !! E R R O R !! ---------------------',fg='red',bold=True))
                            click.echo(click.style('\n---studen  already  registered for this course----',fg='red'))
                else:# else if the course cannot be found in the courses table
                    click.echo(click.style('\n--------- !! E R R O R !! ---------------------',fg='red',bold=True))
                    click.echo(click.style('\n----course does not exist---',fg='red'))
      
            else:#if the studetn instance cannot be found in the table
                click.echo(click.style('\n--------- !! E R R O R !! ---------------------',fg='red',bold=True))  
                click.echo(click.style('student does not Exist',fg='red'))


@courcommand.command()
def display_all_courses():
    '''display all the courses in our database'''
    for course in session.query(Course).all():
        click.echo(click.style(course, fg='cyan', bg='black'))
    
        


if __name__ =='__main__':
    courcommand()