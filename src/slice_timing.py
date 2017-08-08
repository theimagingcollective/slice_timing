import os
from pprint import pprint

from preprocessing import process_inputs

from custom_type_annotations import NumberOfSlices
from custom_type_annotations import RepetitionTime
from custom_type_annotations import SliceOrdering
from custom_type_annotations import SliceTimings


def slice_times(tr: RepetitionTime, num_slices: NumberOfSlices, slices_order: SliceOrdering='interleaved'):
    """
    Calculates the slice times and returns them as a list of floats.
    :param: Repetition Time (TR) in ms
    :param: Number of slices (int)
    :param: Scan Order of Slices (list[int])
    """
    slices_params = process_inputs(tr, num_slices, slices_order)
    delta = slices_params.repetitiontime / slices_params.num_slices
    slice_timing = [slice_ * delta for slice_ in slices_params.scan_order]
    # slice_timing = sorted(list(zip(slices_params.scan_order, del_slice)))
    return slice_timing


def __construct_filename(tr: RepetitionTime, num_slices: NumberOfSlices):
    curr_dir = os.path.realpath(os.getcwd())
    try:
        filename = 'slicetimes-tr{}-n{}{}txt'.format(tr, num_slices, os.extsep)
    except TypeError:
        filename = 'slicetimes-tr{}-n{}{}txt'.format(tr, num_slices, os.extsep)
    finally:
        return os.path.join(curr_dir,filename)


def __write_to_file(filename: str, slice_timings: SliceTimings):
    slice_timings = str(slice_timings).strip('[').rstrip(']')
    with open(filename, 'w') as writeobj:
        writeobj.write(slice_timings)
    


def main(tr: RepetitionTime, num_slices: NumberOfSlices):
    """Generates fMRI scan slice timings.
    Usage:
        python clice_timing.py tr num_slices
        Outputs to screen and txt file to current working directory.
    
    """
    filename = __construct_filename(tr, num_slices)
    slice_timings = slice_times(tr=tr, num_slices=num_slices)
    pprint(slice_timings)
    __write_to_file(filename=filename,slice_timings=slice_timings)
    
    
def cli():
    import sys
    cli_args = sys.argv
    main(cli_args[1], cli_args[2])

if __name__ == '__main__':
    # main(3, 48)
    # import plac
    # plac.call(main)
    cli()
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
    
