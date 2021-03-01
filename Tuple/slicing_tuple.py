'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 12:11:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 12:11:38  
 @Title : slice a tuple problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def slice_Tuple(given_tuple,start_point,end_point):
    """
    Description:
        this function is define for slice a tuple
    Parameter:
        Tuple (Tuple) : user defined tuple
    Return:
        reversed_tuple (Tuple) : reverse tuple of given tuple
    """
    if((start_point<(len(given_tuple)-1) and start_point>=0) and (end_point<=len(given_tuple) and end_point>=0)):
        return given_tuple[start_point:end_point]
    else:
        return "slice not possible"

def main():
    """
    Description:
        this main function for user defind tuple from taking input from user and call slice_Tuple
    Parameter:
        None
    Return:
        None
    """
    given_tuple=(1,2,3,4,5,6,7,8,9,10)
    try:
        while True:
            start_point=int(input("enter start point: "))
            end_point=int(input("enter start point: "))
            loggerfile.Logger("info","successfully take the input from the user")
            break
        possible_slice=slice_Tuple(given_tuple,start_point,end_point)
        if(possible_slice!="slice not possible"):
            print("========================== slicing of tuple here ==========================\nslicing of tuple : {0} from start point: {1} to last_point:{2} is : {3}".format(start_point,end_point,given_tuple,slice_Tuple(given_tuple,start_point,end_point)))
        else:
            print("======================================\nfom start point:{0} to end point:{1} of {2} {3}".format(start_point,end_point,given_tuple,slice_Tuple(given_tuple,start_point,end_point)))
        loggerfile.Logger("info","successfully reversed tuple")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

        
main()
