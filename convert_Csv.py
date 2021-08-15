'''
@Author: Nikita Rai
@Date: 2021-08-13 8:00:30
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-15 11:00:30
@Title : convert csv to json

'''
import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    '''
        Description:
            This function is use to convert the csv file to json 
        Parameter:
            csv file path and json file path passes as a argument
        Return:
            none   
        '''
    jsonArray = []
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 
        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'StateCode_new.csv'
jsonFilePath = r'StateCode.json'
csv_to_json(csvFilePath, jsonFilePath)