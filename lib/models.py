# models.py
from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///SMS.db')
Session = sessionmaker(bind=engine)
session = Session()

student_course = Table('student_course',
                               Base.metadata,
                               Column('courses_id', ForeignKey('courses.id')),
                               Column('students_id', ForeignKey('students.id')),
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    courses = relationship('Course', secondary = student_course, back_populates='students')
    

    def __repr__(self):
        return f"('id':{self.id}, 'fname': {self.first_name}, 'lname': {self.last_name}, gender: {self.gender})"

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    salary = Column(Integer())
    bank_acount = Column(Integer())

    course = relationship('Course', backref='teacher')
    def __repr__(self):
        return f"('id':{self.id}, 'fname': {self.first_name}, 'lname': {self.last_name}, 'gender': {self.salary}, 'bank_acount': {self.bank_acount})"

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer(), primary_key=True)
    course_name = Column(String())
    room = Column(Integer())
    credit_hours = Column(Integer())
    teachers_id = Column(Integer(), ForeignKey('teachers.id'))
    students = relationship('Student', secondary = student_course, back_populates='courses')

  
    def __repr__(self):
        return f"('id':{self.id}, 'course_name': {self.course_name}, 'room': {self.room})"



if __name__ =="__main__":
    pass