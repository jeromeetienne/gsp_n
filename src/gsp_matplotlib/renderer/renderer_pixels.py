# pip imports
import typing
import matplotlib.axes
import matplotlib.collections
import matplotlib.artist

# local imports
from gsp.core.camera import Camera
from gsp.visuals.pixels import Pixels
from gsp.types.transbuf_utils import TransBufUtils
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
        # Create the artists if needed
        # =============================================================================

        if pixels.uuid not in renderer._artists:
            mpl_path_collection = axes.scatter([], [])  # type: ignore
            mpl_path_collection.set_visible(False)  # hide until properly positioned and sized
            renderer._artists[pixels.uuid] = mpl_path_collection
            axes.add_artist(mpl_path_collection)

        # =============================================================================
        # Get existing artists
        # =============================================================================

        positions_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(pixels.positions))
        # sanity check
        assert positions_numpy.shape[1] == 3, "Positions must have shape (N, 3)"
        # TODO
        positions_2d = positions_numpy[:, :2]  # drop z-coordinate for 2D rendering

        colors_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(pixels.colors)) / 255.0  # normalize to [0, 1] range

        # =============================================================================
        # Create the artists if needed
        # =============================================================================

        if pixels.uuid not in renderer._artists:
            mpl_path_collection = axes.scatter([], [])  # type: ignore
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

        mpl_path_collection.set_offsets(offsets=positions_2d)
        mpl_path_collection.set_facecolor(typing.cast(list, colors_numpy))

        # Return the list of artists created/updated
        return [mpl_path_collection]
