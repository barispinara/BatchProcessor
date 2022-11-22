#BatchProcesser Class
#This class helps to generate batch according to given limitation and given record list
#The limitation of batches and records are stored in Config/ByteSizeConstant.py
#You can configure limitations from Config/ByteSizeConstant.py easily.

import Config.ByteSizeConstant as BYTE_CONSTANT
import logging
import time
import datetime

class BatchProcessor:
    def __init__(self, recordList):
        self.recordList = recordList
        #Logging definition, log records which belong to the batch processers will be stored in BatchProgress.log file
        logging.basicConfig(filename="BatchProgress.log", format="[%(asctime)s : %(levelname)s] %(message)s", level=logging.DEBUG)
    
    def BatchGenerator(self, startRecordIndex):
        '''
        --BatchGenerator()
        param: "startRecordIndex" -> This is a current index in the given record list so method can continue the splitting operation from last batch record index
        Definition: This methods basically splits the records according to given limitation. This method can be built by using cache but according to given assignment documentation
                    the order of records shouldn't be interrupted that's why system adds records in to the batch linearly.
        '''
        
        #New batch list
        newBatch = []
        batchByteSize = 0
        
        for recordIndex in range(startRecordIndex, len(self.recordList)):
            # If the size of record is bigger than 1MB then it will be discarded
            if len(self.recordList[recordIndex]) < BYTE_CONSTANT.RECORD_BYTE_SIZE:
                newBatchByteSize = len(self.recordList[recordIndex]) + batchByteSize
                # If the batch size reached 500 or batch byte size reached 5MB then system will stop adding new record in to the batch.
                if newBatchByteSize < BYTE_CONSTANT.BATCH_BYTE_SIZE and len(newBatch) < 500:
                    newBatch.append(self.recordList[recordIndex])
                    batchByteSize += len(self.recordList[recordIndex])
                else:
                    return newBatch, recordIndex
            else:
                continue
        
        # If we added all records in to the batches but batch is not still fulled, then this return state will work
        return newBatch, len(self.recordList)
    
    def BatchProgressing(self):
        logging.info("BatchProcessing is starting")
        startTime = datetime.datetime.now()
        # batchList: all batches will be stored in this variable
        batchList = []
        # startRecordIndex: start index of record list
        startRecordIndex = 0
        # Iterating all records in this while loop.
        while startRecordIndex < len(self.recordList):
            # BatchGenerator method also gives last added record index.
            filledBatch, startRecordIndex = self.BatchGenerator(startRecordIndex)
            batchList.append(filledBatch)
        endTime = datetime.datetime.now()
        timeDiff = endTime - startTime
        logging.info("Batch Processing is finished in " + str(timeDiff.total_seconds() * 1000) + " ms")
        logging.info("Numbers of generated batch : " + str(len(batchList)))
        return batchList
        
        
