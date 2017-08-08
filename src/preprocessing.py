"""
Module for preprocessing input for calculating slice timings.
Uage:
    from preprocessing import process_inputs
"""
import sys
from collections import namedtuple

from custom_type_annotations import NumberOfSlices
from custom_type_annotations import RepetitionTime
from custom_type_annotations import SliceScanOrder


SlicesInfo = namedtuple('SlicesInfo', 'repetitiontime num_slices scan_order')


def process_inputs(tr: RepetitionTime, num_slices: NumberOfSlices, ordering: SliceScanOrder) -> SlicesInfo:
    """
    Helper function for slice_times() arg processing.
    :param: Repetition Time (TR) in ms
    :param: Number of slices (int)
    :param: Scan Order of Slices (list[int])
    :return: Nmaedtuple SlicesInfo.repetitiontime (int), SlicesInfo.num_slices (int), SlicesInfo.ordering (list of ints)
    """
    tr = __preprocess_repetitiontime(tr)
    num_slices = __preprocess_num_slices(num_slices)

    scan_order = __preprocess_scan_order(num_slices, ordering)
    
    slice_params = SlicesInfo(repetitiontime=tr, num_slices=num_slices, scan_order=scan_order)
    return slice_params


def __preprocess_repetitiontime(tr: str):
    """
    Preprocesses & typechecks repetition time
    :param tr: repetition time entered via the command line.
    :type: str
    :return: tr
    :rtype: RepetitionTime: int
    """
    try:
        tr = int(tr)
    except ValueError:
        print('Repetition time has to be a positive integer')
        sys.exit()
    else:
        if tr <= 0:
            print('Repetition time can not be zero or negative')
            sys.exit()
    return tr


def __preprocess_num_slices(num_slices):
    """
    Preprocesses & typechecks number of slices.
    :param num_slices: number of slices entered via the command line.
    :type: str
    :return: num_slices
    :rtype: NumberOfSlices: int
    """
    try:
        num_slices = int(num_slices)
    except ValueError:
        print('Number of slices has to be a positive integer')
        sys.exit()
    else:
        if num_slices < 1:
            print('Number of slices must be 1 or more')
            sys.exit()
    return num_slices


def __preprocess_scan_order(num_slices, ordering):
    """
    Generates & typechecks the order in which slices are scanned.
    :param num_slices: number of slices returned by __preprocess_num_slices()
    :type num_slices: int
    :param ordering: order in which slices have been scanned, 'interleaved' or 'straight'
    :type ordering: SliceOrdering Unnion['interleaved', 'straight'] (str)
    :return: scan_order
    :rtype: SliceScanOrder List[int]
    """
    if ordering == 'interleaved':  # even-numbered scans followed by odd-numbered scans
        scan_order = list(range(0, num_slices, 2))
        scan_order.extend(list(range(1, num_slices, 2)))
    elif ordering == 'straight':  # regular scan order
        scan_order = list(range(0, num_slices))
    else:
        print("Invalid argument: ordering only accepts: interleaved | straight")
        sys.exit()
    return scan_order




