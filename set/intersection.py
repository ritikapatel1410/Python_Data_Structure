'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 23:55:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 23:55:38  
 @Title : discard element to the set problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
sys.path.insert(0, os.path.abspath('custom_exception'))
import custom_exception_file

def intersection_set(set1,set2):
    """
    Description:
        this function is define for find intersection of two sets
    Parameter:
        set1 (set) : first set
        set2 (set) : second set
    Return:
        set3 (set) : intersection of set1,set2
    """
    set3=set1.intersection(set2)
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
    set1={0,1,2,3,4,5,6}
    set2={0,1,2,3,7,8,9}
    try:
        intersection_set_return=intersection_set(set1,set2)
        if(intersection_set_return==set()):
            raise custom_exception_file.IntesectionNotPossible
        else:
            print("=========================== intersection of sets =========================\n set1 {0} set2 {1} intersection of sets {2}".format(set1,set2,intersection_set(set1,set2)))
            print("=========================== program finish here =============================")
            loggerfile.Logger("info","find intersection successfully")
    except custom_exception_file.IntesectionNotPossible:
        loggerfile.Logger("error","intersection not possible")
main()   