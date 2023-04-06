"""
--- test_runner ---

test_runner class which runs all test classes
"""

import unittest
from tests.batch_processor_test import BatchProcessorTest

def create_suite():
    """Test Suite creator"""
    test_classes = [
        BatchProcessorTest
    ]

    loader = unittest.TestLoader()

    suites_list = []
    for tests in test_classes:
        tmp_suite = loader.loadTestsFromTestCase(tests)
        suites_list.append(tmp_suite)

    return unittest.TestSuite(suites_list)

if __name__ == '__main__':
    suite = create_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
