from enum import Enum
from typing import Literal, Union, overload, Any

import numpy

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
    # LATER: add more types for completeness

class Constants:
    """Common constants like colors."""

    red = numpy.uint32(0xFF0000FF)
    green = numpy.uint32(0x00FF00FF)
    blue = numpy.uint32(0x0000FFFF)

class Buffer:
    """typed array with single dimension
    - it is immutable in count and type, but mutable in content
    """

    def __init__(self, count: int, buffer_type: BufferType) -> None: ...
    def get_data(self, offset: int, length: int) -> bytes: ...
    def set_data(self, data: bytes, offset: int) -> None: ...
    def get_count(self) -> int: ...
    def get_type(self) -> BufferType: ...

    # Fill method overloads
    @overload
    def fill(self, value: numpy.uint32) -> "Buffer": ...
    @overload
    def fill(self, value: numpy.uint8) -> "Buffer": ...
    def fill(self, value: Union[numpy.uint32, numpy.uint8]) -> "Buffer": ...

    # numpy conversion
    def to_numpy(self) -> numpy.ndarray: ...
    @staticmethod
    def from_numpy(ndarray: numpy.ndarray) -> "Buffer": ...

class Mat4:
    """4x4 Matrix. Handle Model, View, Projection matrices."""

    def __init__(self, data: list[list[float]] | None = None) -> None: ...
    """4x4 Matrix. if data is None, initializes to identity matrix."""
    def get_data(self) -> list[list[float]]: ...
    def set_data(self, data: list[list[float]]) -> None: ...
    @staticmethod
    def from_numpy(ndarray: numpy.ndarray) -> "Mat4": ...

class DataSource:
    """Data source from which data can be loaded and **decoded**, e.g., image file path. .npy numpy files"""

    def __init__(self, uri: str) -> None: ...
    def to_buffer(self, buffer_type: BufferType = BufferType.uint8) -> Buffer: ...

# =============================================================================
# Transform
# =============================================================================

class TransformLink:
    """Base class for a link in a Transform chain."""
    ...

class Transform:
    """Chain of transformations to apply to data."""

    def to_buffer(self) -> Buffer: ...
    """Compute the transform and return a Buffer with the result."""

    links: list[TransformLink]
    """Ordered list of links defining the transform."""

# =============================================================================
# Predefined Transform links
# - all those those classes are instance of TransformLink, they could/should be in user-space gsp-extra
# =============================================================================

class TransformOperator(TransformLink):
    """A transformation link that applies an operator with an operand."""

    operator: Literal['add', 'sub', 'mul', 'div']
    """Operator to apply. One of 'add', 'sub', 'mul', 'div'."""

    # FIXME: this operand may be a Buffer or a Transform in the future
    # FIXME: provide a .copy()
    operand: Union[float, int]
    """Operand for the operator."""

class TransformDataSource(TransformLink):
    """A transformation link that loads data from a DataSource."""

    data_source: DataSource
    """Data source to load data from."""

class TransformMeasure(TransformLink):
    """A transformation link that applies unit conversion."""

    unit: Literal['dot', 'pixel', 'inch', 'centimeter']
    """Unit to convert to, e.g., 'meter', 'pixel', etc."""

class TransformAccessor(TransformLink):
    """A transformation link that accesses a specific field from structured data."""

    field_name: Literal['x', 'y', 'z', 'w', 'r', 'g', 'b', 'a']
    """Name of the field to access in the structured data."""

class TransformSetData(TransformLink):
    """A transformation link that copy data from a Buffer."""

    buffer: Buffer
    """Buffer to use in the transformation."""
    offset: int
    """Offset in the buffer to start reading data from."""
    count: int
    """Number of elements to read from the buffer."""

class TransformColorMap(TransformLink):
    """A transformation link that project scalar data to color using a colormap. Assume the scalar is normalized between 0 and 1."""

    colormap_name: Literal['viridis', 'plasma', 'inferno', 'magma', 'cividis']
    """Name of the colormap to use. Based on matplotlib colormaps."""

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
    def add(self, visual: "Visual") -> None: ...
    def remove(self, visual: "Visual") -> None: ...

# =============================================================================
#
# =============================================================================

class Visual:
    """Base class for visual elements like Pixels, Images, etc."""

    def __init__(self, model_matrix: Mat4) -> None: ...
    def get_model_matrix(self) -> Mat4: ...
    def set_model_matrix(self, matrix: Mat4) -> None: ...

class Pixels(Visual):
    def __init__(
        self, positions: TransBuf, colors: TransBuf, groups: TransBuf
    ) -> None: ...
    def set_positions(self, x: int, y: int, color: tuple[int, int, int]) -> None: ...
    def get_positions(self) -> list[tuple[int, int, tuple[int, int, int]]]: ...

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
    def __init__(self, view_matrix: Mat4, projection_matrix: Mat4) -> None: ...

class MatplotlibRenderer:
    def __init__(self, canvas: Canvas) -> None: ...
    def render(self, visuals: list[Visual], cameras: list[Camera]) -> None: ...
