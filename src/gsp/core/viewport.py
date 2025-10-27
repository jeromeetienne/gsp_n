
# pip imports
import uuid


class Viewport:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.uuid = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visuals = []  # List to hold visual elements added to the viewport

    def add(self, visual):
        self.visuals.append(visual)
    
    def removd(self, visual):
        self.visuals.remove(visual)