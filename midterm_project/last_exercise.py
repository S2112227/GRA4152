#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:19:22 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE ARGPARSE

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 9")

#############
# Import Libraries
import argparse
import textwrap
import statsmodels.api as sm
import numpy as np
from DataSet import * # from midterm project
from models_commented import * # from midterm project
from diagnosticPlot import * # from midterm project

###############
## Create Object
# We create an argparse object ready to take arguments
parser = argparse.ArgumentParser(description = "Generate Logistic Regression Models")

###############
## Create Help Description
# We create a description for the argparse object to define
parser = argparse.ArgumentParser(prog='Logistic Regression test program',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                                            Logistic Regression
                                     --------------------------------
                                     Allows to implement a Logistic Regression model on the spector dataset from statsmodels. 
                                     
                                     Using the spector dataset, the user can specify a seed and the percentage of train or test data. With these parameters, the code randomly splits the dataset. 
                                     
                                     After splitting the data set, the code uses the train set to fit the parameters (betas). To do this the code minimizes the model's deviance. 
                                     
                                     A Model Summary is provided and includes:
                                         - Model
                                         - Parameters
                                         - Accuracy (area under ROC curve)
                                      
                                     Finally, the code allows the user to plot the ROC curve.
                                     
                                     To implement the Logistic Regression the code uses the following packages:
                                         - DataSet
                                         - models
                                         - diagnosticPlot
                                    '''),
        epilog=textwrap.dedent('''\
                                     --------------------------------
                                     See documentation for the DataSet, models, and diagnosticPlot libraries for more information about the Logistic Regression implementation.
                                    ''')
                    )
parser.print_help()


###############
## Add Arguments
# We add to the parser all the arguments required for the LogisticRegression class

# The first argument we add is the seed for the random train/test split
parser.add_argument('-s', '--seed', metavar="", default= 1234, type= int, help='Random seed for data set train/test split. Default value is provided')

# For the percentages of train and test, we create a mutually exclusive group. This because both percentages are related.
group = parser.add_mutually_exclusive_group()
group.add_argument('-ptr', '--percentageTrain', default= 0.7, type= float, 
                   help='Percentage of train data from the data set. Default value is provided. Set either percentage of train data or percentage of test data')
group.add_argument('-pte', '--percentageTest', type= float, 
                   help='Percentage of test data from the data set. Set either percentage of train data or percentage of test data')

# We add an argument with choices for the covariates (model). Thus, the user can pick from several models provided.
parser.add_argument('-m', '--model', default="y ~ b0 + b1*x1", type= str, 
                    choices=["y ~ b0 + b1*x1", "y ~ b0 + b1*x1 + b2*x2", "y ~ b0 + b1*x1 + b2*x2 + b3*x3"], 
                    help='Covariates in the model. You can only choose one model among the options. Default value is provided')

# Finally, we add an argument for the user to decide whether to generate or not a diagnostic plot. The action "store_true" indicates that the default is False, but when the arg is called it becomes True.
parser.add_argument('-pl', '--plot', action='store_true', 
                    help='Plot the ROC Curve for the model. Default value is provided in the action propety. If given, its value is True')
    

###############
## Pass Arguments to an Object that retrives arguments with property-decorator style
args = parser.parse_args()
print("\n", args, "\n")

#!python3 parsing.py

###############    
## Argparse Test   
# Load the Spector Data Set from Statsmodels and load the dependent variable and the covariates
spector_data = sm.datasets.spector.load()
x = np.array(spector_data.exog)
y = np.array(spector_data.endog)

# Create a DataSet object with the dependent variable and the covariates loaded from Statsmodels. 
dataTest = DataSet(x, y, horizontal_x = False, scale = False)
# add intercept
dataTest.add_constant()
# Create a train and test set using the seed value and train/test split from argparse
if args.percentageTest == None:
    dataTest.train_test(trainSize = args.percentageTrain, randomSeed = args.seed)
else:
    dataTest.train_test(trainSize = 1-args.percentageTest, randomSeed = args.seed)
    
# Define and fit model parameters for the model specified by the user using argparse
logRegression_1 = LogisticRegression(dataTest.x_tr, dataTest.y_tr, horizontal_x = True)
logRegression_1.linearModel(args.model)
logRegression_1.fit(logRegression_1.params, logRegression_1.x, logRegression_1.y)
logRegression_1.optimize(init_val=1)
logRegression_1.summary()

# Depending on the value of the argparse' plot argument, use the diagnosticPlot class to plot the results of the logistic regression
if args.plot == True:
    if args.model == "y ~ b0 + b1*x1" :
        diagnostic_1 = diagnosticPlot(logRegression_1)
        diagnostic_1.plot(dataTest.y_te, logRegression_1.predict(logRegression_1.params, dataTest.x_te[0:2,:]))
    elif args.model == "y ~ b0 + b1*x1 + b2*x2" :
        diagnostic_2 = diagnosticPlot(logRegression_1)
        diagnostic_2.plot(dataTest.y_te, logRegression_1.predict(logRegression_1.params,dataTest.x_te[0:3,:])) 
    elif args.model == "y ~ b0 + b1*x1 + b2*x2 + b3*x3" :         
        diagnostic_3 = diagnosticPlot(logRegression_1)
        diagnostic_3.plot(dataTest.y_te, logRegression_1.predict(logRegression_1.params, dataTest.x_te)) 



