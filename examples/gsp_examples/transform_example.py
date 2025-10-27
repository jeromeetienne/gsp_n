# stdlib imports
import os

# local imports
from gsp.types.buffer import Buffer, BufferType
from gsp.transforms.transform import Transform, TransformAccessor, TransformLink, TransformDataSource


__dirname__  = os.path.dirname(os.path.abspath(__file__))

def main():
    transformChain = Transform()


    image_url = f"file://{__dirname__}/images/image.png"
    transformChain.add(TransformDataSource(image_url, BufferType.uint8))
    transformChain.add(TransformAccessor('r'))

    buffer = transformChain.to_buffer()
    print(buffer)

if __name__ == "__main__":
    main()
