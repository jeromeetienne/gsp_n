from ..core.visual_base import VisualBase as VisualBase
from ..types.transbuf import TransBuf as TransBuf

class Pixels(VisualBase):
    positions: TransBuf
    colors: TransBuf
    groups: TransBuf
    def __init__(self, positions: TransBuf, colors: TransBuf, groups: TransBuf) -> None: ...
