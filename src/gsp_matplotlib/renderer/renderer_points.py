# pip imports
import typing
import matplotlib.axes
import matplotlib.collections
import matplotlib.artist
import numpy as np

# local imports
from gsp.core.camera import Camera
from gsp.visuals.points import Points
from gsp.utils.transbuf_utils import TransBufUtils
from gsp.types.transbuf import TransBuf
from gsp.types.buffer_type import BufferType
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
        # Get existing artists
        # =============================================================================

        vertices_numpy = Bufferx.to_numpy(TransBufUtils.transbuf_to_buffer(points.positions))

        # Compute the Model-View-Projection (MVP) matrix
        model_matrix_numpy = Bufferx.to_numpy(TransBufUtils.transbuf_to_buffer(model_matrix)).squeeze()
        view_matrix_numpy = Bufferx.to_numpy(TransBufUtils.transbuf_to_buffer(camera.get_view_matrix())).squeeze()
        projection_matrix_numpy = Bufferx.to_numpy(TransBufUtils.transbuf_to_buffer(camera.get_projection_matrix())).squeeze()
        mvp_matrix_numpy = projection_matrix_numpy @ view_matrix_numpy @ model_matrix_numpy

        # convert vertices to homogeneous coordinates (x, y, z) -> (x, y, z, w=1.0)
        ws_column = np.ones((vertices_numpy.shape[0], 1), dtype=np.float32)
        vertices_homogeneous = np.hstack((vertices_numpy, ws_column))  # shape (N, 4) for N vertices

        # Apply the MVP transformation to the vertices
        vertices_transformed = (mvp_matrix_numpy @ vertices_homogeneous.T).T  # shape (N, 4)

        # Perform perspective division to get normalized device coordinates (NDC)
        vertices_homo_transformed = vertices_transformed / vertices_transformed[:, 3:4]  # divide by w - shape (N, 4)
        vertices_3d_transformed = vertices_homo_transformed[:, :3]  # drop w-coordinate - shape (N, 3)

        # NOTE: no need to map NDC to screen coordinates as canvas is drawn directly in NDC coordinates 2d
        pass

        # Convert 3D vertices to 2D - shape (N, 2)
        vertices_2d = vertices_3d_transformed[:, :2]

        # =============================================================================
        # Convert all attributes to numpy arrays
        # =============================================================================

        sizes_numpy = Bufferx.to_numpy(TransBufUtils.transbuf_to_buffer(points.sizes))
        face_colors_numpy = Bufferx.to_numpy(TransBufUtils.transbuf_to_buffer(points.face_colors)) / 255.0  # normalize to [0, 1] range
        edge_colors_numpy = Bufferx.to_numpy(TransBufUtils.transbuf_to_buffer(points.edge_colors)) / 255.0  # normalize to [0, 1] range
        edge_widths_numpy = Bufferx.to_numpy(TransBufUtils.transbuf_to_buffer(points.edge_widths)).flatten()

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

        mpl_path_collection.set_offsets(offsets=vertices_2d)
        mpl_path_collection.set_sizes(typing.cast(list, sizes_numpy))
        mpl_path_collection.set_facecolor(typing.cast(list, face_colors_numpy))
        mpl_path_collection.set_edgecolor(typing.cast(list, edge_colors_numpy))
        mpl_path_collection.set_linewidth(typing.cast(list, edge_widths_numpy))

        # Return the list of artists created/updated
        return [mpl_path_collection]
