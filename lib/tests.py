#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Student,Teacher,Course,student_course


if __name__ == '__main__':
    engine = create_engine('sqlite:///SMS.db')
    Session = sessionmaker(bind=engine)
    session = Session()


'''-------------TEACHER METHODS---------------'''
teacher1 = session.query(student_course).tilter()
print(teacher1)




















# # set the all the lists for the classes 
#     allcustomers = session.query(Customer)
#     allrestaurants = session.query(Restaurant)
#     allreviews = session.query(Review)
#     # (Customer.customer_list_setter(allcustomers))
#     # (Restaurant.restaurant_list_setter(allrestaurants))
#     # (Review.reviews_list_setter(allreviews))
  

#     '''--------------------------- M E T H O D S --------------------------'''


#     # ----------------------Review class methods---------------------------
#     review1 = allreviews[0] # get a review object from the database
#     # print(review1.customer_review) # get the customer that gave the review
#     # print(review1.restaurant_review) # get the restaurant the review belongs to 
#     # print(review1.full_review())


#     # ----------------------Restaurant class methods---------------------------
#     resttaurant1= allrestaurants[0] # we delete all the revies for this one [0]
#     resttaurant2= allrestaurants[1]
#     # print(resttaurant2.restaurant_review)
#     # print(resttaurant2.customer_reviewed)
#     # print(Restaurant.fanciest_restaurant())
#     # print(resttaurant2.all_reviews())

    

#     # ----------------------Customer class methods---------------------------
#     customer1 = allcustomers[1]
#     # print(customer1.reveiws_given_by_customer)
#     # print('--------------------')
#     # print(customer1.restaurants_reviewed)
#     # print(customer1.full_name)
#     # print(customer1.favorite_restaurant)
#     # print(customer1.add_review(resttaurant2,1))
#     # print(customer1.delete_restaurant_review(resttaurant2))




    
