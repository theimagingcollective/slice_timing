from collections import namedtuple

from src.terminology import *


SlicesInfo = namedtuple('SlicesInfo', 'repetitiontime num_slices scan_order')



def __process_inputs(tr: RepetitionTime, num_slices: NumberOfSlices, ordering: SliceScanOrder) -> SlicesInfo:
    """
    Helper function for slice_times() arg processing.
    :param: Repetition Time (TR) in ms
    :param: Number of slices (int)
    :param: Scan Order of Slices (list[int])
    :return: Nmaedtuple SlicesInfo.repetitiontime (int), SlicesInfo.num_slices (int), SlicesInfo.ordering (list of ints)
    """
    if ordering == 'interleaved':  # even-numbered scans followed by odd-numbered scans
        slices = list(range(0, num_slices, 2))
        slices.extend(list(range(1, num_slices, 2)))
    elif ordering == 'straight':  # regular scan order
        slices = list(range(0, num_slices))
    else:
        raise ValueError("Invalid argument: ordering only accepts: interleaved | straight")
    
    if not isinstance(num_slices, int):
        raise TypeError('Number of slices has to be a positive integer')
    if num_slices < 1:
        raise ValueError('Number of slices is atleast 1')
    
    try:
        total = sum(slices)
    except TypeError as excep:
        raise TypeError('{}. ordering must be a list or tuple of non-negative ints'.format(excep))
    else:
        if not total >= 0:
            raise ValueError('ordering can only contain non-negative integers')

    slices = [abs(slice_) for slice_ in slices]
    slice_params = SlicesInfo(repetitiontime=tr, num_slices=num_slices, scan_order=slices)
    return slice_params
    

def slice_times(tr: RepetitionTime, num_slices: NumberOfSlices, slices_order: SliceOrdering):
    """
    Calculates the slice times and returns them as a list of floats.
    :param: Repetition Time (TR) in ms
    :param: Number of slices (int)
    :param: Scan Order of Slices (list[int])
    """
    slices_params = __process_inputs(tr, num_slices, slices_order)
    slices = list(range(1, slices_params.num_slices-1))
    delta = slices_params.repetitiontime / slices_params.num_slices
    del_slice = [slice_ * delta for slice_ in slices_params.scan_order]
    slice_timing = sorted(list(zip(slices_params.scan_order, del_slice)))
    return slice_timing

def __generate_test_data():
    SliceTimesInput = namedtuple('SliceTimesInput', 'repetitiontime num_slices ordering')
    test_data = {
        SliceTimesInput(repetitiontime=3, num_slices=48, ordering='interleaved'): SlicesInfo(
            repetitiontime=3, num_slices=48,
            scan_order=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
                        40, 42, 44, 46, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31,
                        33, 35, 37, 39, 41, 43, 45, 47]),
        }
    return test_data


def test_process_inputs():
    test_data = __generate_test_data()
    for test_input, expected in test_data.items():
        actual = __process_inputs(*test_input)
        assert actual == expected
        

    
    


# slice_times(tr=RepetitionTime(3), num_slices= NumberOfSlices(48), slices_order=SliceScanOrder('interleaved'))
test_process_inputs()
