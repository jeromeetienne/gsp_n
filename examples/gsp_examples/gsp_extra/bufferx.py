from gsp.types import Buffer, BufferType
import numpy as np
import gsp.types.bufferx  # to avoid circular import

# re-export Bufferx here
# LATER: copy methods from gsp.types.bufferx.Bufferx
Bufferx = gsp.types.bufferx.Bufferx


# # =============================================================================
# # Matrix functions
# # =============================================================================

# @staticmethod
# def identity4() -> Buffer:
#     mat4_numpy = np.identity(4, dtype=np.float32)
#     buffer = Bufferx.from_numpy(mat4_numpy, BufferType.mat4)
#     return buffer

# # =============================================================================
# # .to_numpy/.from_numpy
# # =============================================================================
# @staticmethod
# def to_numpy(buffer: Buffer) -> np.ndarray:
#     if buffer.get_type() != BufferType.mat4:
#         # sanity check
#         assert buffer.get_type() == BufferType.mat4, "Buffer type must be mat4"
#         # TODO what about count

#         return np.frombuffer(buffer.to_bytearray(), dtype=np.float32).reshape((4, 4))
#     else:
#         raise NotImplementedError("Only mat4 buffers are supported")

# @staticmethod
# def from_numpy(array_numpy: np.ndarray, bufferType: BufferType) -> Buffer:
#     if bufferType == BufferType.float32:
#         # sanity check
#         assert array_numpy.dtype == np.float32, "Numpy array must be of dtype float32"

#         count = array_numpy.shape[0]
#         buffer = Buffer(count, bufferType)
#         buffer.set_data(bytearray(array_numpy.tobytes()), 0, count)
#         return buffer
#     elif bufferType == BufferType.mat4:
#         # sanity check
#         assert array_numpy.shape == (4, 4), "Numpy array must be of shape (4, 4)"

#         buffer = Buffer(1, bufferType)
#         buffer.set_data(bytearray(array_numpy.astype(np.float32).tobytes()), 0, 1)
#         return buffer
#     elif bufferType == BufferType.vec3:
#         # sanity check
#         assert array_numpy.shape.__len__() == 2 and array_numpy.shape[1] == 3, "Numpy array must be of shape (3,)"

#         count = array_numpy.shape[0]
#         buffer = Buffer(1, bufferType)
#         buffer.set_data(bytearray(array_numpy.astype(np.float32).tobytes()), 0, 1)
#         return buffer
#     else:
#         raise NotImplementedError(f'unable to create a {bufferType} buffer from numpy array of shape {array_numpy.shape} and dtype {array_numpy.dtype}')
