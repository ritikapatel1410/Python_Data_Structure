'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 11:55:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 11:55:38  
 @Title : find union of sets
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def union_set(user_defined_set1,user_defined_set2):
    """
    Description:
        this function is define for find union of two sets
    Parameter:
        user_defined_set1 (set) : first set
        user_defined_set2 (set) : second set
    Return:
        union_set (set) : union of user_defined_set1,user_defined_set2
    """
    union_set=user_defined_set1.union(user_defined_set2)
    return union_set

def main():
    """
    Description:
        this main function for user defind sets and call intersection_set function
    Parameter:
        None
    Return:
        None
    """
    user_defined_set1={0,1,2,3}
    user_defined_set2={0,1,2,7,8,9}

    print("=========================== union of sets =========================\n user_defined_set1 {0} user_defined_set2 {1} union of sets {2}".format(user_defined_set1,user_defined_set2,union_set(user_defined_set1,user_defined_set2)))
    print("=========================== program finish here =============================")
    loggerfile.Logger("info","find union successfully")

main()   