#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:40:39 2022

@author: dmalagont
"""
######################################################################
### OBJECT ORIENTED PROGRAMMING - EXERCISE P10.24

###############
# Set Working Directory
import os
os.getcwd()
os.chdir("/Users/dmalagont/Documents/Educación/BI Norwegian Business School/Object Oriented Programming/Assignments/Lecture 7")

###############
## This module defines a superclass that models an Appointment. An Appointment has a description (for example, “see the dentist”) and a date.
#
class Appointment : # Superclass
 
   #####  
   ## Constructs an Appointment with a description a time (hour:minutes) and a date (day/month/year). 
   # @param description is the description of the Appointment
   # @param hour is the hour of the Appointment's time
   # @param minutes is the minutes of the Appointment's time
   # @param day is the day of the Appointment  
   # @param month is the month of the Appointment  
   # @param year is the year of the Appointment   
   #
   def __init__(self, description, hour, minutes, day, month, year) :
       # Validate the constructor inputs
       if isinstance(description, str)==True and isinstance(hour, int)==True and isinstance(minutes, int)==True and isinstance(day, int)==True and isinstance(month, int)==True and isinstance(year, int)==True:
           if hour >= 0 and hour < 24:
               if minutes >= 0 and minutes < 59:
                   self._description = description
                   self._hour = hour
                   self._minutes = minutes
                   self._day = day
                   self._month = month
                   self._year = year
               else:
                   print("The minutes must be a number between 0 and 59! Please correct and try again.")
           else:
               print("The hour must be ga number between 0 and 23! Please correct and try again.")
       else:
            print("The description must be a text (string) and the components of the time and date must be numbers (integers)! Please correct and try again.")   
    
   #####  
   ## Allows to obtain the description of the Appointment. 
   # @return description of the appointment
   #       
   def getDescription(self) :
       return self._description
    
   #####  
   ## Allows to set the description of the Appointment. 
   # @param description is the description of the Appointment
   #      
   def setDescription(self, description) :
       # Validate the function input
       if isinstance(description, str)==True:
           self._description = description
       else:
           print("The description must be a text (string)! Please correct and try again.")   
      
   #####  
   ## Allows to obtain the time of the Appointment. 
   # @return hour of the appointment
   #       
   def getTime(self) :
       return self._hour, self._minutes

   #####  
   ## Allows to set the hour of the Appointment. 
   # @param hour is the hour of the Appointment  
   #  
   def setHour(self, hour) :
       # Validate the function input
       if isinstance(hour, int)==True and hour >= 0 and hour < 24:
           self._hour = hour 
       else:
           print("The hour must be a number (integer) between 0 and 23! Please correct and try again.")             

   #####  
   ## Allows to set the minutes of the Appointment. 
   # @param hour is the minutes of the Appointment  
   #  
   def setMinutes(self, minutes) :
       # Validate the function input
       if isinstance(minutes, int)==True and minutes >= 0 and minutes < 24:
           self._minutes = minutes
       else:
           print("The minutes must be a number (integer) between 0 and 59! Please correct and try again.")             
            
   #####  
   ## Allows to obtain the day of the Appointment. 
   #       
   def getDay(self) :
       return self._day

   #####  
   ## Allows to set the day of the Appointment. 
   # @param day is the day of the Appointment  
   #  
   def setDay(self, day) :
       # Validate the function input
       if isinstance(day, int)==True:
           self._day = day 
       else:
           print("The day must be a number (integer)! Please correct and try again.")   
       
   #####  
   ## Allows to obtain the month of the Appointment. 
   #       
   def getMonth(self) :
       return self._month

   #####  
   ## Allows to set the month of the Appointment. 
   # @param month is the month of the Appointment  
   #
   def setMonth(self, month) :
       # Validate the function input
       if isinstance(month, int)==True:
           self._month = month 
       else:
           print("The month must be a number (integer)! Please correct and try again.")           
   
   #####  
   ## Allows to obtain the year of the Appointment. 
   #       
   def getYear(self) :
       return self._year

   #####  
   ## Allows to set the year of the Appointment. 
   # @param year is the year of the Appointment  
   #
   def setYear(self, year) :
       # Validate the function input
       if isinstance(year, int)==True:
           self._year = year 
       else:
           print("The year must be a number (integer)! Please correct and try again.")         

   #####
   ## Definition of the __repr__ of the Appointment object.
   #
   def __repr__(self) :
       return f"{self._description} at {self._hour}:{self._minutes} on {self._day}/{self._month}/{self._year}"

   #####
   ## Checks whether the Appointment occurs on a given date.
   #
   def occursOn(self, day, month, year) :
       raise NotImplementedError
    
   #####
   ## Saves the appointment data to a given file.
   #
   def save(self, filename):
       raise NotImplementedError  

###############
## This module defines a subclass that models a One Time Appointment. A One Time appointment has a description (for example, “see the dentist”), a time and a date.
#
class OneTime (Appointment) : # Subclass

   #####  
   ## Constructs a One Time Appointment with a description, a time and a date (day/month/year). 
   # @param description is the description of the Appointment
   # @param hour is the hour of the Appointment's time
   # @param minutes is the minutes of the Appointment's time
   # @param day is the day of the Appointment  
   # @param month is the month of the Appointment  
   # @param year is the year of the Appointment   
   #
   def __init__(self, description, hour, minutes, day, month, year) :
       # Use the Superclass constructor
       super().__init__(description, hour, minutes, day, month, year)

   #####
   ## Definition of the __repr__ of the OneTime object.
   #
   def __repr__(self) :
       return "One Time Appointment - " + super().__repr__()

   #####
   ## Checks whether the Appointment occurs on a given date (validates day, month, and year)
   # @param day is the day to be validated  
   # @param month is the month to be validated  
   # @param year is the year to be validated 
   #
   def occursOn(self, day, month, year) :
       if isinstance(day, int)==True and isinstance(month, int)==True and isinstance(year, int)==True:
           if self.getDay()==day and self.getMonth()==month and self.getYear()==year:
               return True
           else:
               return False
       else:
           print("The components of the date must be numbers (integers)! Please correct and try again.")   

   #####
   ## Saves the appointment data to a given file.
   #  @param filename is the name of the file
   #
   def save(self, filename) :
       # Create a file and open it
       file = open(filename, "a")
       text  = "OneTime;" + str(self._description) + ";" + str(self._hour) +";" + str(self._minutes) + ";" + str(self._day) + ";" + str(self._month) + ";" + str(self._year) + "\n"
       # Append text to the file
       file.write(text)
       # Close the file
       file.close()

###############
## This module defines a subclass that models a Daily Appointment. A Daily appointment has a description (for example, “see the dentist”), a time and a date.
#
class Daily (Appointment) : # Subclass

   #####  
   ## Constructs a Daily Appointment with a description, a time and a date (day/month/year). 
   # @param description is the description of the Appointment
   # @param hour is the hour of the Appointment's time
   # @param minutes is the minutes of the Appointment's time
   # @param day is the day of the Appointment  
   # @param month is the month of the Appointment  
   # @param year is the year of the Appointment   
   #
   def __init__(self, description, hour, minutes, day, month, year) :
       # Use the Superclass constructor
       super().__init__(description, hour, minutes, day, month, year)

   #####
   ## Definition of the __repr__ of the Daily object.
   #
   def __repr__(self) :
       return "Daily Appointment - " + super().__repr__()
   
   #####
   ## Checks whether the Appointment occurs on a given date (validates day, month, and year).
   # @param day is the day to be validated  
   # @param month is the month to be validated  
   # @param year is the year to be validated 
   #
   def occursOn(self, day, month, year) :
       if isinstance(day, int)==True and isinstance(month, int)==True and isinstance(year, int)==True:
           # Validates daily events except future events.
           if self.getDay()<day or self.getMonth()<month or self.getYear()<year:
               return True
           else:
               return False
       else:
           print("The components of the date must be numbers (integers)! Please correct and try again.")  

   #####
   ## Saves the appointment data to a given file.
   #  @param filename is the name of the file
   #
   def save(self, filename) :
       # Create a file and open it
       file = open(filename, "a")
       text  = "Daily;" + str(self._description) + ";" + str(self._hour) + ";" + str(self._minutes) + ";" + str(self._day) + ";" + str(self._month) + ";" + str(self._year) + "\n"
       # Append text to the file
       file.write(text)
       # Close the file
       file.close()

###############
## This module defines a subclass that models a Monthly Appointment. A Monthly appointment has a description (for example, “see the dentist”), a time and a date.
#
class Monthly (Appointment) : # Subclass

   #####  
   ## Constructs a Monthly Appointment with a description, a time and a date (day/month/year). 
   # @param description is the description of the Appointment
   # @param hour is the hour of the Appointment's time
   # @param minutes is the minutes of the Appointment's time
   # @param day is the day of the Appointment  
   # @param month is the month of the Appointment  
   # @param year is the year of the Appointment   
   #
   def __init__(self, description, hour, minutes, day, month, year) :
       # Use the Superclass constructor
       super().__init__(description, hour, minutes, day, month, year)

   #####
   ## Definition of the __repr__ of the Monthly object.
   #
   def __repr__(self) :
       return "Monthly Appointment - " + super().__repr__()

   #####
   ## Checks whether the Appointment occurs on a given date (validates day, month, and year).
   # @param day is the day to be validated  
   # @param month is the month to be validated  
   # @param year is the year to be validated 
   #
   def occursOn(self, day, month, year) :
       if isinstance(day, int)==True and isinstance(month, int)==True and isinstance(year, int)==True:
           # Validates daily events except future events.
           if self.getDay()==day and (self.getMonth()<month or self.getYear()<year):
               return True
           else:
               return False
       else:
           print("The components of the date must be numbers (integers)! Please correct and try again.")  

   #####
   ## Saves the appointment data to a given file.
   #  @param filename is the name of the file
   #
   def save(self, filename) :
       # Create a file and open it
       file = open(filename, "a")
       text  = "Monthly;" + str(self._description) + ";" + str(self._hour) + ";" + str(self._minutes) + ";" + str(self._day) + ";" + str(self._month) + ";" + str(self._year) + "\n"
       # Append text to the file
       file.write(text)
       # Close the file
       file.close()
       
###############    
## The exercise from the book is ambiguous with regards to the load method. 
## The implementation within the Appointment class was not clear and therefore a function was created.
## Loads a file with appointment's data.
#  @param filename is the name of the file
#  @return is a list filled with the different appointments (objects) in the file
#
def load(filename) :
    # Open file from working directory
    file = open(filename, "r")
        
    # Create an empty list
    appointments= []
        
    # Split the file using the same character used to split when saving the file
    for i in file :
        i = i.strip()
        split = i.split(";")
            
        # Idenfity the object type and retrieve the data
        if split[0] == "OneTime" :
            appointments.append(OneTime(str(split[1]), int(split[2]), int(split[3]), int(split[4]), int(split[5]), int(split[6])))
        elif split[0] == "Monthly" :
            appointments.append(Monthly(str(split[1]), int(split[2]), int(split[3]), int(split[4]), int(split[5]), int(split[6])))
        elif split[0] == "Daily" :
            appointments.append(OneTime(str(split[1]), int(split[2]), int(split[3]), int(split[4]), int(split[5]), int(split[6])))
            i = i.strip()
                        
        # Close the file
        file.close()
        return appointments      
     
###############    
## Class and Methods test      
# First, an appointments list is created and filled with instances of the Appointment subclasses
appointments = []
appointments.append(OneTime("Christmas Dinner", 19, 30, 1, 12, 2022))
appointments.append(Daily("Buy groceries", 18, 10, 24, 10, 2022))
appointments.append(Monthly("Pay Netflix", 8, 15, 1, 11, 2022))
appointments.append(OneTime("Visit High School friends", 12, 45, 9, 12, 2022))
appointments.append(Daily("Yoga class", 7, 40, 25, 10, 2022))
appointments.append(Monthly("Pay rent", 8, 30, 1, 12, 2022))

# Second, all the appointments are saved to a file
for i in range(len(appointments)) :
    appointments[i].save("appointments.txt")

# Third, the appointments' data from the file is retrieved and printed
appointments_file = load("appointments.txt")
appointments_file

for i in range(len(appointments_file)) :
    print(appointments[i])

