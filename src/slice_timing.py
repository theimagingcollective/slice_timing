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


def slice_times(rep_time: RepetitionTime, num_slices: NumberOfSlices, order: SliceOrdering, precision,
                unit,
                output,
                verbose,
                ):
    """
    Calculates the slice times and returns them as a list of floats.
    :param: Repetition Time (TR) in ms
    :param: Number of slices (int)
    :param: Scan Order of Slices (list[int])
    """
    slices_params = process_inputs(rep_time, num_slices, order)
    delta = slices_params.repetitiontime / slices_params.num_slices
    slice_timing = [slice_ * delta for slice_ in slices_params.scan_order]
    # slice_timing = sorted(list(zip(slices_params.scan_order, del_slice)))
    return slice_timing


def __construct_filename(rep_time: RepetitionTime, num_slices: NumberOfSlices):
    curr_dir = os.path.realpath(os.getcwd())
    try:
        filename = 'slicetimes-tr{}-n{}{}txt'.format(rep_time, num_slices, os.extsep)
    except TypeError:
        filename = 'slicetimes-tr{}-n{}{}txt'.format(rep_time, num_slices, os.extsep)
    finally:
        return os.path.join(curr_dir,filename)


def __write_to_file(filename: str, slice_timings: SliceTimings):
    slice_timings = str(slice_timings).strip('[').rstrip(']')
    with open(filename, 'w') as writeobj:
        writeobj.write(slice_timings)


def main():
    """Generates fMRI scan slice timings.
    Usage:
        python slice_timing.py rep_time num_slices
        Outputs to screen and txt file to current working directory.

    """
    cli_args = get_cli_args()
    print(cli_args)
    print(cli_args.__dict__)
    filename = __construct_filename(cli_args.rep_time, cli_args.num_slices)
    print(filename)
    slice_timings = slice_times(
                rep_time=cli_args.rep_time,
                num_slices=cli_args.num_slices,
                precision=cli_args.precision,
                unit=cli_args.unit,
                output=cli_args.output,
                verbose=cli_args.verbose,
                order=cli_args.order,
                )
    print(slice_timings)


def main2(tr: RepetitionTime, num_slices: NumberOfSlices, op=None):
    """Generates fMRI scan slice timings.
    Usage:
        python clice_timing.py tr num_slices
        Outputs to screen and txt file to current working directory.
    
    """
    
    filename = __construct_filename(tr, num_slices)
    slice_timings = slice_times(tr=tr, num_slices=num_slices)
    if op == 'print':
        print(slice_timings)
        sys.exit()
    elif op == 'pprint':
        pprint(slice_timings)
        sys.exit()
    else:
        print(slice_timings)
        __write_to_file(filename=filename,slice_timings=slice_timings)
    
    
def cli():
    """
    Basic Command line interface implementation
    :return: None
    """
    cli_args = sys.argv
    op = {
        '-p': print,
        '-pp': pprint,
        }
    for op_ in op.keys():
        try:
            op_idx = cli_args.index(op_)
        except ValueError:
            continue
    
    if '-h' in cli_args or '--help' in cli_args:
        print(__doc__)
        sys.exit()
    if '-p' in cli_args:
        op = 'print'
    elif '-pp' in cli_args:
        op = 'pprint'
    else:
        op = None
    try:
        main(cli_args[1], cli_args[2], op)
    except IndexError:
        print(__doc__)
        

if __name__ == '__main__':
    # main(3, 48)
    main()
    # import plac
    # plac.call(main)
    # cli()
    
    """
    
    :TODO:
    Write more tests
    Remove complicated custom type annotations.
    Refine the CLI
    
    Old Doc string:
    Usage:
    slice_timings [-h, --help] -tr <repetition time in ms> -ns <number of slices>
    
    Mandatory arguments:
    tr \t Specifies the repetition time (TR)  for the scan in ms. Positive integer.
    slices \t Specifies the number of slices in the scan. Positive integer.
    
    Optional arguments:
    -h, --help \t Displays the help (this text).
    -o, --order \t Order in which slices are scanned
        \t\t interleaved (default): even slices then odd slices
        \t\t striaght: regular order
        
    -op, --output \t Specifies how the output will be presented.
                        file (default): Output is saved to a text file as multiline CSV
                        s, screen: Output is shown on screen
    
    """
    
