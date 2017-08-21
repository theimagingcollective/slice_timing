"""
Module for preprocessing input for calculating slice timings.
Uage:
    from preprocessing import process_inputs
"""
import sys
from collections import namedtuple
from decimal import Decimal
from decimal import InvalidOperation

from custom_type_annotations import NumberOfSlices
from custom_type_annotations import RepetitionTime
from custom_type_annotations import SliceOrdering


SlicesParams = namedtuple('SlicesParams',
                        '''repetitiontime
                        num_slices
                        scan_order
                        precision
                        unit
                        output
                        verbose''')


def process_inputs(rep_time: RepetitionTime, num_slices: NumberOfSlices, order: SliceOrdering, precision,
                unit,
                output,
                verbose
                ) -> SlicesParams:
    """
    Helper function for slice_times() arg processing.
     - Repetition Time (TR) in ms
     - Number of slices (int)
     - Scan Order of Slices (list[int])
    :returns: Nmaedtuple SlicesParams.repetitiontime (int), SlicesParams.num_slices (int), SlicesParams.ordering (list of ints)
    """
    rep_time = _preprocess_repetitiontime(rep_time)
    num_slices = _preprocess_num_slices(num_slices)

    scan_order = _preprocess_scan_order(num_slices, order)
    unit = _preprocess_unit(unit=unit,rep_time=rep_time)
    
    slice_params = SlicesParams(repetitiontime=rep_time,
                                num_slices=num_slices,
                                scan_order=scan_order,
                                precision=precision,
                                unit=unit,
                                output=output,
                                verbose=verbose,
                                )
    return slice_params


def _preprocess_repetitiontime(rep_time: RepetitionTime):
    """
    Preprocesses & typechecks repetition time
     - rep_time: repetition time entered via the command line.
    :returns: rep_time (Decimal)
    """
    try:
        rep_time = Decimal(rep_time)
    except InvalidOperation as excep:
        print('ERROR: Repetition time has to be a positive number')
        sys.exit()
    else:
        if rep_time <= 0:
            print('ERROR: Repetition time can not be zero or negative')
            sys.exit()
    return rep_time


def _preprocess_num_slices(num_slices):
    """
    Preprocesses & typechecks number of slices.
     - num_slices: (NumOfSlices, int) number of slices entered via the command line.
    :returns: (NumOfSlices, Decimal) num_slices
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


def _preprocess_scan_order(num_slices, order):
    """
    Generates & typechecks the order in which slices are scanned.
    :param num_slices: number of slices returned by _preprocess_num_slices()
    :type num_slices: int
    :param order: order in which slices have been scanned, 'interleaved' or 'sequential'
    :type order: SliceOrdering Unnion['interleaved', 'sequential'] (str)
    :return: scan_order
    :rtype: SliceScanOrder List[int]
    """
    if order == 'interleaved':  # even-numbered scans followed by odd-numbered scans
        scan_order = list(range(0, num_slices, 2))
        scan_order.extend(list(range(1, num_slices, 2)))
    elif order == 'sequential':  # regular scan order
        scan_order = list(range(0, num_slices))
    else:
        print("Invalid argument: order only accepts: interleaved | sequential")
        sys.exit()
    return scan_order


def _preprocess_unit(unit, rep_time):
    if unit == 'auto':
        try:
            rep_time_f = float(rep_time)
        except ValueError:
            print('Repetition time must be a positive float or integer.')
        else:
            if rep_time_f <= 0:
                print('Repetition time can not be zero or a negative number.')
        
        float_int_diff = rep_time_f - int(rep_time)
        if float_int_diff:
            unit = 's'
        else:
            unit = 'ms'
        return unit
    

def test_preprocessing():
    cli_in = sys.argv
    print(_preprocess_repetitiontime(cli_in[1]))
    # print(_preprocess_repetitiontime('3a'))
    # print(_preprocess_unit('auto', 3.0))
    # print(_preprocess_unit('auto', 0.654))


if __name__ == '__main__':
    test_preprocessing()
    # _preprocess_repetitiontime()
