import numpy as np
from gsp.core import Canvas, Viewport
from gsp.visuals import Pixels
from gsp.types import Buffer, BufferType
from gsp.math import Mat4
from gsp.core import Camera
from gsp.renderer.matplotlib.renderer import MatplotlibRenderer


def main():
    # Create a canvas
    canvas = Canvas(800, 600, 96.0)

    # Create a viewport and add it to the canvas
    viewport = Viewport(0, 0, 400, 300)
    canvas.add(viewport)

    # =============================================================================
    # Add random points
    # - various ways to create Buffers
    # =============================================================================
    point_count = 1024
    # Random positions - Create buffer from numpy array
    positions_buffer = Buffer.from_numpy(
        np.random.rand(point_count, 3).astype(np.float32)
    )
    # all pixels red - Create buffer and fill it with a constant
    color_numpy = np.array([255, 0, 0, 255], dtype=np.uint8)
    colors_buffer = Buffer.from_numpy(color_numpy)
    # one group for all points - create buffer and set value with immediate assignment
    groups_buffer = Buffer(1, BufferType.uint32)
    groups_buffer.set_data(bytes(b'\x00\x00\x00\x01'), 0, 1)

    pixels = Pixels(positions_buffer, colors_buffer, groups_buffer)
    viewport.add(pixels)

    # Set the model matrix for the visual
    model_matrix = Mat4.from_numpy(np.eye(4, dtype=np.float32))
    pixels.set_model_matrix(model_matrix)

    # =============================================================================
    # Render the canvas
    # =============================================================================
    # Create a camera
    view_matrix = Mat4()
    projection_matrix = Mat4(
        np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, -0.1], [0, 0, -1, 0]], dtype=np.float32)
    )
    camera = Camera(view_matrix, projection_matrix)

    # Create a renderer and render the scene
    matplotlibRenderer = MatplotlibRenderer(canvas)
    matplotlibRenderer.render([pixels], [camera])


if __name__ == "__main__":
    main()
