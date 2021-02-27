'''
 @Author: Ritika Patidar
 @Date: 2021-02-17 00;52:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-18 00:52:38  
 @Title : concatenate dictionary problem
'''

import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def concatenate_dictionary(dic1,dic2,dic3):
    """
    Description:
        this function is define for concatenate dictionaryDictionary/LogFile
    Parameter:
        dic1 (dict) : user defind dictionary
        dic2 (dict) : user defind dictionary
        dic3 (dict) : user defind dictionary
    Return:
        concatenate dictionary
    """
    dictionary={}
    dictionary.update(dic1)
    dictionary.update(dic2)
    dictionary.update(dic3)
    return dictionary

def main():
    """
    Description:
        this main function defined for call concatenate_dictionary function and defined dictionary dict1,dict2,dict3 
    Parameter:
        None
    Return:
        None
    """
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    print("============================ Occurance of element is here =========================================")
    print("dictionary {0} {1} {2} after concatenate dictionary : {3}".format(dic1,dic2,dic3,concatenate_dictionary(dic1,dic2,dic3)))
    loggerfile.Logger("info","successfully concatenate dictionary")

main()   