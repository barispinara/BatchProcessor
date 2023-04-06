"""
--- config/byte_size_constant ---

This file helps us to configure and set limitation on our batch processer class
You can change or edit values if you would like to change limitations.
"""

KB = 1024
MB = KB * KB

BATCH_BYTE_SIZE = 5 * MB
BATCH_RECORD_SIZE = 500
RECORD_BYTE_SIZE = 1 * MB
