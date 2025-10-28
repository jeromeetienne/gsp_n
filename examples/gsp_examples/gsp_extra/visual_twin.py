# local imports
from .bufferx import Bufferx
from gsp.core.visual_base import VisualBase


class VisualTwin:
    def __init__(self, visual: VisualBase):
        self.uuid = visual.uuid
        self.model_matrix = Bufferx.mat4_identity()
        self.visual = visual
