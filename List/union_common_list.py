'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 23:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 23:30:38  
 @Title : find common items from two lists problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def common_element(user_define_list1,user_define_list2):
    """
    Description:
        this function is define for find common items from two lists
    Parameter:
        user_define_list1 (list) : user defined list
        user_define_list2 (list) : use defined list
    Return:
       union_of_list (list) : list of common element
    """
    union_of_list=list(set(user_define_list1).intersection(set(user_define_list2)))
    return union_of_list
   

def main():
    """
    Description:
        this main function for create list from taking user input and call common_element
    Parameter:
        None
    Return:
        None
    """
    user_define_list1=[1,2,3,4,5]
    user_define_list2=[1,2,7,8,3,6]
    try:
        print("=========================================================\n user_define_list1 {0} and user_define_list2 {1} common element are : {2}".format(user_define_list1,user_define_list2,common_element(user_define_list1,user_define_list2)))
        loggerfile.Logger("info","find common element successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   