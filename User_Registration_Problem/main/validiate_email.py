'''
 @Author: Ritika Patidar
 @Date: 2021-02-28 23:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-28 23:00:38  
 @Title : validiate email id of user regestration problem 
'''
import re
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def valid_email(email_id):
    """
    Description:
        this function is define for validiate email id of user 
    Parameter:
       email_id (str) : email id of user
    Return:
       if email id is valid then return valid email id else return invalid email id
    """
    pattern=re.compile("^(abc).[a-z0-9]{1,}[@](bl)+[.](co)+[.](in|com|org)$")
    if(pattern.match(email_id)):
        return "valid email id"
    else:
        return "invalid email id" 

def input_email():
    """
    Description:
        this function is define for take input as email id from user 
    Parameter:
       None
    Return:
       return_type (str) : email id 
    """
    while True:
        try:
            first_name=input("enter email id: ")
            return first_name
            loggerfile.Logger("info","get email id successfully")
            break
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
    

