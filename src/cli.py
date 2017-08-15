import argparse
import slice_timing

arg_parser = argparse.ArgumentParser(description='Generates fMRI slice timings', prog='slice_timing.py', usage='%(prog)s --help for list of commands.')

arg_parser.add_argument('rep_time', metavar='RepetitionTime(TR)', type=int, help='Repetition Time (TR). positive integer')
arg_parser.add_argument('num_slices', metavar='NumberOfScanSlices', type=int, help='Number of slices in the scan.')
arg_parser.add_argument('-o', '--order', default='interleaved', choices=['interleaved', 'sequential'],
                        metavar='', help='The order in which slices were scanned. Choices: %(choices)s. (default: %(default)s)')
arg_parser.add_argument('-op', '--output', metavar='', default='file')
arg_parser.add_argument('-p', '--precision', metavar='', default=6, type=int, help='Specify the precision of the calculated slice times. (default: %(default)s)')
arg_parser.add_argument('-v', '--verbose', action='store_true')  # will list all the parameters in a json style key-value pair.
arg_parser.add_argument('-u', '--unit', metavar='', default='s', choices=['s', 'ms'], help='Specifies the unit of time to be used for the calculation. Choices: %(choices)s (default: %(default)s)')


if __name__ == '__main__':
    pass
    cli_args = arg_parser.parse_args()
    print(cli_args)
    # arg_parser.print_help()


def scratchpad():
    print(0)
    print(arg_parser.parse_args('3 4 -o sequential -p 3 -v -op c -u ms'.split()))
    print(arg_parser.parse_args('3 4'.split()))
    
    print(1)
    print(arg_parser.parse_args('3 4 --order sequential --precision 3 --verbose --output c --unit ms'.split()))
    
    # print(2)
    # print(arg_parser.__doc__)
    
    print(3)
    print(arg_parser.parse_args(['-h']))
    
    # print(4)
    # print(arg_parser.parse_args([]))
    
    
    # print(arg_parser.parse_args('3 4 -o a -p 3 -v -op c -u r'.split()))
    # print(arg_parser.parse_args('3 4 -o equential -p 3 -v -op c -u ms'.split()))
    
    
