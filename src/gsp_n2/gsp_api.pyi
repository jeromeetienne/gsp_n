from enum import Enum
from typing import Literal, NewType, Union, overload, Any



class BufferType():
    """Type of elements in a Buffer. Heavily inspired by GLSL types."""

    float32 = NewType('float32', float)
    uint8 = NewType('uint8', int)
    uint16 = NewType('uint16', int)
    uint32 = NewType('uint32', int)
    int8 = NewType('int8', int)
    int16 = NewType('int16', int)
    int32 = NewType('int32', int)
    rgba8 = NewType('rgba8', int)
    vec2 = NewType('vec2', tuple[float, float])
    vec3 = NewType('vec3', tuple[float, float, float])
    vec4 = NewType('vec4', tuple[float, float, float, float])
    mat4 = NewType('mat4', list[list[float]])  # 16 floats

class Constants:
    """Common constants like colors."""

    red = BufferType.rgba8(int.from_bytes(bytearray([255, 0, 0, 255]), byteorder='big'))
    green = BufferType.rgba8(int.from_bytes(bytearray([0, 255, 0, 255]), byteorder='big'))
    blue = BufferType.rgba8(int.from_bytes(bytearray([0, 0, 255, 255]), byteorder='big'))


class Buffer:
    """typed array with single dimension
    - it is immutable in count and type, but mutable in content
    """

    def __init__(self, count: int, buffer_type: BufferType) -> None: ...
    def get_data(self, offset: int, length: int) -> bytearray: ...
    def set_data(self, data: bytearray, offset: int) -> None: ...
    def get_count(self) -> int: ...
    def get_type(self) -> BufferType: ...

# =============================================================================
# Transform
# =============================================================================

class Transform:
    """Chain of transformations to apply to data."""

    def to_buffer(self) -> Buffer: ...
    """Compute the transform and return a Buffer with the result."""

# =============================================================================
#
# =============================================================================

Groups = Union[int, list[int], list[list[int]]]
"""A type that can represent group IDs in various forms."""

TransBuf = Union[Transform, Buffer]
"""A type that can be either a Transform or a Buffer."""

# =============================================================================
# Texture
# =============================================================================

class Texture:
    def __init__(self, data: TransBuf, ndim: int) -> None: ...

class Texture2D(Texture):
    def __init__(self, data: TransBuf) -> None: ...

class Texture3D(Texture):
    def __init__(self, data: TransBuf) -> None: ...

# =============================================================================
#
# =============================================================================

class Canvas:
    def __init__(self, width: int, height: int, dpi: float) -> None: ...
    def set_dpi(self, dpi: float) -> None: ...
    def set_size(self, width: int, height: int) -> None: ...
    def get_dpi(self) -> float: ...
    def get_size(self) -> tuple[int, int]: ...
    def add(self, viewport: "Viewport") -> None: ...
    def remove(self, viewport: "Viewport") -> None: ...

class Viewport:
    def __init__(self, x: int, y: int, width: int, height: int) -> None: ...
    def set_size(self, width: int, height: int) -> None: ...
    def get_size(self) -> tuple[int, int]: ...
    def set_offset(self, x: int, y: int) -> None: ...
    def get_offset(self) -> tuple[int, int]: ...

# =============================================================================
#
# =============================================================================

class Visual:
    """Base class for visual elements like Pixels, Images, etc."""
    def __init__(self) -> None: ...

class Pixels(Visual):
    def __init__( self, positions: TransBuf, colors: TransBuf, groups: TransBuf ) -> None: ...
    """Visual element representing pixels.
    
    Arguments:
        positions: TransBuf representing pixel positions (BufferType.vec2 | BufferType.vec3).
        colors: TransBuf representing pixel colors (BufferType.rgba8).
        groups: TransBuf representing group IDs for pixels (BufferType.uint32).
    """

class Images(Visual):
    def __init__(
        self,
        positions: TransBuf,
        sizes: TransBuf,
        axes: TransBuf,
        angles: TransBuf,
        textures: list[Texture2D],
        groups: TransBuf,
    ) -> None: ...

# =============================================================================
# Renderer
# =============================================================================

class Camera:
    def __init__(self, view_matrix: TransBuf, projection_matrix: TransBuf) -> None: ...
    """
    Camera with view and projection matrices.

    Arguments:
        view_matrix: TransBuf representing the view matrix (BufferType.mat4).
        projection_matrix: TransBuf representing the projection matrix (BufferType.mat4).
    """

class MatplotlibRenderer:
    def __init__(self, canvas: Canvas) -> None: ...
    def render(self, viewports: list[Viewport], visuals: list[Visual], model_matrices: list[TransBuf], cameras: list[Camera]) -> None: ...
