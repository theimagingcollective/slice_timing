"""
Generates fMRI scan slice timings.
Usage:
    $<python> <path>/slice_timing.py [-h, --help] rep_time num_slices [-p, -pp]
    
    Mandatory Arguments: Repetition time (rep_time), number of slices (num_slices)
    Default: Outputs to screen and txt file in current working directory.
    
    Optional Arguments:
             -h, --help : \t Diplays the help (this text).
             -p         : \t Print output to screen in one line. Do not output to file.
            -pp         : \t Pretty print output to screen , one entry per-line. Do not output to file.
    
"""
import os
import sys

from pprint import pprint

from preprocessing import process_inputs
from custom_type_annotations import NumberOfSlices
from custom_type_annotations import RepetitionTime
from custom_type_annotations import SliceOrdering
from custom_type_annotations import SliceTimings
from cli import get_cli_args

from output import output_slice_timings

def slice_times(rep_time: RepetitionTime, num_slices: NumberOfSlices, *, order: SliceOrdering='interleaved', precision=6,
                unit='auto',
                output='show',
                verbose=False
                ):
    """
    Calculates the slice times and returns them as a list of floats.
    :param: Repetition Time (TR) in ms
    :param: Number of slices (int)
    :param: Scan Order of Slices (list[int])
    """
    slices_params = process_inputs(rep_time, num_slices, order, precision,
                unit,
                output,
                verbose,
                )
    print(slices_params)
    # quit()
    delta = slices_params.repetitiontime / slices_params.num_slices
    slice_timing = [slice_ * delta for slice_ in slices_params.scan_order]
    # slice_timing = sorted(list(zip(slices_params.scan_order, del_slice)))
    return slice_timing


def main(args_for_testing: str=None):
    """Generates fMRI scan slice timings.
    Usage:
        python slice_timing.py rep_time num_slices
        Outputs to screen and txt file to current working directory.

    """
    cli_args = get_cli_args(args_for_testing)
    print(cli_args)
    # print(cli_args.__dict__)
    # filename = _construct_filename(cli_args.rep_time, cli_args.num_slices)
    # print(filename)
    slice_timings = slice_times(
                rep_time=cli_args.rep_time,
                num_slices=cli_args.num_slices,
                precision=cli_args.precision,
                unit=cli_args.unit,
                output=cli_args.output,
                verbose=cli_args.verbose,
                order=cli_args.order
                )
    output_slice_timings(slice_timings, cli_args.output)



if __name__ == '__main__':
    # main(3, 48)
    main('3, 4')
    # import plac
    # plac.call(main)
    # cli()
    
    """
    
    :TODO:
    Write more tests
    Remove complicated custom type annotations.
    Refine the CLI
    """
    
