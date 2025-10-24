import src.gsp_n as gsp
from src.gsp_n import Constants, BufferType, Buffer, Texture2D, Images, Pixels,Camera, MatplotlibRenderer, Canvas, Viewport, Mat4, DataSource
import numpy as np


def main():
    # Create a canvas
    canvas = Canvas(800, 600, 96.0)

    # Create a viewport and add it to the canvas
    viewport = Viewport(400, 300)
    canvas.add(viewport)

    # =============================================================================
    # Add random points
    # - various ways to create Buffers
    # =============================================================================
    point_count = 1024
    # Random positions - Create buffer from numpy array
    positions_buffer = Buffer.from_numpy(np.random.rand(point_count, 3).astype(np.float32))
    # all pixels red - Create buffer and fill it with a constant
    colors_buffer = Buffer(point_count, BufferType.color).fill(gsp.Constants.red)  # Red color
    # one group for all points - create buffer and set value with immediate assignment
    groups_buffer = Buffer(1, BufferType.uint32)
    groups_buffer[0] = 1

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
    projection_matrix = Mat4([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, -0.1], [0, 0, -1, 0]])
    camera = Camera(view_matrix, projection_matrix)

    # Create a renderer and render the scene
    matplotlibRenderer = MatplotlibRenderer(canvas)
    matplotlibRenderer.render([pixels], [camera])


if __name__ == "__main__":
    main()
