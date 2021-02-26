'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 2:18:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 2:18:38  
 @Title : generate n:n^2 format dictionary
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def n_n2_dictionary(no_of_items):
    """
    Description:
        this function is define generate a dictionary into n:n^2 pattern
    Parameter:
        no_of_input (dict) : size of dictionary given by user
    Return:
        Dict (dict) : formed dictionary in n:n^2 format
    """
    Dict={}
    for key in range(1,no_of_items+1):
        Dict[key]=key*key
    return Dict

def main():
    """
    Description:
        this main function for take input from the user and call n_n2_dictionary function
    Parameter:
        None
    Return:
        None
    """

    try:
        size_of_dict=int(input("enter the size of dictionary: "))
        print("=====================================================\ndictionary : {0}".format(n_n2_dictionary(size_of_dict)))
        loggerfile.Logger("info","successfully dictionary created")
    except ValueError as error:
        loggerfile.Logger("error","{0} occured".format(error))
    except Exception:
        loggerfile.Logger("error","{0} occured".format(error))

main()   
