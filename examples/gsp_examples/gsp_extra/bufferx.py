from gsp.types import Buffer, BufferType
import numpy as np
import gsp.types.bufferx  # to avoid circular import

# re-export Bufferx here
# LATER: copy methods from gsp.types.bufferx.Bufferx
# - for now, just re-export, thus no code duplication
# - we dont want to force users to handle numpy, so it is in gsp_extra
Bufferx = gsp.types.bufferx.Bufferx
