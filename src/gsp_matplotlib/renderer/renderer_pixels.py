# pip imports
import typing
import matplotlib.axes
import matplotlib.collections
import matplotlib.artist

# local imports
from gsp.core.camera import Camera
from gsp.utils.group_utils import GroupUtils
from gsp.visuals.pixels import Pixels
from gsp.utils.transbuf_utils import TransBufUtils
from gsp.utils.math_utils import MathUtils
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
        # Transform vertices with MVP matrix
        # =============================================================================

        # convert all necessary buffers to numpy arrays
        vertices_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(pixels.get_positions()))
        model_matrix_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(model_matrix)).squeeze()
        view_matrix_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(camera.get_view_matrix())).squeeze()
        projection_matrix_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(camera.get_projection_matrix())).squeeze()

        # Apply Model-View-Projection transformation to the vertices
        vertices_3d_transformed = MathUtils.apply_mvp_to_vertices(vertices_numpy, model_matrix_numpy, view_matrix_numpy, projection_matrix_numpy)

        # Convert 3D vertices to 2D - shape (N, 2)
        vertices_2d = vertices_3d_transformed[:, :2]

        colors_numpy = Bufferx.to_numpy(TransBufUtils.to_buffer(pixels._colors)) / 255.0  # normalize to [0, 1] range

        # =============================================================================
        #   Compute indices_per_group for groups depending on the type of groups
        # =============================================================================

        indices_per_group = GroupUtils.compute_indices_per_group(vertices_numpy.__len__(), pixels._groups)
        group_count = len(indices_per_group)

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

            for group_index in range(group_count):
                mpl_path_collection = axes.scatter([], [], s=size, marker="o")
                mpl_path_collection.set_antialiased(True)
                mpl_path_collection.set_linewidth(0)
                mpl_path_collection.set_visible(False)
                # hide until properly positioned and sized
                group_uuid = f"{pixels.uuid}_group_{group_index}"
                renderer._artists[group_uuid] = mpl_path_collection
                axes.add_artist(mpl_path_collection)

        # =============================================================================
        # Update matplotlib for each group
        # =============================================================================

        changed_artists: list[matplotlib.artist.Artist] = []
        for group_index in range(group_count):
            group_uuid = f"{pixels.uuid}_group_{group_index}"

            # =============================================================================
            # Get existing artists
            # =============================================================================

            mpl_path_collection = typing.cast(matplotlib.collections.PathCollection, renderer._artists[group_uuid])
            mpl_path_collection.set_visible(True)
            changed_artists.append(mpl_path_collection)

            # =============================================================================
            # Update artists
            # =============================================================================

            mpl_path_collection.set_offsets(offsets=vertices_2d[indices_per_group[group_index]])
            mpl_path_collection.set_facecolor(typing.cast(list, colors_numpy[group_index]))

        # Return the list of artists created/updated
        return changed_artists
