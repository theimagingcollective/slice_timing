import argparse
import slice_timing

arg_parser = argparse.ArgumentParser(description='Generates fMRI slice timings')
arg_parser.add_argument('rep_time')
arg_parser.add_argument('num_slices')
arg_parser.add_argument('-o', '--order')
# arg_parser.add_argument('-h', '--help')
arg_parser.add_argument('-op', '--output')
arg_parser.add_argument('-p', '--precision')
arg_parser.add_argument('-v', '--verbose')  # lists all the parameters in a json style key-value pair.

print(arg_parser.parse_args('3 4 -o a -p b -v True -op c'.split()))
