'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 19:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 19:15:38  
 @Title : convert sequence into tuple and list
'''
import re

def conv_tuple_list():
    """
    Description:
        this function define for convert sequence into tuple and list
    Parameter:
        None
    Return:
        None
    """
    while True:
        sequence=input("enter sequence: ")
        if(re.match(r'^[0-9 0-9]*$',sequence)):
            break
    list_output=[]
    for number in sequence.split(" "):
        list_output.append(number)
    return tuple(list_output),list_output
    
tuple_sequence,list_sequence=conv_tuple_list()
print("tuple sequence : {0} \n list sequence : {1}".format(tuple_sequence,list_sequence))

