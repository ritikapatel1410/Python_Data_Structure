'''
 @Author: Ritika Patidar
 @Date: 2021-02-28 23:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-28 23:00:38  
 @Title : validiate name user regestration problem 
'''
import re
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def valid_first_name(first_name):
    """
    Description:
        this function is define for validiate name user regestration problem 
    Parameter:
       first_name (str) : first name of user
    Return:
       if first_name is valid then return valid name else return invalid name
    """
    if(re.match(r'^[A-Z]{1}[a-z]{2,}$',first_name)):
        return "valid name"
    else:
        return "invalid name" 

def valid_last_name(last_name):
    """
    Description:
        this function is define for validiate last name  user regestration problem 
    Parameter:
       last_name (str) : last name of user
    Return:
       if last_name is valid then return valid name else return invalid name
    """
    if(re.match(r'^[A-Z]{1}[a-z]{2,}$',last_name)):
        return "valid name"
    else:
        return "invalid name" 

def input_name(return_type):
    """
    Description:
        this function is define for take input as first or last name from user 
    Parameter:
       return_type (str) : first_name or last_name depends on which function called
    Return:
       return_type (str) : first_name or last_name depends on which function called
    """
    while True:
        try:
            if(return_type=="first_name"):
                first_name=input("enter first name: ")
                loggerfile.Logger("info","get first name successfully")
                return first_name
            elif(return_type=="last_name"):
                last_name=input("enter last name: ")
                loggerfile.Logger("info","get last name successfully")
                return last_name
            break
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
    

