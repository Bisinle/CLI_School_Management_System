import sys
import os
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_directory)

# Now you can import from models
from models.models import *
from database.Session_and_Base import *



# session.query(Admin).delete()
# bisinle = Admin(
#     name = 'Bisinle Daud',
#     email='abdi.com',
#     password ='12345'
# )
# session.add(bisinle)
# session.commit()
def user_login():
    login_email = str(input('Enter your email: '))
    login_passowrd = input('Enter your password: ')

    user = session.query(Admin).filter_by(email=login_email.title(), password = login_passowrd.title()).first()
    if user is not None:
        return user
    else:
        return None



if __name__ == '__main__':
    user_login()