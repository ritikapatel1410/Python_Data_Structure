'''
 @Author: Ritika Patidar
 @Date: 2021-02-25 4:50:38
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-25 4:50:38  
 @Title : count success True in dictionary
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile 

def check_dict(dictionary):
    """
    Description:
        this function is define for count success == true in dictionary 
    Parameter:
        dictionary (dict) : user defined dictionary
    Return:
        count (int) : count success=True condition
    """
    count=0
    for item in dictionary:
        try:
            if(item["success"]==True):
                count+=1
        except KeyError as error:
            loggerfile.Logger("error","{0} error occured".format(error))
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

    return count

def main():
    """
    Description:
        this main function for defind dictionary from the user and call check_dict
    Parameter:
        None
    Return:
        None
    """
    dictionary = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    print("=============================== success == True count here =====================\n success == True count : {0}".format(check_dict(dictionary)))
    loggerfile.Logger("info","count success==true successfully")
    print("====================================================================================================")
main()   
