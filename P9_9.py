#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:28:59 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE P9.9

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 4")

###############
## This module defines the ComboLock class
#  
class ComboLock:   
   """
   This class models a combination lock in a gym locker. The lock is constructed with a combination of three numbers between 0 and 39. 
   The lock opens if the user first turned it right to the first number in the combination, then left to the second, and then right to the third.
   The class contains the following methods:
   - ComboLock: Allows the user to assign the secret combination composed by three numbers.
   - reset: Allows the user to place the dial in 0.
   - turnRight: Moves the dial a specific number of ticks to the right and allows to unlock the first and third number.
   - turnLeft: Moves the dial a specific number of ticks to the left and allows to unlock the second number. 
   - open: Allows the user to attempt to open the lock.
   """
   #####
   ## Define the constructor for the class 
   #
   def __init__(self):
       self._dial = 0 #The lock initiates with the dial on 0
       self._isUnlocked = True #The lock initiates unlocked
       self._secret1 = 0
       self._secret1IsUnlocked = True
       self._secret2 = 0
       self._secret2IsUnlocked = True
       self._secret3 = 0 
       self._secret3IsUnlocked = True
       self._movement = 1
   #####
   ## The method allows the user to assign the combination and lock the combination lock
   #
   def ComboLock(self, secret1, secret2, secret3):
       if self._isUnlocked == True:
           self._secret1 = secret1 #First number in the secret code
           self._secret2 = secret2 #Second number in the secret code
           self._secret3 = secret3 #Third number in the secret code    
           self._isUnlocked = False #The combination lock is locked
           print("The combination was succesfully assigned!")
       else:
           print("It is not possible to assign the combination. Unlock first!")
   #####
   ## The reset method resets the dial so that it points to 0. 
   #
   def reset(self):
        self._dial = 0 
        print("The dial has been set to 0!")
   
   #####
   ## The turnRight method moves the dial a specific number of ticks to the right and allows to unlock the first and third number. 
   #
   def turnRigth(self, ticks):    
       if ticks >= 40: #Validate that the number of ticks is not greater than 39
           print("The number of ticks cannot be greater than 39!")
       else:
           self._dial = self._dial + ticks - int((self._dial + abs(ticks))/40)*40 #Move the dial to the right           

           if self._movement == 1 and self._secret1 == self._dial: #Turning to the right only helps to open the lock when trying to input the first or third number
               self._secret1IsUnlocked = True
               self._movement = 2 #The user moves forward to the second number    
           elif self._movement == 3 and self._secret3 == self._dial:
               self._secret3IsUnlocked = True #All three numbers are unlocked and the user can open the lock with the open method 
           else:
               self._secret1IsUnlocked = False
               self._secret2IsUnlocked = False
               self._secret3IsUnlocked = False
               self._movement = 1 #The user must start over with the first number   
   
   #####
   ## The turnLeft method moves the dial a specific number of ticks to the left and allows to unlock the second number. 
   #
   def turnLeft(self, ticks):     
       if ticks > 39: #Validate that the number of ticks is not greater than 39
           print("The number of ticks cannot be greater than 39!")
       else:         
           if self._dial - ticks < 0:
               self._dial = 40 + self._dial - ticks - int((self._dial - ticks)/40)*40 #Move the dial to the left
           else:
               self._dial = self._dial - ticks #Move the dial to the left
           if self._dial == 40:
               self._dial = 0 

           if self._movement == 2 and self._secret2 == self._dial: #Turning to the left only helps to open the lock when trying to input the second number (second movement)
               self._secret2IsUnlocked = True
               self._movement = 3 #The user moves forward to the third number  
           else: #When the user turns the dial to the left but it is not for the second movement, all the three secret numbers get locked again
               self._secret1IsUnlocked = False
               self._secret2IsUnlocked = False
               self._secret3IsUnlocked = False
               self._movement = 1 #The user must start over with the first number           
       
   #####
   ## The open method attempts to open the lock 
   #
   def open(self):
        if self._secret1IsUnlocked == True and self._secret2IsUnlocked == True and self._secret3IsUnlocked == True:
            self._isUnlocked = True
            self._movement = 1
            print("The lock has been sucessfully unlocked!")
        else:
            print("Incorrect combination! Try again.")
   
###############    
## Class and Methods test
# First, a lock is created as an instance of the ComboLock class
MyFirstLock = ComboLock()

# The method ComboLock is tested by setting a secret combination and testing that it cannot be changed until the lock is unlocked
MyFirstLock.ComboLock(5, 37, 25) #The secret combination is assigned
MyFirstLock.ComboLock(15, 6, 18) #Since the lock is locked, a new combination cannot be assigned until the lock is open

# The methods turnRight, turnLeft and open are tested by making the correct movements to unlock the lock
MyFirstLock.turnRigth(45) #The number of ticks must be lower or equal than 39
MyFirstLock.turnRigth(5) #Since the dial begins on 0, we move it 5 ticks to the right
MyFirstLock.turnLeft(59) #The number of ticks must be lower or equal than 39
MyFirstLock.turnLeft(8) #To get to 37 from 5, we move the dial 8 ticks to the left
MyFirstLock.turnRigth(28) #Finally, to get to 28 from 37, we move the dial 28 ticks to the right
MyFirstLock.open() #The lock can be open

# The reset method is tested by assigning a new secret combination an unlocking the lock again
MyFirstLock.reset()
MyFirstLock.ComboLock(15, 6, 18) #A new secret combination is assigned
MyFirstLock.turnRigth(15) #Since the dial begins on 0, we move it 15 ticks to the right
MyFirstLock.turnLeft(9) #To get to 6 from 15, we move the dial 9 ticks to the left
MyFirstLock.turnRigth(12) #Finally, to get to 18 from 6, we move the dial 12 ticks to the right
MyFirstLock.open() #The lock can be open


