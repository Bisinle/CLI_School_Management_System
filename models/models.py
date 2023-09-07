# models.py
from database.Session_and_Base import *


'''-----------------COURSE_STUDENT ASSOCIATION TABLE---------------------'''
student_course = Table('student_course',
                               Base.metadata,
                               Column('courses_id', ForeignKey('courses.id')),
                               Column('students_id', ForeignKey('students.id')),
)



'''-------------------------S T U D E N T S ------------T A B L E------------------------'''
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    courses = relationship('Course', secondary=student_course, back_populates='students')
    
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
    students = relationship('Student', secondary = student_course, back_populates='courses')

  
    def __repr__(self):
        return f"('id':{self.id}, 'course_name': {self.course_name}, 'room': {self.room}, 'credit_hours; {self.credit_hours}, 'teachers_is': {self.teachers_id})"



if __name__ =="__main__":
    pass