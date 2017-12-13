#!/usr/bin/env python3
"""
Generates fMRI scan slice timings.
"""
from decimal import Decimal
from decimal import getcontext
from typing import List

from preprocessing import process_inputs
from custom_type_annotations import NumberOfSlices
from custom_type_annotations import RepetitionTime
from custom_type_annotations import SliceOrdering
from cli import get_cli_args
from output import output_slices_info


def slice_times(rep_time: RepetitionTime, num_slices: NumberOfSlices, *,
                order: SliceOrdering='interleaved', precision=6, unit='auto', output='show', verbose=False,
                as_float=True
                ) -> List[float] or List[Decimal]:
    """
    Generates fMRI slice timings. Returns a list of Decimals.
    mandatory args: repetition time (Decimal), number of slices (int)
    
    rep_time: (positive Decimal) Repetition Time (TR).
    num_slices: (positive int) Number of slices in the scan.
    
    keyword only args (optional, * m=indicates defaults):
     - order: (str) The order in which slices were scanned.
          Choices: *interleaved, sequential
     - output: (str) How to output the results.
        Show the formatted slice times, save them to a file or show the unformatted list.
          Choices: *show, save, list
     - precision: (positive int) Specify the precision of the calculated slice times.
        (default: 6)
     - unit: (str) Specifies the unit of time to be used for the calculation.
        Choices: *auto, s, ms (default: auto)
          auto sets unit to ms if rep_time is int, s if Decimal
     - as_float: (bool) outputs the timing as list of floats or decimals.
        Choices: *True, False
    """
    slices_params = process_inputs(rep_time, num_slices, order, precision,
                                   unit,
                                   output,
                                   verbose,
                                   )
    getcontext().prec = precision
    delta = slices_params.repetitiontime / slices_params.num_slices
    slice_timing = [slice_ * delta for slice_ in slices_params.scan_order]
    if as_float:
	    slice_timing = [float(timing) for timing in slice_timing]
    return slice_timing, slices_params.scan_order


def main(args_for_testing: str=None):
    """Generates fMRI scan slice timings.
    Usage:
        <python3> slice_timing.py rep_time num_slices
        Outputs to screen.
    <python3> slice_timing.py -h or --help for detailed help.
    """
    cli_args = get_cli_args(args_for_testing)
    slice_timings, slice_order = slice_times(
                rep_time=cli_args.rep_time,
                num_slices=cli_args.num_slices,
                precision=cli_args.precision,
                unit=cli_args.unit,
                output=cli_args.output,
                verbose=cli_args.verbose,
                order=cli_args.order
                )
    output_slices_info(slice_timings=slice_timings,slice_order=slice_order, dest=cli_args.output,
                       rep_time=cli_args.rep_time, num_slices=cli_args.num_slices)
    

if __name__ == '__main__':
    main()
