slice_timings is a small module to calculate fMRI slice timings

fmriprep (https://github.com/poldracklab/fmriprep) requires a JSON file to contain meta information.

Here is an example JSON file
{ "RepetitionTime": 3.0,
"Instruction": "Lie still and keep your eyes open",
"TaskName": "rest",
"EchoTime": 0.030,
"PhaseEncodingDirection" : "j",
"EffectiveEchoSpacing" : 0.0354,
"ParallelReductionFactorInPlane":1,
"NumberOfVolumesDiscardedByScanner" : 4,
"SliceTiming": [ 0.0, 1.5, 0.0625, 1.5625, 0.125, 1.625, 0.1875, 1.6875, 0.25, 1.75, 0.3125, 1.8125, 0.375, 1.875, 0.4375, 1.9375, 0.5, 2.0, 0.5625, 2.0625, 0.625, 2.125, 0.6875, 2.1875, 0.75, 2.25, 0.8125, 2.3125, 0.875, 2.375, 0.9375, 2.4375, 1.0, 2.5, 1.0625, 2.5625, 1.125, 2.625, 1.1875, 2.6875, 1.25, 2.75, 1.3125, 2.8125, 1.375, 2.875, 1.4375, 2.9375 ]
}

An array for slice timing needs to be calculated. This calculation is straight forward.  
slice_timings serves as a python command line script and importable module/function to calculate this for the user.
