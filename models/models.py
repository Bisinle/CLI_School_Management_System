# models.py
from database.Session_and_Base import *




# '''-----------------COURSE_STUDENT ASSOCIATION TABLE---------------------'''
# student_course = Table('student_course',
#                                Base.metadata,
#                                Column('courses_id', ForeignKey('courses.id')),
#                                Column('students_id', ForeignKey('students.id')),
# )


'''--------------- G R A D E S -------------T A B L E-------------------'''
class Grade(Base):
    __tablename__ = 'grades'
    
    id = Column(Integer(), primary_key=True)
    student_id = Column('student_id', Integer(), ForeignKey('students.id'))
    course_id = Column('course_id', Integer(), ForeignKey('courses.id'))
    mark=Column(Integer())
    grade=Column(String(1))


    # realtionships with the other models
    student = relationship('Student',back_populates='grade')
    course = relationship('Course',back_populates='grade')
    extend_existing=True


    def __repr__(self):
        return f"('id':{self.id}, 'stud_name': {self.student.first_name}, 'course_name': {self.course.course_name}, 'marks; {self.mark}, 'grade': {self.grade})"




'''-------------------------S T U D E N T S ------------T A B L E------------------------'''
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    grade = relationship('Grade',  back_populates='student',cascade='all, delete-orphan')
    courses = association_proxy('grade', 'course')
    
#---------------------------------------------------------------------------------


    def __repr__(self):
        return f"('id':{self.id}, 'fname': {self.first_name}, 'lname': {self.last_name}, gender: {self.gender})"




'''-------------------------T E A C H E R S ------------T A B L E------------------------'''

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    salary = Column(Integer())
    bank_acount = Column(Integer())

    course = relationship('Course', backref='teacher')
    def __repr__(self):
        return f"('id':{self.id}, 'fname': {self.first_name}, 'lname': {self.last_name}, 'salary': {self.salary}, 'bank_acount': {self.bank_acount})"


'''------------------------C O U R S E S ------------T A B L E------------------------'''

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer(), primary_key=True)
    course_name = Column(String())
    room = Column(Integer())
    credit_hours = Column(Integer())
    teachers_id = Column(Integer(), ForeignKey('teachers.id'))
    grade = relationship('Grade',  back_populates='course')
    students = association_proxy('grade', 'student')

   

  
    def __repr__(self):
        return f"('id':{self.id}, 'course_name': {self.course_name}, 'room': {self.room}, 'credit_hours; {self.credit_hours}, 'teachers_is': {self.teachers_id})"



if __name__ =="__main__":
    '''----------testing model relationships-----------'''
    # fetch a student instance
  