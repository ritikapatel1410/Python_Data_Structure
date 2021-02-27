'''
 @Author: Ritika Patidar
 @Date: 2021-02-27 17:00:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-27 17:40:38  
 @Title : display formatted text (width=50) problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile
import textwrap

def formed_text(given_text):
    """
    Description:
        this function is define display formatted text (width=50) problem
    Parameter:
        given_text (str) : user defined text
    Return:
        formatted text with width=50
    """
    return textwrap.fill(given_text,width=50)

def main():
    """
    Description:
        this main function for user defind textfrom user and call formated_text function
    Parameter:
        None
    Return:
        None
    """
    given_text="Python is a widely used high-level, general-purpose, interpreted,dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java."
    try:
        print("==============================================\ntext befor formatted\n==========================================================================\n{0}\n===================================================== \n after formatted\n===========================================================================\n{1}".format(given_text,formed_text(given_text)))
        loggerfile.Logger("info","formatted text successfully")
        print("=========================== program finish here =============================")
    except ValueError as error:
        loggerfile.Logger("error","{0} error occured".format(error))
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()   