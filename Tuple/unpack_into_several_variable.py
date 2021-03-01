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

def unpack_tuple(user_defined_tuple):
    """
    Description:
        this function is define for unpack a tuple in several variables
    Parameter:
        user_defined_tuple (list) : user defined tuple
    Return:
        unpack_tuple (tuple) : unpack_tuple of given user_defined_tuple
    """
    (name,lastname,age,degree)=user_defined_tuple
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
    user_defined_tuple=("Vijay", "patidar", 28, "B.tech")
    try:
        print("====================================================\nuser_defined_tuple : {0} after unpack see below".format(user_defined_tuple))
        unpack_tuple(user_defined_tuple)
        loggerfile.Logger("info","successfully create unpack tuple successfully")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()