#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:11:53 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE P9.4

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 3")

###############
## This module defines the Address class
# 
class Address:   
   """This class models the different components of an address and allows to: 
       - Print the address (print)
       - Compare addresses by postal code (comesBefore)
       The class is initialized with the following attributes: house number, street, city, state, postal code, and apartment number.
       The apartment number is an optional attribute which is set as empty by default
   """
   #####
   ## Define the constructor for the class where apartmentNumber is an optional variable
   #
   def __init__(self, houseNumber, street, city, state, postalCode, apartmentNumber = None):
       self._houseNumber = houseNumber
       self._street = street
       self._city = city
       self._state = state
       self._postalCode = postalCode
       self._apartmentNumber = apartmentNumber  #The attribute apartmentNumber is set as empty by default
   
    #####
   ## The method print allows to print the address stored in two lines. The first line includes the street and the second the city, state, and postal code    
   #
   def print(self):
      return print(f"{self._street}\n{self._city}, {self._state}, {self._postalCode}")
  
   #####
   ## The method comesBefore tests whether this addres (self) comes before other when compared by postal code    
   #
   def comesBefore(self, other):
      if isinstance(other, Address) == True:
          if int(self._postalCode) < int(other._postalCode): #Since postal codes are entered as string, they are converted to integers to compare them
              print(f"The first address comes before the second address.")
          else:
              print(f"The first address does not come before the second address.")
      else:
          print(f"Error. The second address must be an object of type Address.")

###############    
## Class and Methods test
# First, two different addresses are created as instances of the Address class
address1 = Address("15", "Sinsenveien", "Oslo", "Oslo", "0572")
address2 = Address("60", "Olav M. Troviksvei", "Oslo", "Oslo", "0862")

# The first method "print" is tested for both of the addresses created. It is expected to see the address printed in two lines
address1.print()
address2.print()

# The second method "comesBefore" is tested by comparing the postal code of the address 1 with the postal code of the address 2
# Since the postal code of the address 1 is smaller than the postal code of the address 2, the method prints a message indicating that the address 1 comes before the address 2
address1.comesBefore(address2)

          