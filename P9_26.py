#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:44:33 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE P9.26

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 3")

###############
## This module defines the Customer class
#
class Customer:   
    """
    This class models a customer loyalty marketing campaign. In this campaign, after accumulating $100 in purchases,
    the customer receives a $10 discount on the next purchase. In that sense, once the $100 amount is reached 
    the fixed discount ($10) is obtained and will be redeemable in the next purchase.
    The class has methods that allow to:
    - Make a purchase by indicating the amount of the purchase. At the moment of the purchase, the system validates
    whether there is a discount to apply
    - Identify whether the discount amount ($100) has been reached and the customer is eligible for the discount
    
    """
    #####
    ## Define the constructor for the class 
    #
    def __init__(self):
        self._totalAmountCampaign = 0 #Total amount spent by the customer taking into account previous discounts
        self._discount = 10 #Discount applied to the next purchase
   
    #####
    ## The method evaluates if the discount applies and applies it or adds the value of the purchase to the total amount spent by the customer that counts for the discount    
    #
    def makePurchase(self, amount):
       if self.discountReached() == True: #If the customer has already accumulated a minimum of $100 in purchases, the next purchase has the discount
           self._totalAmountCampaign = amount - self._discount #After obtaining a discount the value accumulated is reset to the excess value after $100
           print(f"The total for the purchase with the discount is: ${amount - self._discount}")
       else: #If the customer has not reached the discount, the amount of the purchase is accumulated for a future discount
           self._totalAmountCampaign = self._totalAmountCampaign + amount 
           print(f"The total for the purchase is: ${amount}")
   
    #####
    ## The method discountReached validates whether the customer has reached the condition to obtain the $10 discount and returns a boolean
    #
    def discountReached(self):
       if self._totalAmountCampaign >= 100: #If the customer has already accumulated a minimum of $100 in purchases, the next purchase has the discount
           print(f"The customer has a ${self._discount} discount!")    
           return True
       else: 
           print("The customer has not obtained the discount yet!") 
           return False

###############    
## Class and Methods test
# First, a customer is created as an instance of the Customer class
customer1 = Customer()

# The methods "makePurchase" and "discountReached" are tested
# Provide a test program and test a scenario in which a customer has earned a discount and then made over $90, 
# but less than $100 in purchases. This should not result in a second discount. 
# Then add another purchase that results in the second discount.
customer1.makePurchase(100) #The customer earns the discount after this purchase
customer1.makePurchase(20) #For this purchase, the discount applies
customer1.makePurchase(85) #For this purchase, the customer has not earned the $10 discount but has an accumulated value of $95
customer1.makePurchase(20) #After this purchase, the customer has earned the $10 discount again
customer1.makePurchase(70) #On this purchase, the second discount earned applies


