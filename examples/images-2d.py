import gsp_n as gsp
from gsp_n import Constants, BufferType, Buffer, Texture2D, Images, Camera, MatplotlibRenderer, Canvas, Viewport, Mat4, DataSource
import numpy as np


def main():
    # Create a canvas
    canvas = Canvas(800, 600, 96.0)

    # Create a viewport and add it to the canvas
    viewport = Viewport(400, 300)
    canvas.add(viewport)

    # =============================================================================
    # Add an image + example of DataSource to Buffer conversion
    # =============================================================================
    # texture
    texture_buffer = DataSource("path/to/your/image.png").to_buffer(gsp.BufferType.uint8)
    texture = Texture2D(texture_buffer)

    positions_buffer = Buffer.from_numpy(np.array([[100.0, 100.0, 0.0]], dtype=np.float32))
    sizes_buffer = Buffer.from_numpy(np.array([[200.0, 150.0]], dtype=np.float32))
    axis_buffer = Buffer.from_numpy(np.array([[0.0, 0.0, 1.0]], dtype=np.float32))
    angles_buffer = Buffer.from_numpy(np.array([np.pi / 4], dtype=np.float32))
    groups_buffer = Buffer.from_numpy(np.array([1], dtype=np.uint32))
    images = Images(positions_buffer, sizes_buffer, axis_buffer, angles_buffer, [texture], groups_buffer)
    viewport.add(images)

    # =============================================================================
    # Render the canvas
    # =============================================================================
    # Create a camera
    view_matrix = Mat4()
    projection_matrix = Mat4([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, -0.1], [0, 0, -1, 0]])
    camera = Camera(view_matrix, projection_matrix)

    # Create a renderer and render the scene
    matplotlibRenderer = MatplotlibRenderer(canvas)
    matplotlibRenderer.render([images], [camera])


if __name__ == "__main__":
    main()
