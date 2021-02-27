'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 3:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 3:00:38  
 @Title : clear set problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def clear_set(user_defind_set):
    """
    Description:
        this function is define for clear set
    Parameter:
        user_defind_set (set) : user defined set
    Return:
        set (set) : empty set
    """
    user_defind_set.clear()
    return user_defind_set

def main():
    """
    Description:
        this main function for user defind sets and call clear_set
    Parameter:
        None
    Return:
        None
    """
    user_defind_set_old={0,1,2,3}
    user_defind_set={0,1,2,3}
    try:
        print("=========================================================\n user_defind_set before clear {0} and after clear {1}".format(user_defind_set_old,clear_set(user_defind_set)))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","clear successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} occured".format(error))
main()   