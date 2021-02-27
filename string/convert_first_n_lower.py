'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 19:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 19:40:38  
 @Title : convert lowercase first n characters in a string
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def lowercase_convert(user_defined_string,n):
    """
    Description:
        this function is define for convert lowercase first n characters in a string
    Parameter:
        user_defined_string (str) : user defined string
    Return:
        converted first n character into lower case
    """
    return user_defined_string[:n].lower()+user_defined_string[n:]

def main():
    """
    Description:
        this main function for user defind string and call lowercase_convert function
    Parameter:
        None
    Return:
        None
    """
    while True:
        try:
            user_defined_string=input("========================================\nenter string: ")
            n=int(input("enter the value of n: "))
            print("==============================================\nreversed string: {0}".format(lowercase_convert(user_defined_string,n)))
            loggerfile.Logger("info","successfully converted string into lowercase")
            print("=========================== program finish here =============================")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()   