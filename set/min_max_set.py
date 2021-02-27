'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 3:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 3:30:38  
 @Title : find min and max of set problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def min_max_set(user_defined_set):
    """
    Description:
        this function is define for find min and max of set
    Parameter:
        user_defined_set (set) : user defined set
    Return:
        minimum (int) : min value of set
        maximum (int) : max value of set
    """
    minimum=min(user_defined_set)
    maximum=max(user_defined_set)
    return minimum,maximum

def main():
    """
    Description:
        this main function for user defind sets and call min_max_set
    Parameter:
        None
    Return:
        None
    """
    user_defined_set={0,1,2,3}
    try:
        minimum,maximum=min_max_set(user_defined_set)
        print("=========================================================\n set : {0} min value : {1} max value : {2}".format(user_defined_set,minimum,maximum))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","min max find successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} occured".format(error))
main()   