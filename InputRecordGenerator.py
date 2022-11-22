'''
Input Record Generator
This class helps us to generate record file with using random and string library.
You can configure the random limitation from Config/InputRecordConstant.py
'''
import string
import random
import Config.ByteSizeConstant as BYTE_CONSTANT
import Config.InputRecordConstant as RECORD_CONSTANT
import pickle
import sys, os
import logging


'''
You can easily generate new records from this method
If you would like to change limitation of random method parameters, you can edit from Config/InputRecordConstant.py 
''' 
def RecordListGenerator():
    #numberOfRecords : Picking random value for deciding how many records will be generated in record list.
    numberOfRecords = random.randrange(RECORD_CONSTANT.NUMBER_RECORD_START_LIMIT, RECORD_CONSTANT.NUMBER_RECORD_END_LIMIT)
    recordCounter = 0
    recordList = []
    print("Selected number of records : " , numberOfRecords)
    print("Record Generation Process is Started")
    while recordCounter < numberOfRecords:
        #selectedRecordLength : Picking byte size of record
        selectedRecordLength = random.randrange(RECORD_CONSTANT.RECORD_BYTE_SIZE_START_LIMIT, RECORD_CONSTANT.RECORD_BYTE_SIZE_END_LIMIT)
        #generatedRecord : Generating a new string record with using "string" library.
        generatedRecord = ''.join(random.choices(string.ascii_letters, k=selectedRecordLength))
        recordList.append(generatedRecord)
        recordCounter += 1
    
    return recordList

