import Config.ByteSizeConstant as BYTE_CONSTANT

#RECORD_BYTE_SIZE_START_LIMIT represents the start offset length of generated strings
RECORD_BYTE_SIZE_START_LIMIT = int(BYTE_CONSTANT.KB * 10)

#RECORD_BYTE_SIZE_END_LIMIT represents the end offset length of generated strings
RECORD_BYTE_SIZE_END_LIMIT = int(BYTE_CONSTANT.MB * 1.1)
'''
NUMBER_RECORD_START_LIMIT represents the start offset number of generated strings in
record array
'''
NUMBER_RECORD_START_LIMIT = 2000
'''
NUMBER_RECORD_END_LIMIT represents the end offset number of generated strings in
record array
'''
NUMBER_RECORD_END_LIMIT = 3000