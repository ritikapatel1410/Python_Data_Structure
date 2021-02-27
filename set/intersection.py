'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 23:55:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 23:55:38  
 @Title : find intersection of two set problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
sys.path.insert(0, os.path.abspath('custom_exception'))
import custom_exception_file

def intersection_set(user_defind_set1,user_defind_set2):
    """
    Description:
        this function is define for find intersection of two sets
    Parameter:
        user_defind_set1 (set) : first set
        user_defind_set2 (set) : second set
    Return:
        set_intersection (set) : intersection of user_defind_set1,user_defind_set2
    """
    set_intersection=user_defind_set1.intersection(user_defind_set2)
    return set_intersection

def main():
    """
    Description:
        this main function for user defind sets and call intersection_set function
    Parameter:
        None
    Return:
        None
    """
    user_defind_set1={0,1,2,3,4,5,6}
    user_defind_set2={0,1,2,3,7,8,9}
    try:
        intersection_set_return=intersection_set(user_defind_set1,user_defind_set2)
        if(intersection_set_return==set()):
            raise custom_exception_file.IntesectionNotPossible
        else:
            print("=========================== intersection of sets =========================\n user_defind_set1 {0} user_defind_set2 {1} intersection of sets {2}".format(user_defind_set1,user_defind_set2,intersection_set(user_defind_set1,user_defind_set2)))
            print("=========================== program finish here =============================")
            loggerfile.Logger("info","find intersection successfully")
    except custom_exception_file.IntesectionNotPossible:
        loggerfile.Logger("error","intersection not possible")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))
main()   