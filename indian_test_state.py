'''
@Author: Nikita Rai
@Date: 2021-08-13 8:00:30
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-15 10:00:30
@Title : unit testing on state census data and state code data 

'''
import unittest
import os
import Indian_state

content, header = Indian_state.state_census_analyser.SCAiterator(os.getenv('SCD'))
record = Indian_state.Indian_state_information.records(content)
class Test_State_Census_Data(unittest.TestCase , Exception):
    '''
    Description:
        This is class contaning 4 test cases to check whether it passes the condition or not 
    Argument:
        Exception is passes as a argument
    '''
    def test_Happy_test_case_SCD(self): 
        '''
        Description:
            this is a function which is use to check the number of records are matched or not 
        Parameter:
            self parameter is pass
        Return:
            none
        '''
        self.assertEqual(record, 29)

if __name__ == '__main__': 
    unittest.main()
