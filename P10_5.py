#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 12:56:44 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE P10.5

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 6")

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

## This module defines the MultiChoiceQuestion class and adds this class to the Question hierarchy of Section 10.1.
## This subclass allows for multiple correct choices.
## This subclass overrides two of the methods from the Question superclass: setAnswer and checkAnswer
#
class MultiChoiceQuestion(Question):
    def __init__(self): 
        # Call the superclass constructor to define its instance variable.
        super().__init__()
    
    ##### 
    ## This method overrides the Question class method with the same name to allow for multiple responses.
    # @param *correctResponses is a number of correct answers defined by the user. This parameter works as *args to receive a unique or multiple answers 
    #
    def setAnswer(self, *correctResponses) :     
        # Transform the unique or multiple correctResponses into a list where all the elements are strings
        self._answer = [str(i) for i in list(correctResponses)]
    
    ##### 
    ## This method overrides the Question class method with the same name to receive and validate unique or multiple responses.
    # @param response is the unique or multiple responses to check against the correct responses
    # @return True if the response or multiple responses are correct, False otherwise 
    #
    def checkAnswer(self, responses):
        # Validate that the responses are a string
        if isinstance(responses, str) == True:
            # Separate the string into multiple elements of a list using the spaces in the string
            responses_split = list(map(str, str(responses).split(' ')))
            
            # Sort the elements of the two lists (self._answer and  responeses) to properly compare the lists
            if sorted(self._answer) == sorted(responses_split) :
                return True
            else:
                return False
                print("Incorrect answer(s)! Please correct and try again. Remember that answers must be separated by spaces")
        else:
            print("The response must be a string which includes all the correct answers separated by space! Please correct and try again.")
    
###############    
## Class and Methods test      
# First, a questionTest is created as an instance of the MultiChoiceQuestion class
questionTest = MultiChoiceQuestion()  

# We set the text of the question and validate that the setText and display methods work properly
questionTest.setText("Which countries joined the EU in January 2007?\n- Bulgaria\n- Poland\n- Croatia\n- Turkey\n- Romania\n- Albania")
questionTest.display()
print("EXPECTED:\nWhich countries joined the EU in January 2007?\n- Bulgaria\n- Poland\n- Croatia\n- Turkey\n- Romania\n- Albania")

# We set the answerS of the question and validate that the setAnswer and checkAnswer methods work properly
questionTest.setAnswer("Bulgaria", "Turkey") # The parameter of the setAnswer method is the correct response for the operation 5/6
questionTest.checkAnswer("Turkey Bulgaria") # We set a response that is not in the same order as the options in the question
print("The expected result is: True")
questionTest.checkAnswer("Turkey") # We set a response that is incomplete
print("The expected result is: False")
questionTest.checkAnswer("Poland Turkey") # We set a response that is incorrect
print("The expected result is: False")

# Finally, we validate that the exceptions to the parameter types work
questionTest.checkAnswer(23) # We set a response that is not a string
print("The response must be a string which includes all the correct answers separated by space! Please correct and try again.")
