# pip imports
import matplotlib.pyplot
import matplotlib.axes
import matplotlib.artist

# local imports
from gsp.core.camera import Camera
from gsp.core.canvas import Canvas
from gsp.core.visual_base import VisualBase

class MatplotlibRenderer:
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self._axes_per_viewport_uuid: dict[str, matplotlib.axes.Axes] = {}
        self._artists_per_visual_uuid: dict[str, matplotlib.artist.Artist] = {}

        # init all viewports
        for viewport in self.canvas.viewports:
            axes_rect = (viewport.x / self.canvas.width,
                         viewport.y / self.canvas.height,
                         viewport.width / self.canvas.width,
                         viewport.height / self.canvas.height)
            axes: matplotlib.axes.Axes = matplotlib.pyplot.axes(axes_rect)
            # this should be -1 to 1 - from normalized device coordinates - https://en.wikipedia.org/wiki/Graphics_pipeline
            # - https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_model_view_projection
            axes.set_xlim(-1, 1)
            axes.set_ylim(-1, 1)

            self._axes_per_viewport_uuid[viewport.uuid] = axes


    def render(self, visuals: list[VisualBase], cameras: list[Camera]):
        # Rendering logic using matplotlib goes here
        pass

