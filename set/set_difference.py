'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 1:55:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 1:55:38  
 @Title : find difference of sets
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def difference_set(user_defined_set1,user_defined_set2):
    """
    Description:
        this function is define for find difference of two sets
    Parameter:
        user_defined_set1 (set) : first set
        user_defined_set2 (set) : second set
    Return:
        set3 (set) : difference of user_defined_set1,user_defined_set2
    """
    set3=user_defined_set1.difference(user_defined_set2)
    return set3

def main():
    """
    Description:
        this main function for user defind sets and call difference_set
    Parameter:
        None
    Return:
        None
    """
    user_defined_set1={0,1,2,3}
    user_defined_set2={0,1,2,7,8,9}
    try:
        print("======================================================\n user_defined_set1 {0} user_defined_set2 {1} difference of sets {2}".format(user_defined_set1,user_defined_set2,difference_set(user_defined_set1,user_defined_set2)))
        print("=====================================================\n user_defined_set2 {1} user_defined_set1 {0} difference of sets {2}".format(user_defined_set1,user_defined_set2,difference_set(user_defined_set2,user_defined_set1)))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","find difference successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} occured".format(error))
main()   