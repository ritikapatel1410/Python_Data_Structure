'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 10:51:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 10:51:38  
 @Title : unpack a tuple in several variables problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def unpack_tuple(Tuple):
    """
    Description:
        this function is define for unpack a tuple in several variables
    Parameter:
        Tuple (list) : user defined tuple
    Return:
        unpack_tuple (tuple) : unpack_tuple of given Tuple
    """
    (name,lastname,age,degree)=Tuple
    print("======================== Unpack Tuple Here ========================\nname : {0}\nlastname:{1}\nlastname:{2}\ndegree:{3}".format(name,lastname,lastname,degree))
    return True

def main():
    """
    Description:
        this main function for user defind tuple from taking input from user and call unpack_tuple
    Parameter:
        None
    Return:
        None
    """
    Tuple=("Vijay", "patidar", 28, "B.tech")
    try:
        print("====================================================\nTuple : {0} after unpack is : {1}".format(Tuple,unpack_tuple(Tuple)))
        loggerfile.Logger("info","successfully create unpack tuple successfully")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()