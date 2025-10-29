# pip imports
import numpy as np
import matplotlib.pyplot


# local imports
from gsp.core import Canvas, Viewport, VisualBase
from gsp.visuals import Pixels
from gsp.types import Buffer, BufferType
from gsp.core import Camera
from gsp_matplotlib.renderer import MatplotlibRenderer
from gsp_extra.bufferx import Bufferx
from gsp_extra.visual_twin import VisualTwin


def main():
    # Create a canvas
    canvas = Canvas(100, 100, 96.0)

    # Create a viewport and add it to the canvas
    viewport = Viewport(0, 0, 400, 300)

    # =============================================================================
    # Add random points
    # - various ways to create Buffers
    # =============================================================================
    point_count = 1024
    group_count = 1

    # Random positions - Create buffer from numpy array
    positions_numpy = np.random.rand(point_count, 3).astype(np.float32) * 2.0 - 1
    positions_buffer = Bufferx.from_numpy(positions_numpy, BufferType.vec3)

    # all pixels red - Create buffer and fill it with a constant
    colors_buffer = Buffer(group_count, BufferType.rgba8)
    colors_buffer.set_data(bytearray([255, 0, 0, 255]) * colors_buffer.get_count(), 0, 1)

    # one group for all points - create buffer and set value with immediate assignment
    groups_buffer = Buffer(1, BufferType.uint32)
    groups_buffer.set_data(bytearray((group_count).to_bytes(4, byteorder="big")), 0, 1)

    # Create the Pixels visual and add it to the viewport
    pixels = Pixels(positions_buffer, colors_buffer, groups_buffer)
    pixels_twin = VisualTwin(pixels)

    # =============================================================================
    # Render the canvas
    # =============================================================================

    # Create a camera
    view_matrix = Bufferx.mat4_identity()
    projection_matrix = Buffer(1, BufferType.mat4)
    projection_matrix.set_data(bytearray(np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, -0.1], [0, 0, -1, 0]], dtype=np.float32).tobytes()), 0, 1)
    camera = Camera(view_matrix, projection_matrix)

    # Create a renderer and render the scene
    matplotlibRenderer = MatplotlibRenderer(canvas)
    matplotlibRenderer.render([viewport], [pixels], [pixels_twin.model_matrix], [camera])

    matplotlib.pyplot.show()


if __name__ == "__main__":
    main()
