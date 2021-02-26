'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 2:55:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 2:55:38  
 @Title : find symmetric difference of sets
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def symmetric_difference_set(set1,set2):
    """
    Description:
        this function is define for find difference of two sets
    Parameter:
        set1 (set) : first set
        set2 (set) : second set
    Return:
        set3 (set) : symmetric difference of set1,set2
    """
    set3=set1.symmetric_difference(set2)
    return set3

def main():
    """
    Description:
        this main function for user defind sets and call symmetric_difference_set
    Parameter:
        None
    Return:
        None
    """
    set1={0,1,2,3}
    set2={0,1,2,7,8,9}
    try:
        print("=========================================================\n set1 {0} set2 {1} symmetric difference of sets {2}".format(set1,set2,symmetric_difference_set(set1,set2)))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","find difference successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} occured".format(error))
main()   