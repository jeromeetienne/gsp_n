# local imports
from .bufferx import Bufferx
from gsp.core.visual_base import VisualBase


class VisualTwin:
    def __init__(self, visual: VisualBase):
        self.uuid = visual.uuid
        """uuid of the visual being wrapped."""
        self.visual = visual
        """the visual being wrapped."""
        self.model_matrix = Bufferx.mat4_identity()
        """model matrix of the visual being wrapped."""
