'''
 @Author: Ritika Patidar
 @Date: 2021-02-23 22:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-23 22:15:38  
 @Title : find builtin module problem
'''
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print("==============================================================================================================")
print(textwrap.fill(module_name, width=100))