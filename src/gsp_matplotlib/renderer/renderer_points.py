# pip imports
import typing
import matplotlib.axes
import matplotlib.collections
import matplotlib.artist

# local imports
from gsp.core.camera import Camera
from gsp.visuals.points import Points
from gsp.types.transbuf_utils import TransBufUtils
from gsp.types.transbuf import TransBuf
from .renderer import MatplotlibRenderer
from ..extra.bufferx import Bufferx


class RendererPoints:
    @staticmethod
    def render(
        renderer: MatplotlibRenderer,
        axes: matplotlib.axes.Axes,
        visual: Points,
        model_matrix: TransBuf,
        camera: Camera,
    ) -> list[matplotlib.artist.Artist]:
        points: Points = visual

        # =============================================================================
        # Create the artists if needed
        # =============================================================================

        if points.uuid not in renderer._artists:
            mpl_path_collection = axes.scatter([], [])  # type: ignore
            mpl_path_collection.set_visible(False)  # hide until properly positioned and sized
            renderer._artists[points.uuid] = mpl_path_collection
            axes.add_artist(mpl_path_collection)

        # =============================================================================
        # Get existing artists
        # =============================================================================

        positions_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(points.positions))
        # sanity check
        assert positions_numpy.shape[1] == 3, "Positions must have shape (N, 3)"
        # TODO
        positions_2d = positions_numpy[:, :2]  # drop z-coordinate for 2D rendering

        sizes_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(points.sizes))
        if sizes_numpy.ndim == 2 and sizes_numpy.shape[1] == 1:
            sizes_numpy = sizes_numpy[:, 0]  # flatten to 1D array

        assert sizes_numpy.ndim == 1, "Sizes must be a 1D array"

        face_colors_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(points.face_colors)) / 255.0  # normalize to [0, 1] range
        edge_colors_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(points.edge_colors)) / 255.0  # normalize to [0, 1] range
        edge_widths_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(points.edge_widths)).flatten()

        # =============================================================================
        # Create the artists if needed
        # =============================================================================

        if points.uuid not in renderer._artists:
            mpl_path_collection = axes.scatter([], [])  # type: ignore
            mpl_path_collection.set_visible(False)
            # hide until properly positioned and sized
            renderer._artists[points.uuid] = mpl_path_collection
            axes.add_artist(mpl_path_collection)

        # =============================================================================
        # Get existing artists
        # =============================================================================

        mpl_path_collection = typing.cast(matplotlib.collections.PathCollection, renderer._artists[points.uuid])
        mpl_path_collection.set_visible(True)

        # =============================================================================
        # Update artists
        # =============================================================================

        mpl_path_collection.set_offsets(offsets=positions_2d)
        mpl_path_collection.set_sizes(typing.cast(list, sizes_numpy))
        mpl_path_collection.set_facecolor(typing.cast(list, face_colors_numpy))
        mpl_path_collection.set_edgecolor(typing.cast(list, edge_colors_numpy))
        mpl_path_collection.set_linewidth(typing.cast(list, edge_widths_numpy))

        # Return the list of artists created/updated
        return [mpl_path_collection]
