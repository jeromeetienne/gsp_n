# stdlib imports
from enum import Enum

# pip imports
import numpy as np
from dataclasses import dataclass

class BufferType(Enum):
    """Type of elements in a Buffer. Heavily inspired by GLSL types."""

    float32 = 0
    uint32 = 1
    color = 1
    uint8 = 2
    int32 = 3
    int8 = 4
    vec2 = 5
    vec3 = 6
    vec4 = 7

    @staticmethod
    def get_itemsize(buffer_type: "BufferType") -> int:
        if buffer_type == BufferType.float32:
            return 4
        elif buffer_type == BufferType.uint32:
            return 4
        elif buffer_type == BufferType.color:
            return 4
        elif buffer_type == BufferType.uint8:
            return 1
        elif buffer_type == BufferType.int32:
            return 4
        elif buffer_type == BufferType.int8:
            return 1
        elif buffer_type == BufferType.vec2:
            return 8  # 2 * 4 bytes (float32)
        elif buffer_type == BufferType.vec3:
            return 12 # 3 * 4 bytes (float32)
        elif buffer_type == BufferType.vec4:
            return 16 # 4 * 4 bytes (float32)
        else:
            raise ValueError(f"Unknown BufferType: {buffer_type}")

    @staticmethod
    def to_numpy_dtype(buffer_type: "BufferType") -> np.dtype:
        if buffer_type == BufferType.float32:
            return np.float32
        elif buffer_type == BufferType.uint32 or buffer_type == BufferType.color:
            return np.uint32
        elif buffer_type == BufferType.uint8:
            return np.uint8
        elif buffer_type == BufferType.int32:
            return np.int32
        elif buffer_type == BufferType.int8:
            return np.int8
        elif buffer_type in (BufferType.vec2, BufferType.vec3, BufferType.vec4):
            return np.float32
        else:
            raise ValueError(f"Unknown BufferType: {buffer_type}")
    
    @staticmethod
    def to_numpy_shape(buffer_type: "BufferType") -> tuple:
        if buffer_type == BufferType.vec2:
            return (2,)
        elif buffer_type == BufferType.vec3:
            return (3,)
        elif buffer_type == BufferType.vec4:
            return (4,)
        else:
            return (1,)
        
if __name__ == "__main__":
    buffer_type = BufferType.vec3

    print("BufferType:", buffer_type, type(buffer_type))
