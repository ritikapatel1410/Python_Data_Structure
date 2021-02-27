'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 21:44:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 21:44:38  
 @Title : check numbe into sequence
'''
def check(sequence,value):
    """
    Description: 
        cheack value in sequence or not
    Parameter:
        sequence (list) : group of element
    Return:
        True (boolean): if value in sequence
        False (boolean): if value not in sequence
    """
    if(value in sequence):
        return True
    else:
        return False

test_case=[[3,[1, 5, 8, 3]],[-1,[1, 5, 8, 3]]]
for test in test_case:
    print("{0} -> {1} : {2}".format(test[0],test[1],check(test[1],test[0])))
