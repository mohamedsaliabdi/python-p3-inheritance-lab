#!/usr/bin/env python

from user import User

class Student(User):
    from user import User  # Assuming User class is in user.py

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, course):
        if course in self.knowledge:
            print("Course already in the list.")
        else:
            self.knowledge.append(course)
            return self.knowledge

# Test the class
paul = Student("Paul", "Cheru")
paul.learn("math")
print(paul.learn("math"))
print(paul.knowledge)
# paul.learn("science")
# paul.learn("math")  # This should say "Course already in the list"


        