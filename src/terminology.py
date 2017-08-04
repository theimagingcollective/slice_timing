from typing import NewType
from typing import List
from typing import Union
from typing import NamedTuple



RepetitionTime = NewType('RepetitionTime', int)
NumberOfSlices = NewType('NumberOfSlices', int)
SliceScanOrder = NewType('SliceScanOrder', List[int])
SliceOrdering = NewType('SliceOrdering', Union['interleaved', 'straight'])
SliceParams = NewType('SliceParams', NamedTuple)

