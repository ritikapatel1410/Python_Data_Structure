'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 19:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 19:15:38  
 @Title : check uncommon element
'''
def uncommon_colour(color_list1,color_list2):
    """
    Description:
        this function define for check uncommon color into two set
    Parameter:
        color_list1 (set) : input 
        color_list2 (set) : input
    Return:
        uncommon color of set
    """
    color=[color for color in color_list1 if(color not in color_list2)]
    return set(color)

#input
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
#call function
print(uncommon_colour(color_list_1,color_list_2))