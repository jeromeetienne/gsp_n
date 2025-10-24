# local imports
from gsp.core import Buffer, BufferType


def main():
    buffer = Buffer(10, BufferType.uint32)
    print("Buffer created:", buffer)

    # create a bytearray of 40 bytes (10 uint32)
    byte_array = bytearray(b'\x00\x00\x00\x00' * 10)

    # Set data
    buffer.set_data(bytearray(b'\x00\x00\x00\x22' * 2), 0, 2)
    print("Buffer data set.")

    # Get data
    new_buffer = buffer.get_data(0, 5)
    print("New buffer created from existing buffer:", new_buffer)
    print(f"New buffer count: {new_buffer.get_count()}")


if __name__ == "__main__":
    main()