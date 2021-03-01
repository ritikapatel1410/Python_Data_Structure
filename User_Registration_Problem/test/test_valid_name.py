'''
 @Author: Ritika Patidar
 @Date: 2021-02-16 15:50:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-02-16 15:50:10  
 @Title : Test cases for valid name problem
'''
import unittest
import sys
sys.path.insert(0, 'main')
from validiate_name import valid_first_name,valid_last_name

class Test_valid_name(unittest.TestCase):
    """
    Description:
        This class define for test valid_first_name and valid_last_name method
    """

    def test_valid_first_name(self):
        """
        Description:
            This method define for test all case of valid_first_name method of validiate_name.py
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(valid_first_name("Ritika"),"valid name")
        self.assertNotEqual(valid_first_name("dipali"),"valid name")
        self.assertEqual(valid_first_name("dipali"),"invalid name")
        self.assertEqual(valid_first_name("1234"),"invalid name")
        self.assertEqual(valid_first_name("dipali@1"),"invalid name")
        self.assertIsNotNone(valid_first_name("dipali@1"))
        self.assertRaises(TypeError,valid_first_name)

    def test_valid_last_name(self):
        """
        Description:
            This method define for test all case of valid_last_name method of validiate_name.py
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(valid_last_name("Patidar"),"valid name")
        self.assertNotEqual(valid_last_name("patidar"),"valid name")
        self.assertEqual(valid_last_name("patidar"),"invalid name")
        self.assertEqual(valid_last_name("1234"),"invalid name")
        self.assertEqual(valid_last_name("patidar@1"),"invalid name")
        self.assertIsNotNone(valid_last_name("patidar@1"))
        self.assertRaises(TypeError,valid_last_name)

if __name__ == '__main__':
    unittest.main()