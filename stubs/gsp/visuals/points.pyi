from ..core.visual_base import VisualBase as VisualBase
from ..types.transbuf import TransBuf as TransBuf

class Points(VisualBase):
    positions: TransBuf
    sizes: TransBuf
    face_colors: TransBuf
    edge_colors: TransBuf
    edge_widths: TransBuf
    groups: TransBuf
    def __init__(self, positions: TransBuf, sizes: TransBuf, face_colors: TransBuf, edge_colors: TransBuf, edge_widths: TransBuf, groups: TransBuf) -> None: ...
