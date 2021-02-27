'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 19:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 19:15:38  
 @Title : list all files in a directory problem
'''
#import module
from os import listdir
from os.path import isfile, join
print("================================= List of Files Here ===========================================================================")
files_list = [ f for f in listdir('/home/patidar')if isfile(join('/home/patidar', f))]
print(files_list)