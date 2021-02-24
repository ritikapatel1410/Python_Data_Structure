'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 22:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 22:15:38  
 @Title : calculate execution time of method problem
'''
import time
def execute_time(count):
    start_time = time.time()
    while count!=0:
        count-=1
    end_time = time.time()
    return end_time-start_time
count=10
print("excetion time of method : {0} sec".format(execute_time(count)))