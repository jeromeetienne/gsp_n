from ..core.visual_base import VisualBase
from ..types.transbuf import TransBuf


class Pixels(VisualBase):
    def __init__(self, positions: TransBuf, colors: TransBuf, groups: TransBuf):
        super().__init__()

        self.positions: TransBuf = positions
        self.colors: TransBuf = colors
        self.groups: TransBuf = groups
