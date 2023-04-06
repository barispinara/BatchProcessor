"""
--- test/input_record_generator

Helpful class for generating input record data for testing
"""
from string import ascii_lowercase
from random import choice

def input_record_generator(num_of_records : int , size_of_records : int):
    """
        :@description:
            The method generates example record list for testing
        :@return:
            "input_record_list": List of str
    """
    input_record_list = []
    for _ in range(num_of_records):
        generated_record = generate_single_record(size_of_records)
        input_record_list.append(generated_record)
    return input_record_list

def generate_single_record(size_of_records : int):
    """
        :@description:
            The method generates single record data for testing
        :@return:
            str
    """
    return ''.join(choice(ascii_lowercase
                          ) for i in range(size_of_records))
