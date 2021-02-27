'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 22:45:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 22:45:38  
 @Title : get the difference between the two lists 
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def difference_list(user_defined_list1,user_defined_list2):
    """
    Description:
        this function is define for get the difference between the two lists 
    Parameter:
        user_defined_list1 (list) : user defined list
        user_defined_list2 (list) : use defined list
    Return:
        difference_list (list) : difference of user_defined_list1 and user_defined_list2
    """
    difference_list=[set(user_defined_list1).symmetric_difference(set(user_defined_list2))]
    return difference_list

def main():
    """
    Description:
        this main function for create list from taking user input and call difference_list function
    Parameter:
        None
    Return:
        None
    """
    user_defined_list1=[1,2,3]
    user_defined_list2=[1,2,7,8]
    try:
        print("=========================================================\n difference of {0} and {1} is : {2}".format(user_defined_list1,user_defined_list2,difference_list(user_defined_list1,user_defined_list2)))
        loggerfile.Logger("info","find difference of list successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   