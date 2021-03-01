'''
 @Author: Ritika Patidar
 @Date: 2021-03-01 16:28:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-03-01 16:28:10  
 @Title : Test cases for validiate password problem
'''
import unittest
import sys
sys.path.insert(0, 'main')
from validiate_password import valid_password

class Test_validiate_password(unittest.TestCase):
    """
    Description:
        This class define for test all case of valid_password method
    """

    def test_valid_password(self):
        """
        Description:
            This method define for test all case of valid_password method of valid_mobile_number.py
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(valid_password("A12@11ab"),"Valid Password")
        self.assertNotEqual(valid_password("A1@22"),"Valid Password")
        self.assertNotEqual(valid_password("9a12A121"),"Valid Password")
        self.assertEqual(valid_password("a12#11A1"),"Valid Password")
        self.assertEqual(valid_password("a123A#111111"),"invalid Password")
        self.assertIsNotNone(valid_password("A12@11ab"))
        self.assertRaises(TypeError,valid_password)

if __name__ == '__main__':
    unittest.main()