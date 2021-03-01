'''
 @Author: Ritika Patidar
 @Date: 2021-03-01 16:28:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-03-01 16:28:10  
 @Title : Test cases for valid mobile number problem
'''
import unittest
import sys
sys.path.insert(0, 'main')
from validiate_mobile_number import valid_mobile_number

class Test_validiate_mobile_number(unittest.TestCase):
    """
    Description:
        This class define for test all case of valid_mobile_number method
    """

    def test_valid_mobile_number(self):
        """
        Description:
            This method define for test all case of valid_mobile_number method of valid_mobile_number.py
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(valid_mobile_number("91 9893123425"),"valid mobile number")
        self.assertNotEqual(valid_mobile_number("9893123425"),"valid mobile number")
        self.assertNotEqual(valid_mobile_number("91 6893123425"),"valid mobile number")
        self.assertEqual(valid_mobile_number("91 8193123425"),"valid mobile number")
        self.assertEqual(valid_mobile_number("91 0893123425"),"invalid mobile number")
        self.assertIsNotNone(valid_mobile_number("91 9893123425"))
        self.assertRaises(TypeError,valid_mobile_number)

if __name__ == '__main__':
    unittest.main()