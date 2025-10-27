# pip imports
import typing
import matplotlib.axes
import matplotlib.collections
import matplotlib.artist
import numpy as np

# local imports
from gsp.core.camera import Camera
from gsp.visuals.pixels import Pixels
from gsp.renderer.matplotlib.renderer import MatplotlibRenderer

class RendererPixels:
    @staticmethod
    def render_pixels(renderer: MatplotlibRenderer, axes: matplotlib.axes.Axes, visual: Pixels, camera: Camera) -> list[matplotlib.artist.Artist]:
        pixels: Pixels = visual

        # =============================================================================
        # Create the artists if needed
        # =============================================================================
        if pixels.uuid not in renderer._artists:
            mpl_path_collection = axes.scatter([], [])  # type: ignore
            mpl_path_collection.set_visible(False)  # hide until properly positioned and sized
            renderer._artists[pixels.uuid] = mpl_path_collection
            axes.add_artist(mpl_path_collection)
        
        # Get the existing artist
        mpl_path_collection = typing.cast(matplotlib.collections.PathCollection, renderer._artists[pixels.uuid])
        mpl_path_collection.set_visible(True)

        vertices_2d = np.random.rand(100, 2).astype(np.float32)

        mpl_path_collection.set_offsets(offsets=vertices_2d)
        # mpl_path_collection.set_sizes(typing.cast(list, [50]))  # set a default size for each point
        # mpl_path_collection.set_color(typing.cast(list, material.colors))
        # mpl_path_collection.set_edgecolor(typing.cast(list, material.edge_colors))
        # mpl_path_collection.set_linewidth(typing.cast(list, material.edge_widths))




        return [mpl_path_collection]


        