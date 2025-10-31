from ..core.visual_base import VisualBase
from ..types.transbuf import TransBuf
from ..types.group import Groups


class Pixels(VisualBase):
    def __init__(self, positions: TransBuf, colors: TransBuf, groups: Groups):
        super().__init__()

        self.positions: TransBuf = positions
        self.colors: TransBuf = colors
        self.groups: Groups = groups
