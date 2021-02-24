'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 19:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 19:15:38  
 @Title : calendar problem
'''
#import module
import re
import calendar
while True:
    #valid year 1900-2099
    y = int(input("Input the year : "))
    m = int(input("Input the month : "))
    if(re.match(r'^[1-12]*$',str(m)) and re.match(r'^(19|20)\d{2}$',str(y))):
        break
print(calendar.month(y, m))