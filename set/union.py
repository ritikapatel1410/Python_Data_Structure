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

def union_set(set1,set2):
    """
    Description:
        this function is define for find union of two sets
    Parameter:
        set1 (set) : first set
        set2 (set) : second set
    Return:
        set3 (set) : union of set1,set2
    """
    set3=set1.union(set2)
    return set3

def main():
    """
    Description:
        this main function for user defind sets and call intersection_set function
    Parameter:
        None
    Return:
        None
    """
    set1={0,1,2,3}
    set2={0,1,2,7,8,9}

    print("=========================== union of sets =========================\n set1 {0} set2 {1} union of sets {2}".format(set1,set2,union_set(set1,set2)))
    print("=========================== program finish here =============================")
    loggerfile.Logger("info","find union successfully")

main()   