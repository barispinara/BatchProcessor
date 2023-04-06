"""
--- test/batch_processor_test ---

Test class of BatchProcessor class
"""
import unittest
from batch_processor import BatchProcessor
from tests.input_record_generator \
    import input_record_generator,generate_single_record
from config.byte_size_constant import MB, KB

class BatchProcessorTest(unittest.TestCase):
    """
        BatchProcessorTest class
            - It contains several test functions for BatchProcessor class
    """
    def setUp(self):
        self.bp_object = BatchProcessor()

    def test_batch_generator_1(self):
        """
            Testing batch_generator() with 50 * 15B records 
        """
        input_record_list = input_record_generator(50 , 15)
        expected_batch_list = [input_record_list]
        returned_batch_list = self.bp_object.batch_generator(input_record_list)
        self.assertEqual(expected_batch_list, returned_batch_list)

    def test_batch_generator_2(self):
        """
            Testing batch_generator() with 50 * 15B records + 2MB record
        """
        input_record_list = input_record_generator(50 , 15)
        input_record_list.append(generate_single_record(2 * MB))
        expected_batch_list = [input_record_list[:-1]]
        returned_batch_list = self.bp_object.batch_generator(input_record_list)
        self.assertEqual(expected_batch_list, returned_batch_list)

    def test_batch_generator_3(self):
        """
            Testing batch_generator() with empty record list
        """
        returned_batch_list = self.bp_object.batch_generator([])
        self.assertEqual([] , returned_batch_list)

    def test_batch_generator_4(self):
        """
            Testing batch_generator() with 1000 * 15B records
        """
        input_record_list = input_record_generator(1000 , 15)
        expected_batch_list = [input_record_list[0:500],input_record_list[500:1000]]
        returned_batch_list = self.bp_object.batch_generator(input_record_list)
        self.assertEqual(expected_batch_list, returned_batch_list)

    def test_batch_generator_5(self):
        """
            Testing batch_generator() with 20 * 500KB records
        """
        input_record_list = input_record_generator(20 , 500 * KB)
        expected_batch_list = [input_record_list[0:10], input_record_list[10:20]]
        returned_batch_list = self.bp_object.batch_generator(input_record_list)
        self.assertEqual(expected_batch_list, returned_batch_list)
        