# local imports
from .viewport import Viewport

class Canvas:
    def __init__(self, width: int, height: int, dpi: float):
        self.width = width
        self.height = height
        self.dpi = dpi
        self.viewports = []

    def add(self, viewport):
        self.viewports.append(viewport)

    def remove(self, viewport):
        self.viewports.remove(viewport)    