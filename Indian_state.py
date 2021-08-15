'''
@Author: Nikita Rai
@Date: 2021-08-13 8:00:30
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-15 7:00:30
@Title : State Census Data
'''
import csv,os
from dotenv import load_dotenv
from collections import defaultdict
load_dotenv()
class Indian_state_information(Exception):
    '''
    Description:
        Is is a class in which we can check some mismatch type of exception
    Argument:
        Exception is passes as a argument
    '''
    def mismatch_extension(filename):
        '''
        Description:
            mismatch_extension is a function which is use to check the extension type of the given file 
        Parameter:
            filename is parameter which is pass to check the extension of that paticular file.
        Return:
            Extension of the file is return
        '''
        extension =  (os.path.splitext(filename))
        extension_file = extension[1]
        try:
            if(extension_file != '.csv'):
                raise Exception
            else:
                print('Extension matched')
                return extension_file
        except Exception:
            print("type is not matched with CSV")
            return False

    def records(filename):
        '''
        Description:
            records is a function which is use find the number of records in the paticular file
        Parameter:
            filename is a paramater to which i have to find the records
        Return:
            number of records
            
        '''
        number_of_records = len(filename)
        return number_of_records

    def mismatch_header(header):
        '''
        Description:
            mismatch_header is a function which is use to check the header of the file.
        Parameter:
            header is pass as the argument
        Return:
            header matched
            
        '''
        try:
            if(header != ['State', 'Population', 'AreaInSqKm', 'DensityPerSqKm']):
                raise Exception("Header is not matched withCSV")
            else:
                return 'Header Matched'
        except Exception:
            return False

class Matcher(Indian_state_information):
    '''
    Description:
        Is is a class in which we can match the records of state data and census data
    Argument:
        state_census_analuser and Indian_State_information
    '''
    def count(self):
        '''
        Description:
            count is a function which is use to count the number of data inthe mentioned csv
        Parameter:
            self parameter is pass
        Return:
            total number of rows
            
        '''
        rowcount_census = -1
        for row in open("StateCensusData.csv"):
            rowcount_census+= 1
        print("Number of lines present:-", rowcount_census)
        return rowcount_census
    def matcher(record_var,counter_var):
        '''
        Description:
            matcher is function which is use to match the number of records and total count of the data 
        Parameter:
            total records and total records
        Return:
            none 
        '''
        try:
            if(counter_var == record_var):
                print('Records are matched with CSV')
            else:
                raise Exception
        except Exception:
            print('Records mismatched')
            return False
class state_census_analyser:
    def SCAiterator(filename):
        '''
        Description:
            SCAiterator is a function which is use to read the daya of census .csv and store the data into the list 
        Parameter:
             filename is a parameter
        Return:
            return the content and header of the list
            
        '''
        with open(os.getenv('SCD'), 'r') as csv_file:
            try:
                if csv_file.name != 'StateCensusData.csv':
                    raise Exception 
            except Exception:
                print("File name is incorrect")
            else:
                csv_read = csv.reader(csv_file, delimiter = ",")
                print(csv_read)
            data = []
            for line in csv_read:
                data.append(line)
            print(data)
            return data[1:], data[0]



if __name__ == '__main__' :
   
    content,header = state_census_analyser.SCAiterator(os.getenv('SCD'))
    record =  Indian_state_information.records(content)
    print(record)
    counter = Matcher.count(os.getenv('SCD'))

    typedata_SCD = Indian_state_information.mismatch_extension(os.getenv('SCD'))
    print(typedata_SCD)
    head_SCD = Indian_state_information.mismatch_header(header)
    print(head_SCD)
   

    

    
    