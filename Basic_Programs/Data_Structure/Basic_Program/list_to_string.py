'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 22:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 22:15:38  
 @Title : convert list into string
 '''
def list_string(list_element):
    """
    Description:
        this function define convert list into string
    Parameter:
       list_element (list) : input list
    Return:
        convert string
    """
    for element in range(len(list_element)):
        if(type(list_element[element])!=str):
            list_element[element]=str(list_element[element])
    return "".join(list_element)

list_element=[1,2,3,4,5,6,7,8]
print("{0} --> {1}".format(list_element,list_string(list_element)))