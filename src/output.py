import os

from typing import List
from custom_type_annotations import RepetitionTime
from custom_type_annotations import NumberOfSlices
from custom_type_annotations import SliceTimings


def _reformat_slice_times(slice_timings):
    op_pfx = '"SliceTiming": ['
    gutter_len = len(op_pfx)
    gutter_insert = ''.join([',\n', ' '*gutter_len])
    slice_timings_str = [str(elem) for elem in slice_timings]
    slice_timings_str = [', '.join(slice_timings_str[start: start+10]) for start in range(0, len(slice_timings_str), 10)]
    slice_timings_str = gutter_insert.join(slice_timings_str)
    slice_timings_str = ''.join([op_pfx, slice_timings_str, ']'])
    return slice_timings_str


def _construct_filename(rep_time: RepetitionTime, num_slices: NumberOfSlices) -> object:
    curr_dir = os.path.realpath(os.getcwd())
    try:
        filename = 'slicetimes-tr{}-n{}{}txt'.format(rep_time, num_slices, os.extsep)
    except TypeError:
        filename = 'slicetimes-tr{}-n{}{}txt'.format(rep_time, num_slices, os.extsep)
    finally:
        return os.path.join(curr_dir,filename)


def _write_to_file(filename: str, slice_timings: SliceTimings):
    slice_timings = str(slice_timings).strip('[').rstrip(']')
    with open(filename, 'w') as writeobj:
        writeobj.write(slice_timings)
    print('Slice times saved to {}'.format(filename))
        
        
def output_slice_timings(slice_timings: List, dest: str='show'):
    slice_timings_str = _reformat_slice_times(slice_timings)
    if dest == 'show':
        print('\n', slice_timings_str)
    elif dest == 'save':
        filename = _construct_filename()
        _write_to_file(filename=filename, slice_timings=slice_timings_str)
    elif dest == 'list':
        print(slice_timings)
    else:
        return slice_timings_str
        

def test_data():
    '''
    "SliceTiming": [ 0.0, 1.5, 0.0625, 1.5625, 0.125, 1.625, 0.1875, 1.6875, 0.25, 1.75,
                        0.3125, 1.8125, 0.375, 1.875, 0.4375, 1.9375, 0.5, 2.0, 0.5625,
                        2.0625, 0.625, 2.125, 0.6875, 2.1875, 0.75, 2.25, 0.8125, 2.3125,
                        0.875, 2.375, 0.9375, 2.4375, 1.0, 2.5, 1.0625, 2.5625, 1.125, 2.625,
                        1.1875, 2.6875, 1.25, 2.75, 1.3125, 2.8125, 1.375, 2.875, 1.4375, 2.9375\
    ]
    '''
    slice_timings = [0.0, 30.0, 60.0, 90.0, 120.0, 150.0, 180.0, 210.0, 240.0, 270.0, 300.0, 330.0,
                     360.0, 390.0, 420.0, 450.0, 480.0, 510.0, 540.0, 570.0, 15.0, 45.0, 75.0,
                     105.0, 135.0, 165.0, 195.0, 225.0, 255.0, 285.0, 315.0, 345.0, 375.0, 405.0,
                     435.0, 465.0, 495.0, 525.0, 555.0, 585.0]
    
    slice_timings = [0.0, 1.5, 0.0625, 1.5625, 0.125, 1.625, 0.1875, 1.6875, 0.25, 1.75,
                     0.3125, 1.8125, 0.375, 1.875, 0.4375, 1.9375, 0.5, 2.0, 0.5625,
                     2.0625, 0.625, 2.125, 0.6875, 2.1875, 0.75, 2.25, 0.8125, 2.3125,
                     0.875, 2.375, 0.9375, 2.4375, 1.0, 2.5, 1.0625, 2.5625, 1.125, 2.625,
                     1.1875, 2.6875, 1.25, 2.75, 1.3125, 2.8125, 1.375, 2.875, 1.4375, 2.9375
                     ]
    return slice_timings


if __name__ == '__main__':
    slice_timings = test_data()
    (_reformat_slice_times(slice_timings))
