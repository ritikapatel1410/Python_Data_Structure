'''
 @Author: Ritika Patidar
 @Date: 2021-02-28 23:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-28 23:00:38  
 @Title : validiate password of user regestration problem 
'''
import re
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def valid_password(password):
    """
    Description:
        this function is define for validiate password of user 
    Parameter:
       password (str) : password of user
    Return:
       if password is valid then return valid password else return invalid password
    """
    while True:   
        if ((len(password)!=8) or (not re.search("[A-Z]", password)) or (not re.search("[0-9]", password)) or (not len(re.findall("[\W_]", password))==1)): 
            flag = -1
            break
        else: 
            flag = 0
            return "Valid Password"
            break
    
    if flag ==-1: 
        return "invalid Password"

def input_password():
    """
    Description:
        this function is define for take input as password from user 
    Parameter:
       None
    Return:
       return_type (str) : password
    """
    while True:
        try:
            password=input("enter password: ")
            return password
            loggerfile.Logger("info","get password successfully")
            break
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
  
