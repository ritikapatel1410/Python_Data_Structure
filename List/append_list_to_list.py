'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 23:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 23:00:38  
 @Title : append a list to the second list problem 
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def append_list(user_defind_list1,user_defind_list2):
    """
    Description:
        this function is define for append a list to the second list 
    Parameter:
        user_defind_list1 (list) : user defined list
        user_defind_list2 (list) : use defined list
    Return:
        user_defind_list3 (list) : append list
    """
    user_defind_list3=user_defind_list1+user_defind_list2
    return user_defind_list3

def main():
    """
    Description:
        this main function for create list from taking user input and call append_list function
    Parameter:
        None
    Return:
        None
    """
    user_defind_list1=[1,2,3]
    user_defind_list2=[1,2,7,8]
    try:
        print("=========================================================\n append of {0} and {1} is : {2}".format(user_defind_list1,user_defind_list2,append_list(user_defind_list1,user_defind_list2)))
        loggerfile.Logger("info","append list successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   