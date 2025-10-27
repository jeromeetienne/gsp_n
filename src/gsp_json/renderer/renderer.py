# local imports
from gsp.core.camera import Camera
from gsp.core.canvas import Canvas
from gsp.core.visual_base import VisualBase

class JsonRenderer:
    def __init__(self, canvas: Canvas):
        self.canvas = canvas

    def render(self, visuals: list[VisualBase], cameras: list[Camera]):
        # Rendering logic to output JSON goes here
        pass