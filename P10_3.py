#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:18:24 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE P10.3

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 5")

###############
# Import Libraries
import re

###############
## This function eliminates the spaces in a string
#
def no_spaces(text):
    result = re.sub(r"\s+", "", text, flags=re.UNICODE)
    return result

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
        # Validate that the response is a numeric value of type int or float
        if isinstance(correctResponse, str) == True:
            self._answer = correctResponse
        else: 
            print("The correct response must be a text (string)! Please correct and try again.")

    ##### 
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise 
    #
    def checkAnswer(self, response) :
        # Validate that the response is a numeric value of type int or float
        if isinstance(response, str) == True:
            return no_spaces(response.upper()) == no_spaces(self._answer.upper())
        else: 
            print("The correct response must be a text (string)! Please correct and try again.")        
        
    ##### 
    ## Displays this question. 
    #
    def display(self) :
        print(self._text)
              
###############    
## Class and Methods test      
# First, a questionTest is created as an instance of the Question class
questionTest = Question()  

# We set the text of the question and validate that the setText and display methods work properly
questionTest.setText("Who is the painter of Mona Lisa?")
questionTest.display()
print("The expected result is: Who is the painter of Mona Lisa?")

# We set the answer of the question and validate that the setAnswer and checkAnswer methods work properly
questionTest.setAnswer("Leonardo da Vinci") # The parameter of the setAnswer method is the correct response for the question
questionTest.checkAnswer("Leonardo da  Vinci ") # We set an answer that has additional spaces
print("The expected result is: True")
questionTest.checkAnswer("LeonaRdo Da VincI") # We set an answer that has some capital letters different from the correct response
print("The expected result is: True")

# Finally, we validate that the exceptions to the parameter types work
questionTest.setAnswer(5472) # We set a response that is not a string
print("The expected result is: The correct response must be a text (string)! Please correct and try again.")
questionTest.checkAnswer(False) # We set a response that is not numeric
print("The expected result is: The correct response must be a text (string)! Please correct and try again.")







