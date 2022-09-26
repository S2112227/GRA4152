#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:25:26 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE P10.1

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 5")

###############
## This module defines a class that models exam questions. A question has a text and an answer. 
#
class Question:
    #####    
    ## Constructs a question with empty question and answer strings. 
    #
    def __init__(self) : 
        self._text = "" 
        self._answer = ""

    ##### 
    ## Sets the question text.
    # @param questionText is the text of this question 
    #
    def setText(self, questionText) :
        self._text = questionText

    ##### 
    ## Sets the answer for this question.
    # @param correctResponse is the answer
    #
    def setAnswer(self, correctResponse) :
        self._answer = correctResponse

    ##### 
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise 
    #
    def checkAnswer(self, response) :
        return response == self._answer

    ##### 
    ## Displays this question. 
    #
    def display(self) :
        print(self._text)

## This module defines the NumericQuestion class and adds this class to the Question hierarchy of Section 10.1.
## This subclass overrides two of the methods from the Question superclass: setAnswer and checkAnswer
#
class NumericQuestion(Question):
    def __init__(self, tolerance = 0.01): 
        # Call the superclass constructor to define its instance variable.
        super().__init__()
        # A new instance variable is defined for the subclass. 
        # The tolerance variable allows to validate whether the reponse from the user is close enough to the correct response.
        self._tolerance = tolerance
    
    ##### 
    ## This method overrides the Question class method with the same name to allow for numeric responses.
    # @param correctResponse is the answer and must be a number of type int or float
    #
    def setAnswer(self, correctResponse) :
        # Validate that the correctResponse is a numeric value of type int or float
        if isinstance(correctResponse, float) == True:        
            self._answer = correctResponse
        else:
            print("The correct response must be a numeric value! Please correct and try again.")
    
    ##### 
    ## This method overrides the Question class method with the same name to receive and validate numeric responses.
    # @param response is the numeric response to check against the correct response
    # @return True if the response was correct, False otherwise 
    #
    def checkAnswer(self, response):
        # Validate that the response is a numeric value of type int or float
        if isinstance(response, float) == True:
            # Validate that the response is within the tolerance limit
            if abs(self._answer - response) <= self._tolerance:
                return True
            else:
                return False
        else:
            print("The response must be a numeric value! Please correct and try again.")
    
###############    
## Class and Methods test      
# First, a questionTest is created as an instance of the NumericQuestion class
questionTest = NumericQuestion()   

# We set the text of the question and validate that the setText and display methods work properly
questionTest.setText("What is the result of the following operation?: 5/6")
questionTest.display()
print("The expected result is: What is the result of the following operation?: 5/6")

# We set the answer of the question and validate that the setAnswer and checkAnswer methods work properly
questionTest.setAnswer(0.83) # The parameter of the setAnswer method is the correct response for the operation 5/6
questionTest.checkAnswer(0.85) # We set a response that is beyond the tolerance level of 0.01
print("The expected result is: False")
questionTest.checkAnswer(0.835) # We set a response that is  within the tolerance level of 0.01
print("The expected result is: True")

# Finally, we validate that the exceptions to the parameter types work
questionTest.setAnswer("test") # We set a response that is not numeric
print("The expected result is: The correct response must be a numeric value! Please correct and try again.")
questionTest.checkAnswer("test") # We set a response that is not numeric
print("The expected result is: The correct response must be a numeric value! Please correct and try again.")







