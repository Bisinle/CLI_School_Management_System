#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Course, Teacher,Student,student_course
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
        




'''------------------------D E L E T E student------------------------'''

# @mycommands.command()
# @click.option("--sid",type=int, prompt = 'Enter student id')
# def delete_student(sid):
#     '''delete a student by passing their name'''
#     stud = session.query(Student).filter_by(id=sid).first()
#     session.delete(stud)
#     session.commit()
#     click.echo('student deleted successfully')

'''------------------------U P D A T E  student------------------------'''
# @mycommands.command()
# @click.option("--sid",type=int, prompt = 'Enter student id')
# @click.option("--target_full_name", prompt = 'Enter the name you want to  change')
# @click.option("--new_full_name", prompt = 'Enter the name you want to change it to ')
# @click.option("--sid", prompt = 'Enter student last name to update')
# def update_student(target_full_name,new_full_name):
#     ''' update a student by entering full names seperated by space '''
#     target_full_name_splitted = target_full_name.split(' ')
#     new_full_name_splitted = new_full_name.split(' ')
#     print(f"{target_full_name_splitted} was updated to  {new_full_name_splitted}")
    
#     # delet or update the student that matches the id
#     stud = session.query(Student).filter_by(id=sid).update({
#         Student.gender : 'U'
#     })
#     stud = session.query(Student).filter_by(first_name=target_full_name_splitted[0], last_name = target_full_name_splitted[1]).update({
#         Student.first_name : new_full_name_splitted[0],
#         Student.last_name : new_full_name_splitted[1] })

#     session.commit()  
#     click.echo('updated  successfully')

'''------------------------D I S P L A Y students------------------------'''
# @mycommands.command()
# @click.option()


'''---------------A D D  TEACHER-------------------'''
@mycommands.command()
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




'''------------------ A D D COURSES---------------------'''
@mycommands.command()
@click.option("--course_name" ,'-cn',prompt='Enter the course_name', type = str)
@click.option("--room",'-r',prompt='Enter the venu', type = int)
@click.option("--credit_hours",'-ch',prompt='Enter credit_hours', type = int)
@click.option("--teacher_full_name",'-tn',prompt='Assign to a teacher', type = str)
def add_course(course_name, teacher_full_name,room,credit_hours):
    ''' add a new course'''
    
    if isinstance(course_name,str) and isinstance(teacher_full_name,str) and isinstance(room,int) and isinstance(credit_hours,int):
        # split the full name to get first and last names 
        teacher_full_name_splitted = teacher_full_name.split(' ')
        # filter using the splitted fullname---goal is to optian the user id to pass to the course table
        teacher = session.query(Teacher).filter_by(first_name=teacher_full_name_splitted[0], last_name = teacher_full_name_splitted[1]).first()
        if teacher is not None:
            course = Course(
                    course_name=course_name.title(),
                    room=room,
                    credit_hours= credit_hours,
                    teachers_id=teacher.id,
            )
            # print(course)
        else:
            click.echo("Teacher does not exist")
    else:
        click.echo( '-------please enter the credentials using the correct data types----------')
    course_exists = session.query(Course).filter_by(

        course_name = course.course_name,
        teachers_id = course.teachers_id,
        room = course.room,
        credit_hours = course.credit_hours
    ).first()
    
    if course_exists is  None:
        session.add(course)
        session.commit()
        click.echo('course  added successfully ')
    else:
        click.echo('course  already exists in the database ')



'''-------------------register a ----S T U D E N T---- for a ----C O U R S E----- '''
# get the course names from the table 
cours_names= session.query(Course.course_name).all()
# print(cours_names)
#declare an empty dictto populate with numbers as keys and  the course_names values
course_options = {}
#create the dictionary
for num , course in zip(range(1,len(cours_names)), cours_names):
    course_options.update({num:course})


@mycommands.command()
@click.option('--student_full_name' , '-sn', prompt = 'Enter student_full_name you want to register')
# @click.option('--course_name' , '-cn', prompt = 'Enter the course name for the student', type=click.Choice(course_options))
def course_registrations(student_full_name):
        '''register a student for a course'''
        if isinstance(student_full_name,str) :
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
                        print(stud_instance)
                        print(cours_instance)
                        does_record_exist= session.query(student_course).filter_by(students_id = stud_instance.id, courses_id = cours_instance.id).first()
                        print(does_record_exist)
                        if does_record_exist  is None:
                            stud_instance.courses.append(cours_instance)
                            session.commit()
                            click.echo('\n-----registrations successfull------')
                           
                        else:
                            click.echo('\n--------- !! E R R O R !! ---------------------')
                            click.echo('\n---studen  already  registered for this course----')
                else:
                    click.echo('\n--------- !! E R R O R !! ---------------------')
                    click.echo('\n----course does not exist---')
      
            else:
                click.echo('\n--------- !! E R R O R !! ---------------------')  
                click.echo('student does not Exist')



    
        


            
    # if isinstance(student_name,str) and isinstance(course_name,str):
    #     student_name_aplitted = student_name.split(' ')
    #     # filter using the splitted fullname---goal is to optian the user id to pass to the course table
    #     stud_instance = session.query(Student).filter_by(first_name=student_name_aplitted[0].title(), last_name = student_name_aplitted[1].title()).first()
    #     course_instance = session.query(Course).filter(Course.course_name.like(f'%{course_name.title()}%')).first()
    #     print(stud_instance)
    #     print(course_instance)


            

if __name__ == "__main__":
    # # delete_student()
    # update()
    mycommands()