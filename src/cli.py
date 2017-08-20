import argparse

from pprint import pprint

def get_cli_args(args_for_testing=None):
    arg_parser = argparse.ArgumentParser(description='Generates fMRI slice timings', prog='slice_timing.py', usage='%(prog)s --help for list of commands.')
    
    arg_parser.add_argument('rep_time', metavar='RepetitionTime(TR)', help='Repetition Time (TR). positive integer')
    arg_parser.add_argument('num_slices', metavar='NumberOfScanSlices', type=int, help='Number of slices in the scan.')
    arg_parser.add_argument('-o', '--order', default='interleaved', choices=['interleaved', 'sequential'],
                            metavar='', help='The order in which slices were scanned. Choices: %(choices)s. (default: %(default)s)')
    arg_parser.add_argument('-op', '--output', metavar='', default='show', choices=['show', 'save', 'list'],
                            help='Show the formatted slice times, save them to a file or show the unformatted list. Choices: %(choices)s. default: %(default)s')
    arg_parser.add_argument('-p', '--precision', metavar='', default=6, type=int, help='Specify the precision of the calculated slice times. (default: %(default)s)')
    arg_parser.add_argument('-v', '--verbose', action='store_true')  # will list all the parameters in a json style key-value pair.
    arg_parser.add_argument('-u', '--unit', metavar='', default='auto', choices=['auto', 's', 'ms'],
                            help='Specifies the unit of time to be used for the calculation. Choices: %(choices)s (default: %(default)s)')
    if args_for_testing:
        try:
            args_for_testing = args_for_testing.split()
        except AttributeError:
            raise ValueError('get_cli_args() only accepts str type arg for testing.')
        else:
            return arg_parser.parse_args(args_for_testing)
    else:
        return arg_parser.parse_args()


def scratchpad():
    print(0)
    # print(arg_parser.parse_args('3 4 -o sequential -p 3 -v -op c -u ms'))
    # print(arg_parser.parse_args('3 4'))
    
    print(1)
    # print(arg_parser.parse_args('3 4 --order sequential --precision 3 --verbose --output c --unit ms'))
    
    # print(2)
    # print(arg_parser.__doc__)
    
    print(3)
    # print(arg_parser.parse_args(['-h']))
    
    # print(4)
    # print(arg_parser.parse_args([]))
    
    
    # print(arg_parser.parse_args('3 4 -o a -p 3 -v -op c -u r'))
    # print(arg_parser.parse_args('3 4 -o equential -p 3 -v -op c -u ms'))


if __name__ == '__main__':
    pass
    # cli_args = get_cli_args('3 4 -o sequential -p 3 -v -u ms')
    # print(cli_args)
    cli_args = get_cli_args()
    print(cli_args)
    # cli_args = get_cli_args('3 4 -o sequential -p 3 -v -op c -u ms')
    # print(cli_args)
    # print(type(cli_args))
    # print(cli_args.__dict__)
    # pprint(cli_args.__dir__())
    # arg_parser.print_help()


