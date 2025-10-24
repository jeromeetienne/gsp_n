# stdlib imports
import os

# local imports
from gsp.core.buffer import Buffer, BufferType
from gsp.transforms.transform import Transform, TransformLink, TransformDataSource


__dirname__  = os.path.dirname(os.path.abspath(__file__))

def main():
    transformChain = Transform()


    image_url = f"file://{__dirname__}/images/image.png"
    transformChain.add(TransformDataSource(image_url, BufferType.uint8))

    buffer = transformChain.to_buffer()
    print(buffer)

if __name__ == "__main__":
    main()
