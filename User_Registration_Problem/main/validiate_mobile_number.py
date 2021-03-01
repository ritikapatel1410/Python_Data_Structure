'''
 @Author: Ritika Patidar
 @Date: 2021-02-28 23:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-28 23:00:38  
 @Title : validiate mobile number of user regestration problem 
'''
import re
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def valid_mobile_number(mobile_no):
    """
    Description:
        this function is define for validiate mobile number of user 
    Parameter:
       mobile_no. (str) : mobile number of user
    Return:
       if mobile number is valid then return valid mobile number else return invalid mobile number
    """
    Pattern = re.compile("^(91 )[7-9][0-9]{9}$")
    if(Pattern.match(mobile_no)):
        return "valid mobile number"
    else:
        return "invalid mobile number" 

def input_mobile_no():
    """
    Description:
        this function is define for take input as mobile number from user 
    Parameter:
       None
    Return:
       return_type (str) : mobile number
    """
    while True:
        try:
            mobile_no=input("enter mobile number: ")
            return mobile_no
            loggerfile.Logger("info","get mobile number successfully")
            break
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
    
