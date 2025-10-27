# pip imports
import typing
import matplotlib.axes
import matplotlib.collections
import matplotlib.artist
import numpy as np

# local imports
from gsp.core.camera import Camera
from gsp.visuals.points import Points
from gsp.types.transbuf_utils import TransBufUtils
from gsp_matplotlib.renderer.renderer import MatplotlibRenderer

class RendererPoints:
    @staticmethod
    def render(renderer: MatplotlibRenderer, axes: matplotlib.axes.Axes, visual: Points, camera: Camera) -> list[matplotlib.artist.Artist]:
        pixels: Points = visual

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

        positions_np = TransBufUtils.to_buffer(pixels.positions).to_numpy()
        # sanity check
        assert positions_np.shape[1] == 3, "Positions must have shape (N, 3)"
        # TODO 
        positions_2d = positions_np[:, :2]  # drop z-coordinate for 2D rendering


        sizes_np = TransBufUtils.to_buffer(pixels.sizes).to_numpy()
        if sizes_np.ndim == 2 and sizes_np.shape[1] == 1:
            sizes_np = sizes_np[:, 0]  # flatten to 1D array
            
        assert sizes_np.ndim == 1, "Sizes must be a 1D array"

        face_colors_np = TransBufUtils.to_buffer(pixels.face_colors).to_numpy()/ 255.0  # normalize to [0, 1] range
        edge_colors_np = TransBufUtils.to_buffer(pixels.edge_colors).to_numpy()/ 255.0  # normalize to [0, 1] range
        edge_widths_np = TransBufUtils.to_buffer(pixels.edge_widths).to_numpy().flatten()

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

        mpl_path_collection = typing.cast(matplotlib.collections.PathCollection, renderer._artists[pixels.uuid])
        mpl_path_collection.set_visible(True)

        # =============================================================================
        # Update artists
        # =============================================================================

        mpl_path_collection.set_offsets(offsets=positions_2d)
        mpl_path_collection.set_sizes(typing.cast(list, sizes_np))
        mpl_path_collection.set_facecolor(typing.cast(list, face_colors_np))
        mpl_path_collection.set_edgecolor(typing.cast(list, edge_colors_np))
        mpl_path_collection.set_linewidth(typing.cast(list, edge_widths_np))

        # Return the list of artists created/updated
        return [mpl_path_collection]


        