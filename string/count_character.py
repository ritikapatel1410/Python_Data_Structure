'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 13:40:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 13:40:38  
 @Title : count character of string 
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def count_character(user_defined_string):
    """
    Description:
        this function is define for count character of string 
    Parameter:
        user_defined_string (str) : string taken from user
    Return:
        count_char (dict) : dictionary which contain character : (character count)
    """
    count_char = {}
    for item in user_defined_string:
        if(item not in count_char.keys()):
            count_char[item]=user_defined_string.count(item)
    return count_char

def main():
    """
    Description:
        this main function for take string from user and call count_character function here
    Parameter:
        None
    Return:
        None
    """
    try:
        user_defined_string=input("===================================================================\nenter string: ")
        print("=================== count of char in string ==================\nlength of string {0} character count : {1}".format(user_defined_string,count_character(user_defined_string)))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","count character successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   