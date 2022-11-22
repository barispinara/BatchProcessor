'''
ByteSizeConstant
This file helps us to configure and set limitation on our batch processer class
You can change or edit values if you would like to change limitations.
'''

KB = 1024
MB = KB * KB #(1024 * 1024)
#BATCH_BYTE_SIZE represents total byte size of each batch
BATCH_BYTE_SIZE = 5 * MB
#BATCH_RECORD_SIZE represents total record size of each batch
BATCH_RECORD_SIZE = 500
#RECORD_BYTE_SIZE represents byte size of each record
RECORD_BYTE_SIZE = 1 * MB