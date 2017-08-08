from src.preprocessing import process_inputs

from src.terminology import NumberOfSlices
from src.terminology import RepetitionTime
from src.terminology import SliceOrdering
from src.terminology import SliceTimings


def slice_times(tr: RepetitionTime, num_slices: NumberOfSlices, slices_order: SliceOrdering='interleaved'):
    """
    Calculates the slice times and returns them as a list of floats.
    :param: Repetition Time (TR) in ms
    :param: Number of slices (int)
    :param: Scan Order of Slices (list[int])
    """
    slices_params = process_inputs(tr, num_slices, slices_order)
    delta = slices_params.repetitiontime / slices_params.num_slices
    del_slice = [slice_ * delta for slice_ in slices_params.scan_order]
    slice_timing = sorted(list(zip(slices_params.scan_order, del_slice)))
    return slice_timing, del_slice

