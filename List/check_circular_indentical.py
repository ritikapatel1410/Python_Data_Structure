'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 23:10:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 23:10:38  
 @Title : check whether two lists are circularly identical problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def circularly_identical(user_defind_list1,user_defind_list2):
    """
    Description:
        this function is define for check whether two lists are circularly identical 
    Parameter:
        user_defind_list1 (list) : user defined list
        user_defind_list2 (list) : use defined list
    Return:
       True : if circularly identical
       false : if not circularly identical
    """
    return (' '.join(map(str, user_defind_list1)) in ' '.join(map(str, user_defind_list2 * 2))) 
   

def main():
    """
    Description:
        this main function for create list from taking user input and call circularly_identical function
    Parameter:
        None
    Return:
        None
    """
    user_defind_list1=[8,1,2,7]
    user_defind_list2=[1,2,7,8]
    try:
        print("=========================================================\n user_defind_list1 {0} and user_defind_list2 {1} are circularly identical ? {2}".format(user_defind_list1,user_defind_list2,circularly_identical(user_defind_list1,user_defind_list2)))
        loggerfile.Logger("info","check circularly identical successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   