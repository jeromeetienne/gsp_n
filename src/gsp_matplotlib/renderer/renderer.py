# pip imports
import matplotlib.pyplot
import matplotlib.axes
import matplotlib.artist

# local imports
from gsp.core.camera import Camera
from gsp.core.canvas import Canvas
from gsp.core.viewport import Viewport
from gsp.core.visual_base import VisualBase
from gsp.visuals.points import Points


class MatplotlibRenderer:

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self._axes: dict[str, matplotlib.axes.Axes] = {}
        self._artists: dict[str, matplotlib.artist.Artist] = {}

        # Create a figure of 512x512 pixels
        self._figure = matplotlib.pyplot.figure(figsize=(canvas.width / canvas.dpi, canvas.height / canvas.dpi), dpi=canvas.dpi)

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
            # store axes for this viewport
            self._axes[viewport.uuid] = axes

    def render(self, viewports: list[Viewport], visuals: list[VisualBase], cameras: list[Camera]):

        # sanity check 
        assert len(viewports) == len(visuals) == len(cameras), f'Mismatched lengths: {len(viewports)} viewports, {len(visuals)} visuals, {len(cameras)} cameras'

        # loop over each viewport, visual, camera triplet to render them
        for viewport, visual, camera in zip(viewports, visuals, cameras):
            self._render_visual(viewport, visual, camera)


    def _render_visual(self, viewport: Viewport, visual: VisualBase, camera: Camera):
        """ Render a single visual in a given viewport using the specified camera. """
        axes = self._axes[viewport.uuid]
        if isinstance(visual, Points):
            from gsp_matplotlib.renderer.renderer_points import RendererPoints
            RendererPoints.render(self, axes, visual, camera)
        else:
            raise NotImplementedError(f'Rendering for visual type {type(visual)} is not implemented.')

    def get_axes_for_viewport(self, viewport: Viewport) -> matplotlib.axes.Axes:
        return self._axes[viewport.uuid]

