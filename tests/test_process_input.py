# import pytest
# from unittest.test import test_assertions
from collections import namedtuple

from src.preprocessing import process_inputs
from src.preprocessing import SlicesParams


# assertRaise


def _generate_test_data():
    SliceTimesInput = namedtuple('SliceTimesInput', 'repetitiontime num_slices ordering')
    test_data = {
        SliceTimesInput(repetitiontime=3, num_slices=48, ordering='interleaved'): SlicesParams(
                    repetitiontime=3, num_slices=48,
                    scan_order=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,
                                36, 38,
                                40, 42, 44, 46, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27,
                                29, 31,
                                33, 35, 37, 39, 41, 43, 45, 47]),
        
        SliceTimesInput(repetitiontime=3, num_slices=48, ordering='straight'): SlicesParams(
                    repetitiontime=3, num_slices=48,
                    scan_order=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                                19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]),
        
        SliceTimesInput(repetitiontime=10, num_slices=100, ordering='interleaved'): SlicesParams(
                    repetitiontime=10, num_slices=100,
                    scan_order=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,
                                36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68,
                                70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 1, 3, 5,
                                7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
                                41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73,
                                75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]),
        
        SliceTimesInput(repetitiontime=0, num_slices=48, ordering='straight'): SlicesParams(
                    repetitiontime=0, num_slices=48,
                    scan_order=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                                19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47])
            
        }
    return test_data


def test_process_inputs():
    test_data = _generate_test_data()
    for test_input, expected in test_data.items():
        actual = process_inputs(*test_input)
        # assert actual == expected
        print(expected)
        print(actual)

if __name__ == '__main__':
    test_process_inputs()
