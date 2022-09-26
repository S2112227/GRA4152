#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:47:08 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE P10.8

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 5")

###############
## This module defines a superclass that models a Person. A Person has a name and a year of birth
#
class Person: # Superclass
    #####
    ## Constructs a person with a name and a year of birth.
    ## @name is the name of the person
    ## @year is the year of birth of the person
    #
    def __init__(self, name, year) :
        if isinstance(name, str)==True and isinstance(year, int)==True:
            self._name = name
            self._year = year
        else:
            print("The name must be a text (string) and the year of birth must be a number (integer)! Please correct and try again.")
    
    #####
    ## Definition of the __repr__ of the Person object.
    #
    def __repr__(self) :
        return f"Name: {self._name}\nYear of Birth: {self._year}"

###############
## This module defines a subclass that models a Student which is a Person. A Student has a major
#
class Student(Person): # Subclass
    #####
    ## Constructs a student with a name and a year of birth (person attributes) plus a major.
    ## @name is the name of the person from the superclass
    ## @year is the year of birth of the person from the superclass
    ## @major is the major of the student
    #
    def __init__(self, name, year, major) :
        super().__init__(name, year)
        # Validate that the major is a text of type string
        if isinstance(major, str)==True :
            self._major = major
        else:
            print("The major must be a text (string)! Please correct and try again.")
    
    #####
    ## Definition of the __repr__ of the Student object. This method overrides the same method from the Person superclass
    #
    def __repr__(self) :
        return f"Name: {self._name}\nYear of Birth: {self._year}\nMajor: {self._major}"

###############
## This module defines a subclass that models a Instructor which is a Person. An Instructor has a salary
#
class Instructor(Person): # Subclass
    #####
    ## Constructs an instructor with a name and a year of birth (person attributes) plus a salary.
    ## @name is the name of the person from the superclass
    ## @year is the year of birth of the person from the superclass
    ## @salary is the salary of the instructor
    #
    def __init__(self, name, year, salary) :
        super().__init__(name, year)
        # Validate that the salary is a numeric value of type float
        if isinstance(salary, int)==True :
            self._salary = salary
        else:
            print("The salary must be a number (float)! Please correct and try again.")
    
    #####
    ## Definition of the __repr__ of the Instructor object. This method overrides the same method from the Person superclass
    #
    def __repr__(self) :
        return f"Name: {self._name}\nYear of Birth: {self._year}\nSalary: {self._salary} NOK"

###############    
## Class and Methods test program     
def main():
    # First, a studentTest is created as an instance of the Student subclass
    studentTest1 = Student("Adrian Luthi",2000,"Master of Science in Financial Mathematics")  
    # We validate that the representation method (__repr__) works properly by printing the Student attributes
    print(f"RESULT \n{studentTest1}\n")
    print("EXPECTED\nName: Adrian Luthi\nYear of Birth: 2000\nMajor: Master of Science in Financial Mathematics\n")

    # Second, an instructorTest is created as an instance of the Instructor subclass
    instructorTest1 = Instructor("Tong Zhang",1980,1000000)  

    # We validate that the representation method (__repr__) works properly by printing the Instructor attributes
    print(f"RESULT \n{instructorTest1}\n")
    print("EXPECTED\nName: Tong Zhang\nYear of Birth: 1980\nSalary: 1000000 NOK\n")
    
    # Finally, we validate that the exceptions to the parameter types work
    studentTest2 = Student(4,2000,"Master of Science in Financial Mathematics") 
    print("\nEXPECTED\nThe name must be a text (string) and the year of birth must be a number (integer)! Please correct and try again.\n")
    studentTest3 = Student("Adrian Luthi",2000,0) 
    print("\nEXPECTED\nThe major must be a text (string)! Please correct and try again.\n")
    instructorTest2 = Instructor("Tong Zhang",1980,"1000000") 
    print("\nEXPECTED\nThe salary must be a number (float)! Please correct and try again.\n")

## Run the Class and Methods test program
main()


