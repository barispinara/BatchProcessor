'''
TestRunner
This file constaint test method for testing BatchProcesser class
You can edit generated record file parameters from "Config/InputRecordConstant.py"
'''
import sys
sys.path.append("../")
from BatchProcessor import BatchProcessor
import pickle
import logging
import Config.ByteSizeConstant as BYTE_CONSTANT
from InputRecordGenerator import RecordListGenerator


def Test1():
    '''
    Generating record list and testing batching processor
    The system is tested with these Constants
    RECORD_BYTE_SIZE_START_LIMIT = 10KB
    RECORD_BYTE_SIZE_END_LIMIT = 1.1MB
    NUMBER_RECORD_START_LIMIT = 2000
    NUMBER_RECORD_END_LIMIT = 3000
    '''
    recordList = RecordListGenerator()
    
    calledBatchProcesser = BatchProcessor(recordList)
    generatedBatchList = calledBatchProcesser.BatchProgressing()
    #Testing generated batch list about given limitation
    for batchIndex , batch in enumerate (generatedBatchList):
        batchByteSize = 0
        '''
        If the batch size is higher than 500, test will fail
        '''
        if len(batch) > 500:
            logging.warning("Test 1 Failed , Batch Record Size bigger than 500 [Batch Index : " , 
                            batchIndex , "]")
            return
        for recordIndex , record in enumerate(batch):
            '''
            If the record which is located in selected batch is higher than 1MB,
            test will fail
            '''
            if len(record) > BYTE_CONSTANT.MB:
                logging.warning("Test 1 Failed , One of records is bigger than 1 MB [Batch Index : " , 
                                batchIndex , "Record Index : " , recordIndex , "]" )
                return
            batchByteSize += len(record)
            '''
            If the byte size of batch is higher than 5MB, test will fail
            '''
            if batchByteSize > BYTE_CONSTANT.MB * 5:
                logging.warning("Test 1 Failed , Batch Byte size bigger than 5MB")
                return
    logging.info("TEST 1 PASSED")      
            
            
if __name__ == "__main__":
    print("Test is starting")
    Test1()
    print("Test is finished, you can check results from BatchProgress.log file")