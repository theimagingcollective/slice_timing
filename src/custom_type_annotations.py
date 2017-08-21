from typing import NewType
from typing import List
from typing import Union
from typing import NamedTuple
from decimal import Decimal


RepetitionTime = NewType('RepetitionTime', Decimal)
NumberOfSlices = NewType('NumberOfSlices', int)
SliceScanOrder = NewType('SliceScanOrder', List[int])
SliceOrdering = NewType('SliceOrdering', Union['interleaved', 'straight'])
SliceParams = NewType('SliceParams', NamedTuple)
SliceTimings= NewType('SliceTimings', List[int])
