import sys
import os
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_directory)

# Now you can import from models
from models.models import *
from database.Session_and_Base import *
import click
import random



@click.group(name='teacher-commands')
def teacher_command():
    '''teachers database'''
# '''---------------A D D  TEACHER-------------------'''
@teacher_command.command()
@click.option("--first_name" ,'-fn',prompt='Enter FNAME', type = str)
@click.option("--last_name" ,'-ln',prompt='Enter LNAME', type = str)
@click.option("--salary",'-s',prompt='Enter salary', type = int)
@click.option("--bank_account",'-ba',prompt='Enter bank_account', type = int)
def add_teacher( first_name,last_name,salary,bank_account):
    ''' add a new teacher, first_name last_name salary and bank_acc'''
    if first_name.isalpha() and last_name.isalpha() and isinstance(salary,int) and isinstance(bank_account,int):
        teacher = Teacher(
            first_name=first_name.title(),
            last_name=last_name.title(),
            salary=salary,
            bank_acount= bank_account
        )
    else:
        click.echo( '-------please enter the credentials using the correct data types----------')

    teacher_exists = session.query(Teacher).filter_by(

        first_name = teacher.first_name,
        last_name = teacher.last_name,
        salary = teacher.salary,
        bank_acount = teacher.bank_acount,
    ).first()
    
    if teacher_exists is  None:
        session.add(teacher)
        session.commit()
        click.echo('teacher added successfully ')
    else:
        click.echo('teacher already exists in the database ')





# '''------------------ D E L E T E     teacher------------------'''
@teacher_command.command()
@click.option('--teacher_full_name', '-tf', prompt = "Enter the teacher's full name")
def delete_teacher(teacher_full_name):
    '''deletes a teacher and updates course table'''
    if len(teacher_full_name.split(' ')) == 2 and isinstance(teacher_full_name, str):
        fname,lname = teacher_full_name.split(' ')
        
        # let's check if the teacher exists in the records
        teacher= session.query(Teacher).filter( Teacher.first_name.like(f"%{fname}%"), Teacher.last_name.like(f"%{lname}%")).first()
        # let's find the course instance that is assigned to the teacher above
        if teacher is not None:
            print('--------------------')
            # find another teacher to assign the course to 
            assign_course_to_another_teacher_id =(random.choice([teach.id for teach in session.query(Teacher).all()]))
            # update the teachers_id column in the course with the new teacher id
            assigned_course = session.query(Course).filter_by(teachers_id = teacher.id).update({
                Course.teachers_id : assign_course_to_another_teacher_id
            })
            # print(,assign_course_to_another_teacher_id)#' this teacher id will replace the old one-->'
            #delete the old teacher
            session.delete(teacher) 
            session.commit()           
           
        else:
            click.echo(click.style('\n--------- !! E R R O R !! ---------------------',fg='red',bold=True))  
            click.echo(click.style('Not found',fg='red', bold=True))
    else:
        click.echo(click.style('\n--------- !! E R R O R !! ---------------------',fg='red',bold=True))  
        click.echo(click.style('Please enter full name spereted by space',fg='red', bold=True))



'''-----------------U P D A T E _____________T E A C H E R-------------'''


@teacher_command.command()
@click.option('--teacher_full_name', '-tf', prompt = "Enter the teacher's full name")
def update_teacher(teacher_full_name):
    '''-----update a  teacher's information'''
    # get the table column names using inspector
    # inspector = inspect(session.get_bind())
    # table_columns = ([column['name'] for column in inspector.get_columns(Teacher.__table__.name)])
    options={'all':'all', 'fn':'first_name', 'ln':'last_name', 'sal':'salary', 'acc':'bank_acount'}
    if len(teacher_full_name.split(' ')) ==2 and isinstance(teacher_full_name,str):
        fname,lname= teacher_full_name.split(' ')
        #check if the teacher EXISTS in the databse
        teacher= session.query(Teacher).filter( Teacher.first_name.like(f"%{fname.title()}%"), Teacher.last_name.like(f"%{lname.title()}%")).first()
        # let's find the course instance that is assigned to the teacher above
        if teacher is not None:
            user_option = click.prompt('which colum do you want to update', type=click.Choice(options))
            if user_option =='all':
                fname =click.prompt('Enter first name ')
                lname=click.prompt('Enter last name ')
                salary=click.prompt('Enter salary amount')
                bank_account=click.prompt('Enter bank_account number ')
                session.query(Teacher).filter_by(id = teacher.id).update({
                    Teacher.first_name : fname.title(),
                    Teacher.last_name : lname.title(),
                    Teacher.salary : salary,
                    Teacher.bank_acount : bank_account

                })
                session.commit()
                click.echo(click.style('successfully updated the teacher information',fg='white',bg='green'))
            elif user_option =='fn':
                fname =click.prompt('Enter first name ')
                session.query(Teacher).filter_by(id = teacher.id).update({
                    Teacher.first_name : fname.title()
                

                })
                session.commit()
                click.echo(click.style('successfully updated the teacher first_name',fg='white',bg='green'))
            
            elif user_option=='ln':
                lname =click.prompt('Enter last name ')
                session.query(Teacher).filter_by(id = teacher.id).update({
                    Teacher.last_name : lname.title()
                

                })
                session.commit()
                click.echo(click.style('successfully updated the teacher last_name',fg='white',bg='green'))

            elif user_option=='sal':
                salary =int(click.prompt('Enter salary '))
                session.query(Teacher).filter_by(id = teacher.id).update({
                    Teacher.salary : salary
                

                })
                session.commit()
                click.echo(click.style('successfully updated the teacher salary',fg='white',bg='green'))

            elif user_option=='acc':
                bank_account =int(click.prompt('Enter bank_account '))
                session.query(Teacher).filter_by(id = teacher.id).update({
                    Teacher.salary : bank_account
                

                })
                session.commit()
                click.echo(click.style('successfully updated the teacher salary',fg='white',bg='green'))

            

        else:
            click.echo(click.style('\n--------- !! E R R O R !! ---------------------',fg='red',bold=True))  
            click.echo(click.style('teacher does not Exist',fg='red'))
    else:
        click.echo(click.style('\n--------- !! E R R O R !! ---------------------',fg='red',bold=True))  
        click.echo(click.style('please enter string of  first and last names ',fg='red'))



        
        
'''-----------------D I S P L A Y  ________ A L L _________T E A C H E R-------------'''
@teacher_command.command()
def display_all_teachers():
    '''display all the teachers in our records'''
    for teacher in session.query(Teacher).all():
        click.echo(click.style(teacher,fg='blue',bold=True))




'''----------D I S P L A Y _______T E A C H E R_____COURSES-------------'''

@teacher_command.command()
@click.option("--teacher_full_name", prompt = 'Enter teacher full name')
def teacher_courses(teacher_full_name):
    '''display all the courses a particular student is taking'''
    fname,lname= (teacher_full_name.split(' '))        
    teacher = session.query(Teacher).filter(Teacher.first_name.like(f"%{fname.title()}%"), Teacher.last_name.like(f"%{lname.title()}%")).first()
    
    click.echo( f"--- studetn is taking {len(teacher.course)} courses, ")
    for course in teacher.course:
        print('---------------------------------------------------')
        click.echo(click.style(course,fg='white',bg='magenta'))





if __name__ == "__main__":
    teacher_command()
