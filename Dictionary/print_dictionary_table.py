'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 3:50:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 3:50:38  
 @Title : print dictionary in table form problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def print_table(dictionary):
    """
    Description:
        this function is define for print dictionary in table form
    Parameter:
        dictionary (dict) : user defined dictionary
    Return:
        "print table successfully"
    """
    print ("  {:<10} {:<10} ".format('KEY', 'VALUE')) 
    for key, value in dictionary.items():
        print ("  {:<10} {:<10}".format(key,value)) 


    return "print table successfully"

def main():
    """
    Description:
        this main function for take input from the user and call print_table function
    Parameter:
        None
    Return:
        None
    """
    dictionary = {1:"one", 2:"two",3:"three",4:"four"} 
    print("=============================== print dictionary in table form =====================================")
    print_table(dictionary)
    loggerfile.Logger("info","print dictionary into table form successfully")
    print("====================================================================================================")
main()   
