# slice_timings
Small module to calculate fMRI slice timings


bobkraft:


fmriprep requires a JSON file to contain meta information. Here is an example JSON file

{ "RepetitionTime": 3.0, "Instruction": "Lie still and keep your eyes open", "TaskName": "rest", "EchoTime": 0.030, "PhaseEncodingDirection" : "j", "EffectiveEchoSpacing" : 0.0354, "ParallelReductionFactorInPlane":1, "NumberOfVolumesDiscardedByScanner" : 4, "SliceTiming": [ 0.0, 1.5, 0.0625, 1.5625, 0.125, 1.625, 0.1875, 1.6875, 0.25, 1.75, 0.3125, 1.8125, 0.375, 1.875, 0.4375, 1.9375, 0.5, 2.0, 0.5625, 2.0625, 0.625, 2.125, 0.6875, 2.1875, 0.75, 2.25, 0.8125, 2.3125, 0.875, 2.375, 0.9375, 2.4375, 1.0, 2.5, 1.0625, 2.5625, 1.125, 2.625, 1.1875, 2.6875, 1.25, 2.75, 1.3125, 2.8125, 1.375, 2.875, 1.4375, 2.9375 ] }

Not all of the information needs to be in the JSON file. In particular, we need to calculate an array for slice timing. This calculation is straight forward. It would be nice to have python command line script to calculate this for the user. SliceTiming is in seconds from the first slice (0s) to the last slice (TR-<slice_acquisition_time>). The values of SliceTiming are stored in slice order not acquisition order.

Here is the calculation
Inputs:

TR = 3 # Repetition Time n_slices = 48 # Number of Slices order_slices = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,
36, 38, 40, 42, 44, 46, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23,
25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47] # This is a Siemens Interleaved ordering scheme. Even slices first, then odd

slices = list(range(1,nSlices-1))
Intermediate results:

delta = TR/n_slices

slice_timing = sorted(list( zip(order, slice*delta))) # You want to sort on first
Output

return slice_timing[:,2]

Here is an example

TR = 3 nSlices = 10 order = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9} # Note {} should be[] slice = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

sliceTiming = {{0, 0.}, {1, 1.5}, {2, 0.3}, {3, 1.8}, {4, 0.6}, {5, 2.1}, {6, 0.9}, {7, 2.4}, {8, 1.2}, {9, 2.7}}

return {0.0, 1.5, 0.3, 1.8, 0.6, 2.1, 0.9, 2.4, 1.2, 2.7}
