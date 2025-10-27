# pip imports
import uuid

# local imports
from .viewport import Viewport

class Canvas:
    def __init__(self, width: int, height: int, dpi: float):
        self.uuid = str(uuid.uuid4())
        self.width = width
        self.height = height
        self.dpi = dpi
        self.viewports: list[Viewport] = []

    def add(self, viewport: Viewport):
        self.viewports.append(viewport)

    def remove(self, viewport: Viewport):
        self.viewports.remove(viewport)