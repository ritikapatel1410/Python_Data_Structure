'''
 @Author: Ritika Patidar
 @Date: 2021-02-24 10:09:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-24 10:09:38  
 @Title :  implement anonymous function problem
'''

num_list = [45, 55, 60, 37, 100, 105, 220]
print("==============================================================================")
# use anonymous function to filter
new_list = list(filter(lambda x: (x%15 == 0) , num_list))
print("numbers divisible by fifteen : {0}".format(new_list))