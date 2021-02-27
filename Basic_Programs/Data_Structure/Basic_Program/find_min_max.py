'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 14:47:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 14:47:38  
 @Title : find min or max value in sequence problem
'''
def min_max_function(sequence):
    """
    Description:
        find min max value in sequence
    Parameter:
        sequence (list) : user defind list for check min and max
    Return:
        min_val (int) : min value of sequence
        max_val (int) : max value of sequence
    """
    min_val=sequence[0]
    max_val=sequence[0]
    for value in sequence[1:]:
        if(value>max_val):
            max_val=value
        if(value<min_val):
            min_val=value
    return max_val,min_val

sequence=[1,2,7,6,0,1,-1,3]
print("========================\n max value : {0}\n min value :{1}".format(min_max_function(sequence)[0],min_max_function(sequence)[1]))

