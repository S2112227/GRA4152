#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:42:45 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE P10.21

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 6")

###############
## A bank account has a balance and a mechanism for applying interest or fees at the end of the month.
#
class BankAccount :   

    #####  
    ## Constructs a bank account with zero balance. 
    #
    def __init__(self) :
        self._balance = 0.0
         
    #####  
    ## Makes a deposit into this account.
    # @param amount the amount of the deposit 
    #
    def deposit(self, amount) :
        self._balance = self._balance + amount
        
    #####  
    ## Makes a withdrawal from this account, or charges a penalty if sufficient funds are not available.
    # @param amount the amount of the withdrawal 
    #
    def withdraw(self, amount) :
        self._balance = self._balance - amount
    
    #####  
    ## Carries out the end of month processing that is appropriate for this account.
    #
    def monthEnd(self) :
        raise NotImplementedError
        
    #####  
    ## Gets the current balance of this bank account. 
    # @return the current balance
    #
    def getBalance(self) :
        return self._balance


###############
## A savings account earns interest on the minimum balance. 
#
class SavingsAccount(BankAccount) :
    ##### 
    ## Constructs a savings account with a zero balance. 
    #
    def __init__(self, interestRate = 0.0) :
        super().__init__()
        self._minBalance = 0
        self._interestRate = interestRate

    ##### 
    ## Sets the interest rate for this account.
    # @param rate the monthly interest rate in percent 
    #
    def setInterestRate(self, rate) :
        self._interestRate = rate
    
    #####    
    ## These methods override superclass methods. 
    #
    def withdraw(self, amount) :
        super().withdraw(amount)
        balance = self.getBalance()
        if balance < self._minBalance :
            self._minBalance = balance
            
    def monthEnd(self) :
        interest = self._minBalance * self._interestRate / 100 
        self.deposit(interest)
        self._minBalance = self.getBalance()


###############
## A checking account checks the withdrawal count. If there have been too many withdrawals, a charge is applied. 
#
class CheckingAccount(BankAccount) :
    ##### 
    ## Constructs a checking account with a counter for the number of transactions.
    # @param freeTransactions is the number of monthly free transactions for the account
    # @param transactionCost is the cost of a single transaction after the number of free transactions has been exceeded
    #
    def __init__(self, freeTransactions = 3, transactionCost = 1) :
        super().__init__()
        self._numTransactions = 0
        self._freeTransactions = freeTransactions
        self._transactionCost = transactionCost

    #####  
    ## Makes a withdrawal from this account, and applies charges if there have been too many transactions.
    ## These method overrides the superclass method.
    # @param amount the amount of the withdrawal 
    #
    def withdraw(self, amount) :
        # Increase the number of transactions in the month by 1
        self._numTransactions += 1
        
        # Estimate the new balance which accounts for transaction costs in case they apply
        self._balance = self._balance - amount - self.transactionCost()
        print(f"The cost of the transaction is ${self.transactionCost()}")
    
    #####  
    ## Makes a deposit into this account, and applies charges if there have been too many transactions.
    ## These method overrides the superclass method.
    # @param amount the amount of the deposit 
    #
    def deposit(self, amount) :
        # Increase the number of transactions in the month by 1
        self._numTransactions += 1
        
        # Estimate the new balance which accounts for transaction costs in case they apply
        self._balance = self._balance + amount - self.transactionCost()
        print(f"The cost of the transaction is ${self.transactionCost()}")
    
    #####  
    ## Carries out the end of month processing that is appropriate for this account. In this case it resets the number of monthly transactions
    #
    def monthEnd(self) :
        self._numTransactions = 0        

    #####  
    ## Estimates the cost of a transaction (deposit or withdrawal in this case) depending on the number of transactions in the month.
    # @return the cost of the transaction
    #
    def transactionCost(self) :
        # Identify if the number of free monthly transactions has been exceeded
        if self._numTransactions > self._freeTransactions :
            return self._transactionCost
        else:
            return 0
        
        
###############    
## Class and Methods test      
# First, a checkingAccountTest is created as an instance of the CheckingAccount subclass which belongs to the BankAccount superclass
checkingAccountTest = CheckingAccount()

# The method deposit (from subclass) and getBalance (from superclass) are tested by making a deposit on the account and validating that the balance changes
checkingAccountTest.deposit(55) #A deposit of 55 is made to increasing the balance to 55. The transaction cost is $0
print("EXPECTED:\nThe cost of the transaction is $0")
checkingAccountTest.deposit(30) #A deposit of 30 is made to increasing the balance to 85. The transaction cost is $0
print("EXPECTED:\nThe cost of the transaction is $0")
checkingAccountTest.getBalance() #We use the getBalance method to obtain the balance from the account
print("The expected value is: 85")

# The method withdraw (from subclass) and getBalance (from superclass) are tested by making a withdrawal on the account and validating that the balance changes
checkingAccountTest.withdraw(10) #A withdrawal of 10 is made deccreasing the balance to 75
print("EXPECTED:\nThe cost of the transaction is $0")
checkingAccountTest.withdraw(20) #A withdrawal of 20 is made decreasing the balance to 54
print("EXPECTED:\nThe cost of the transaction is $1")
checkingAccountTest.getBalance() #We use the getBalance method to obtain the balance from the account
print("The expected value is: 54")

