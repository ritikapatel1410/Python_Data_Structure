'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 23:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 23:30:38  
 @Title : split a list based on first character of word problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def string_split(word):
    """
    Description:
        this function is define for find common items from two lists
    Parameter:
        word (str) : string taken from user 
    Return:
       List (list) : list contain all the element after split word
    """
    List=word.split(word[0])
    return List
   

def main():
    """
    Description:
        this main function for string take from user and call string_split
    Parameter:
        None
    Return:
        None
    """
    try:
        word=input("===========================================================\nenter word: ")
        print("=========================================================\n word {0} after spliting by first character : {1}".format(word,string_split(word)))
        loggerfile.Logger("info","split word successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   