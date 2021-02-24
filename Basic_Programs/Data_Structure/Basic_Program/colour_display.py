'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 20:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 20:15:38  
 @Title : colour display problem
'''

def colour_display(user_input):
    """
    Description:
        this function define for colour display
    Parameter:
        None
    Return:
        None
    """
    return user_input[0],user_input[len(user_input)-1]
color_list = ["Red","Green","White" ,"Black"]
first_colour,last_colour=colour_display(color_list)
print("first colour : {0} \nlast colour : {1}".format(first_colour,last_colour))