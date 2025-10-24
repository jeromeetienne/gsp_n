import gsp_api as gsp
import numpy as np


def main():
    # Create a canvas
    canvas = gsp.Canvas(800, 600, 96.0)

    # Create a viewport and add it to the canvas
    viewport = gsp.Viewport(400, 300)
    canvas.add(viewport)

    # =============================================================================
    # Add random points
    # - various ways to create Buffers
    # =============================================================================
    point_count = 1024
    # Random positions - Create buffer from numpy array
    positions_buffer = gsp.Buffer.from_numpy(np.random.rand(point_count, 3).astype(np.float32))
    # all pixels red - Create buffer and fill it with a constant
    colors_buffer = gsp.Buffer(point_count, gsp.BufferType.color).fill(gsp.Constants.red)  # Red color
    # one group for all points - create buffer and set value with immediate assignment
    groups_buffer = gsp.Buffer(1, gsp.BufferType.uint32)
    groups_buffer[0] = 1

    pixels = gsp.Pixels(positions_buffer, colors_buffer, groups_buffer)
    viewport.add(pixels)

    # Set the model matrix for the visual
    model_matrix = gsp.Mat4x4.from_numpy(np.eye(4, dtype=np.float32))
    pixels.set_model_matrix(model_matrix)

    # =============================================================================
    # Render the canvas
    # =============================================================================
    # Create a camera
    view_matrix = gsp.Mat4x4()
    projection_matrix = gsp.Mat4x4([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, -0.1], [0, 0, -1, 0]])
    camera = gsp.Camera(view_matrix, projection_matrix)

    # Create a renderer and render the scene
    matplotlibRenderer = gsp.MatplotlibRenderer(canvas)
    matplotlibRenderer.render([pixels], [camera])


if __name__ == "__main__":
    main()
