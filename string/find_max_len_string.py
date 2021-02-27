'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 14:10:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 14:10:38  
 @Title : find maximum length word in list
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def maximum_word(word_list):
    """
    Description:
        this function is define for find maximum length word in list
    Parameter:
        word_list (list) : user defined list of words
    Return:
        return a word which have maximum length
    """
    length_word_list=[]
    for word in word_list:
        length_word_list.append((len(word),word))
    length_word_list.sort()
    return length_word_list[(len(length_word_list)-1)][1]
def main():
    """
    Description:
        this main function for take string from user and call extend_string function
    Parameter:
        None
    Return:
        None
    """
    word_list=[]
    while True:
        try:
            size_of_list=int(input("===============================================\nenter size of list: "))
            for item in range(size_of_list):
                word=input("enter element {0} of list: ".format(item))
                word_list.append(word)
            maximum_word(word_list)
            print("======================================\nloggest word in list {0} is {1}".format(word_list,maximum_word(word_list)))
            print("=========================== program finish here =============================")
            loggerfile.Logger("info","find loggest word of list successfully")
            break
        except ValueError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

main()   