"""
--- batch_processor ---
    - You can change batch and record limitations from
        config/byte_size_constant file
"""

from config.byte_size_constant import RECORD_BYTE_SIZE, BATCH_BYTE_SIZE

class BatchProcessor:
    """
        BatchProcessor class
            - It contains batch generator functions which creates batches
    """
    def batch_generator(self, record_list : list):
        """
            :@param:
                "record_list" : str list which holds records.
            :@description:
                The method generates batches and fills them with given record
                    according to limitation
            :@return:
                "batch_list" : List of List str
        """

        batch_list = []
        tmp_batch_byte_size = 0
        batch = []

        for record in record_list:
            if len(record) <= RECORD_BYTE_SIZE:
                if (tmp_batch_byte_size + len(record) >= BATCH_BYTE_SIZE
                            or len(batch) >= 500):
                    batch_list.append(batch)
                    batch = []
                    tmp_batch_byte_size = 0

                tmp_batch_byte_size += len(record)
                batch.append(record)

        if batch:
            batch_list.append(batch)

        return batch_list
