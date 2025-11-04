# stdlib imports
import os

# local imports
from gsp.types.buffer import Buffer, BufferType
from gsp.transforms.transform_chain import TransformChain
from gsp.transforms.links.transform_data_source import TransformDataSource
from examples.gsp_examples.gsp_extra.transform_links.transform_link_immediate import TransformLinkImmediate


__dirname__ = os.path.dirname(os.path.abspath(__file__))


def main():
    transformChain = TransformChain(BufferType.uint32)

    image_url = f"file://{__dirname__}/images/image.png"
    image_url = f"file://{__dirname__}/images/UV_Grid_Sm.jpg"
    transformChain.add(TransformDataSource(image_url, BufferType.uint8))
    # transformChain.add(TransformAccessor("r"))

    buffer = transformChain.to_buffer()
    print(buffer)


if __name__ == "__main__":
    main()
