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

def clear_set(set1):
    """
    Description:
        this function is define for clear set
    Parameter:
        set1 (set) : user defined set
    Return:
        set (set) : empty set
    """
    set1.clear()
    return set1

def main():
    """
    Description:
        this main function for user defind sets and call clear_set
    Parameter:
        None
    Return:
        None
    """
    set1_old={0,1,2,3}
    set1={0,1,2,3}
    try:
        print("=========================================================\n set1 before clear {0} and after clear {1}".format(set1_old,clear_set(set1)))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","clear successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} occured".format(error))
main()   