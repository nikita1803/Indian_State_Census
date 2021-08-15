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
content_sc, header_sc = Indian_state.stateCode_Analyser.SCAiterator(os.getenv('SC'))
record_sc = Indian_state.Indian_state_information.records(content_sc)
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

    def test_sad_test_case_SCD(self):  
        '''
        Description:
            this is a function which is use to check that exception is raised or not
        Parameter:
            self parameter is pass
        Return:
            none
        '''
        with self.assertRaises(Exception):
            SAD=Indian_state.Matcher.matcher(record,22)
            self.assertTrue(SAD)

    def test_type_error_SCD(self):
        '''
        Description:
            this is a function which is use to check the type of the file 
        Parameter:
            self parameter is pass
        Return:
            none
        '''
        typedata = Indian_state.Indian_state_information.mismatch_extension(os.getenv('SCD'))
        with self.assertRaises(Exception):
            self.assertEqual(typedata, '.pdf')

    def test_header_check_SCD(self):
        '''
        Description:
            this is a function which is use to check the heder for census file 
        Parameter:
            self parameter is pass
        Return:
            none
        '''
        head = [Indian_state.Indian_state_information.mismatch_header(header)]
        with self.assertRaises(Exception):
            self.assertEqual(head, 'Header Mathed')

    def test_Happy_test_case_SC(self): 
        '''
        Description:
            this is a function which is use to check the number of records 
        Parameter:
            self parameter is pass
        Return:
            none
        '''
        self.assertEqual(record_sc, 37)

    def test_sad_test_case_SC(self):
        '''
        Description:
            this is a function which is use to check that the exception is raised or not
        Parameter:
            self parameter is pass
        Return:
            none
        '''
        SAD1=Indian_state.Matcher.matcher(record_sc, 39)
        with self.assertRaises(Exception):
            self.assertTrue(SAD1)

    def test_type_error_SC(self):
        '''
        Description:
            this is a function which is use to check the type of the file
        Parameter:
            self parameter is pass
        Return:
            none
        '''
        typedata = Indian_state.Indian_state_information.mismatch_extension(os.getenv('SC'))
        with self.assertRaises(Exception):
            self.assertEqual(typedata, '.pdf')

    def test_header_check_SC(self):
        '''
        Description:
            this is a function which is use to check the heder of the data
        Parameter:
            self parameter is pass
        Return:
            none
        '''
        head = Indian_state.stateCode_Analyser.mismatch_header(header_sc)
        with self.assertRaises(Exception):
            self.assertEqual(head, ' Matched')
                    
if __name__ == '__main__': 
    unittest.main()
