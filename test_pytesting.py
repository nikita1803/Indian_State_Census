'''
@Author: Nikita Rai
@Date: 2021-08-13 8:00:30
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-15 11:00:30
@Title : pytesting for state code new csv file
'''
import pytest
import os
import Indian_state

content_SCN, header_SCN = Indian_state.State_Code_new_Analyser.SCNiterator(os.getenv('SCN'))
record = Indian_state.Indian_state_information.records(content_SCN)

def test_Happy_test_case_SCN(): 
        '''
        Description:
            this is a function which is use to check the number of records are matched or not 
        Parameter:
            none
        Return:
            none
        '''
        assert record== 29
def test_sad_test_case_SCD(): 
        '''
        Description:
            this is a function which is use to check that exception is raised or not
        Parameter:
            none
        Return:
            none
        '''
        SAD = Indian_state.Matcher.matcher(record, 22)
        assert SAD == False




       
        