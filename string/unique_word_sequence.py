'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 14:20:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 14:20:38  
 @Title : print unique word sequence of given sequence
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def sorted_sequence_word(word_sequence):
    """
    Description:
        this function is define for print unique word sequence of given sequence
    Parameter:
        word_sequence (str) : word sequence taken from the user
    Return:
        sorted unique sequence of word
    """
    list_word=word_sequence.split(",")
    list_word_sorted=list(set(list_word))
    list_word_sorted.sort()
    return ",".join(list_word_sorted)

def main():
    """
    Description:
        this main function for take string from user and call maximum_word function
    Parameter:
        None
    Return:
        None
    """
    try:
        word_sequence=input("===============================================\nenter word by comma seprated: ")
        print("======================================\ngiven sequence : {0} \nunique sorted sequence is: {1}".format(word_sequence,sorted_sequence_word(word_sequence)))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","successfull get unique sorted sequence")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   