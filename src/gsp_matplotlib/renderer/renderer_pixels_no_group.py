# pip imports
import typing
import matplotlib.axes
import matplotlib.collections
import matplotlib.artist

# local imports
from gsp.core.camera import Camera
from gsp.visuals.pixels import Pixels
from gsp.utils.transbuf_utils import TransBufUtils
from gsp.types.transbuf import TransBuf
from .renderer import MatplotlibRenderer
from ..extra.bufferx import Bufferx


class RendererPixels:
    @staticmethod
    def render(
        renderer: MatplotlibRenderer,
        axes: matplotlib.axes.Axes,
        visual: Pixels,
        model_matrix: TransBuf,
        camera: Camera,
    ) -> list[matplotlib.artist.Artist]:
        pixels: Pixels = visual

        # =============================================================================
        # Get existing artists
        # =============================================================================

        vertices_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(pixels._positions))
        # sanity check
        assert vertices_numpy.shape[1] == 3, "Positions must have shape (N, 3)"
        # TODO
        vertices_2d = vertices_numpy[:, :2]  # drop z-coordinate for 2D rendering

        colors_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(pixels._colors)) / 255.0  # normalize to [0, 1] range

        # =============================================================================
        # Create the artists if needed
        # =============================================================================

        if pixels.uuid not in renderer._artists:
            # Get DPI to compute pixel size
            assert axes.figure.get_dpi() is not None, "Canvas DPI must be set for proper pixel sizing"
            # TODO move that into a unit_helper module - to help with unit conversions
            one_point_in_inches = 1.0 / 72.0
            # Marker sizes in matplotlib are specified in "points squared" (pt²)
            # - Squaring the ratio converts a linear scale (points) to an area scale (points squared).
            size_point_squared = (one_point_in_inches * axes.figure.get_dpi()) ** 2
            # hardcoded scale factor to get approximately 1 pixel size
            size = 0.25 * size_point_squared

            mpl_path_collection = axes.scatter([], [], s=size, marker="o")
            mpl_path_collection.set_antialiased(True)
            mpl_path_collection.set_linewidth(0)
            mpl_path_collection.set_visible(False)
            # hide until properly positioned and sized
            renderer._artists[pixels.uuid] = mpl_path_collection
            axes.add_artist(mpl_path_collection)

        # =============================================================================
        # Get existing artists
        # =============================================================================

        mpl_path_collection = typing.cast(matplotlib.collections.PathCollection, renderer._artists[pixels.uuid])
        mpl_path_collection.set_visible(True)

        # =============================================================================
        # Update artists
        # =============================================================================

        mpl_path_collection.set_offsets(offsets=vertices_2d)
        mpl_path_collection.set_facecolor(typing.cast(list, colors_numpy))

        # Return the list of artists created/updated
        return [mpl_path_collection]
