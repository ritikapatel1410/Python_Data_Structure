'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 19:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 19:40:38  
 @Title : count substring in a sstring problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def count_substring(user_defined_string,sub_string):
    """
    Description:
        this function is define count substring in a sstring problem
    Parameter:
        user_defined_string (str) : user defined string
        sub_string (str) : sub string of user_defined_string
    Return:
        count (int) : no of sub_string into user_defined_string
    """
    count=user_defined_string.count(sub_string)
    return count
def main():
    """
    Description:
        this main function for user defind string and call count_substring function
    Parameter:
        None
    Return:
        None
    """
    try:
        user_defined_string=input("========================================\nenter string: ")
        sub_string=input("========================================\nenter sub string: ")
        print("==============================================\ncount of sub string: {0} ==== into string :{1} ====is {2}".format(sub_string,user_defined_string,count_substring(user_defined_string,sub_string)))
        loggerfile.Logger("info","successfully count sub string successfully")
        print("=========================== program finish here =============================")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   