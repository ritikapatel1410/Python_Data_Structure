'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 3:18:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 3:18:38  
 @Title : remove key from dictionary
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def remove_key(key):
    """
    Description:
        this function is define for remove key from the dictionary
    Parameter:
        key (int) : which you want to remove
    Return:
        Dict (dict) : after removing key
    """
    Dict={1:"one", 2:"two",3:"three",4:"four"}
    Dict.pop(key)
    return Dict

def main():
    """
    Description:
        this main function for take input from the user and call remove_key function
    Parameter:
        None
    Return:
        None
    """

    try:
        key=int(input("=============================\nenter the key: "))
        old_Dict={1:"one", 2:"two",3:"three",4:"four"}
        print("=====================================================\ndictionary before {0} and after {1}".format(old_Dict,remove_key(key)))
        loggerfile.Logger("info","remove key successfully")
    except ValueError as error:
        loggerfile.Logger("error","{0} occured".format(error))
    except KeyError as error:
        loggerfile.Logger("error","{0} occured".format(error))

main()   
