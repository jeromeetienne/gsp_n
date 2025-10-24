from datetime import datetime
from enum import Enum
from typing import Literal, Optional

from pydantic.dataclasses import dataclass

@dataclass 
class GspMessage:
    message_id: int
    """id is increasing integer identifier for each message"""

# =============================================================================
# Canvas
# =============================================================================

@dataclass
class CanvasCreate(GspMessage):
    canvas_uuid: str
    """unique identifier for the canvas"""
    width: int
    """width of the canvas in pixels"""
    height: int
    """height of the canvas in pixels"""
    dpi: float
    """dots per inch (DPI) of the canvas"""

@dataclass
class CanvasSetDpi(GspMessage):
    canvas_uuid: str
    """unique identifier for the canvas"""
    dpi: float
    """dots per inch (DPI) of the canvas"""

@dataclass
class CanvasSetSize(GspMessage):
    canvas_uuid: str
    """unique identifier for the canvas"""
    width: int
    """width of the canvas in pixels"""
    height: int
    """height of the canvas in pixels"""

# =============================================================================
# Viewport
# =============================================================================

@dataclass
class Viewport(GspMessage):
    viewport_uuid: str
    canvas_uuid: str
    x: int
    y: int
    width: int
    height: int

@dataclass
class ViewportSetPosition(GspMessage):
    viewport_uuid: str
    x: int
    y: int

@dataclass
class ViewportSetSize(GspMessage):
    viewport_uuid: str
    width: int
    height: int

# =============================================================================
# 
# =============================================================================


@dataclass
class TransformLink(GspMessage):
    ...

@dataclass
class TransformLinkOperator(TransformLink):
    operator: Literal['add', 'sub', 'mul', 'div']
    operand: float | int

@dataclass
class Transform(GspMessage):
    links: list[TransformLink]
    """list of links defining the transform"""


# =============================================================================
# Buffer
# =============================================================================
class BufferType(Enum):
    """Type of elements in a Buffer"""
    int32 = 'int32'
    float32 = 'float32'
    float64 = 'float64'

@dataclass
class Buffer(GspMessage):
    """typed array of a single dimension"""
    buffer_uuid: str
    """unique identifier for the buffer"""
    count: int
    """number of elements of <type> in the buffer"""
    type: BufferType
    """type of each elements in the buffer"""
    data: bytes
    """Contiguous byte array representing the buffer data"""

TransBuffer = Transform | Buffer

# =============================================================================
# Visual
# =============================================================================
@dataclass
class Visual(GspMessage):
    visual_uuid: str
    """unique identifier for the visual"""

@dataclass
class Pixels(Visual):
    positions: TransBuffer
    """Transform or Buffer representing pixel positions"""
    colors: TransBuffer
    """Transform or Buffer representing pixel colors"""
    groups: TransBuffer
    """Transform or Buffer representing pixel groups"""