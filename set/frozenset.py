'''
 @Author: Ritika Patidar
 @Date: 2021-02-26 3:30:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-26 3:30:38  
 @Title : use of frozensets problem
'''
import sys
import os
sys.path.insert(0, os.path.abspath('LogFile'))
import loggerfile

def frozen_operation(frozen_set1,frozen_set2):
    """
    Description:
        this function is define for operation of frozensets
    Parameter:
        frozen_set1 (fozensets) : user defined frozensets
        frozen_set2 (fozensets) : user defined frozensets
    Return:
       frozensets operation       
    """
    return frozen_set1.isdisjoint(frozen_set2),frozen_set1.symmetric_difference(frozen_set2),frozen_set1|frozen_set2

def main():
    """
    Description:
        this main function for user defind frozensets and call frozen_operation
    Parameter:
        None
    Return:
        None
    """
    frozen_set1 = frozenset([1, 2, 3, 4, 5])
    frozen_set2 = frozenset([3, 4, 5, 6, 7])
    try:
        print("================================== frozensets operation ============================================")
        adjoint_frozen,difference_frozen,combine_set=frozen_operation(frozen_set1,frozen_set2)
        print("disjoint of frozen set : {0} \nsymmetric difference of frozen set : {1} \ncomine_set : {2}".format(adjoint_frozen,difference_frozen,combine_set))
        print("=========================== program finish here =============================")
        loggerfile.Logger("info","successfully performed frozen sets operation")
    except Exception as error:
        loggerfile.Logger("error","{0} occured".format(error))
main()   