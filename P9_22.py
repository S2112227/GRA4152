#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 13:19:32 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE P9.22

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 4")

###############
## This module defines the BankAccount class. A bank account has a balance that can be changed by deposits and withdrawals.
# 
class BankAccount:
    #####
    ## Constructs a bank account with a given balance.
    ## @param initialBalance the initial account balance (default = 0.0) 
    #
    def __init__(self, initialBalance = 0.0):
        self._balance = initialBalance
 
    #####
    ## Deposits money into this account.
    ## @param amount the amount to deposit 
    #
    def deposit(self, amount):
        self._balance = self._balance + amount
    
    #####
    ## Makes a withdrawal from this account, or charges a penalty if sufficient funds are not available.
    ## @param amount the amount of the withdrawal 
    #
    def withdraw(self, amount):
        PENALTY = 10.0
        if amount > self._balance:
            self._balance = self._balance - PENALTY
        else:
            self._balance = self._balance - amount
    
    #####
    ## Adds interest to this account.
    ## @param rate the interest rate in percent
    #
    def addInterest(self, rate):
        amount = self._balance * rate / 100.0 
        self._balance = self._balance + amount
      
    #####    
    ## Gets the current balance of this account. # @return the current balance
    #
    def getBalance(self):
        return self._balance

###############
## This module defines the Portfolio class.
# 
class Portfolio:
    """
    This class models a portfolio that contains two accounts of the class BankAccount defined earlier:Cheking and Savings.
    The class contains the following methods:
    - deposit: Allows the user to make a deposit in either of the accounts.
    - withdraw: Allows the user to withdraw from either of the accounts.
    - transfer: Allows the user to transfer from one account to the other.
    """
    #####
    ## Define the constructor for the class 
    #
    def __init__(self, initialBalanceChecking = 0.0, initialBalanceSavings = 0.0):
        self._checking = BankAccount(initialBalanceChecking)
        self._savings = BankAccount(initialBalanceSavings)

    #####
    ## The deposit method allows to make a deposit of a certain amount on the account chosen ("S" or "C").
    #
    def deposit(self, amount, account):
        if account == "S": #Check if the account is a savings account
            self._savings.deposit(amount)
        elif account == "C": #Check if the account is checking account
            self._checking.deposit(amount)
        else:
            print("The account must be either 'S' or 'C'! Please input a correct value.")

    #####
    ## The withdraw method allows to make a withdrawal of a certain amount from the account chosen ("S" or "C").
    #
    def withdraw(self, amount, account):
        if account == "S": #Check if the account is a savings account
            self._savings.withdraw(amount)
        elif account == "C": #Check if the account is checking account
            self._checking.withdraw(amount)
        else:
            print("The account must be either 'S' or 'C'! Please input a correct value.")

    #####
    ## The transfer method allows to make a transfer of from the account chosen ("S" or "C") to the other account in the portfolio.
    #
    def transfer(self, amount, account):
        if account == "S": #Check if the account is a savings account
            self._savings.withdraw(amount)
            self._checking.deposit(amount)
        elif account == "C": #Check if the account is checking account
            self._checking.withdraw(amount)
            self._savings.deposit(amount)
        else:
            print("The account must be either 'S' or 'C'! Please input a correct value.")        

    #####
    ## The getBalance method allows to obtain the balance from the account chosen ("S" or "C").
    #
    def getBalance(self, account):
        result = None
        if account == "S": #Check if the account is a savings account
            result = self._savings.getBalance()
        elif account == "C": #Check if the account is checking account
            result = self._checking.getBalance()
        else:
            print("The account must be either 'S' or 'C'! Please input a correct value.") 
        
        return result
            
###############    
## Class and Methods test      
# First, a portfolio is created as an instance of the Portfolio class
checking = 150
savings = 300
portfolio1 = Portfolio(checking, savings)

# The method deposit and getBalance are tested by making a deposit on the savings and checking account and validating that the balance changes
portfolio1.deposit(55, "C") #A deposit of 55 is made to the checking account increasing the balance to 205
portfolio1.deposit(30, "S") #A deposit of 30 is made to the savings account increasing the balance to 330
portfolio1.getBalance("C") #We use the getBalance method to obtain the balance from the cheking account
print("The expected value is: 205")
portfolio1.getBalance("S") #We use the getBalance method to obtain the balance from the savings account
print("The expected value is: 330")

# The method withdraw and getBalance are tested by making a withdrawal on the savings and checking account and validating that the balance changes
portfolio1.withdraw(10, "C") #A withdrawal of 10 is made to the checking account deccreasing the balance to 195
portfolio1.withdraw(20, "S") #A withdrawal of 20 is made to the savings account increasing the balance to 310
portfolio1.getBalance("C") #We use the getBalance method to obtain the balance from the cheking account
print("The expected value is: 195")
portfolio1.getBalance("S") #We use the getBalance method to obtain the balance from the savings account
print("The expected value is: 310")

# The method transfer and getBalance are tested by making a transfer on from both accounts and validating that the balance changes
portfolio1.transfer(35, "C") #A transfer of 35 is made from the cheking account to the savings account
portfolio1.getBalance("C") #We use the getBalance method to obtain the balance from the cheking account
print("The expected value is: 160")
portfolio1.getBalance("S") #We use the getBalance method to obtain the balance from the savings account
print("The expected value is: 345")
portfolio1.transfer(15, "S") #A transfer of 15 is made froom the savings account to the checking account
portfolio1.getBalance("S") #We use the getBalance method to obtain the balance from the savings account
print("The expected value is: 330")
portfolio1.getBalance("C") #We use the getBalance method to obtain the balance from the cheking account
print("The expected value is: 175")

# Finally, all methods are tested with regards to an invalid account (character)
portfolio1.deposit(1, "X") 
portfolio1.withdraw(1, "X") 
portfolio1.transfer(1, "X") 
portfolio1.getBalance("X") 
print("The expected message is: The account must be either 'S' or 'C'! Please input a correct value.")
