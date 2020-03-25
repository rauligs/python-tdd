import struct
import os


class TestFiles:

    # Text files: unicode encoding and decoding automatically when writing and reading data.
    # Encoding can be specified as extra parameter, also the file can be read as 'rb' and
    # decode it manually
    def test_text_file_create_check_destroy(self):
        data_file = open('data.txt', 'w')  # Output mode ('w' is write). 'r' is default
        data_file.write('Hello\n')
        data_file.write('world\n')
        data_file.close() # Flush output buffers to disk
        text = open('data.txt').read()  # Read all into a string
        assert text == 'Hello\nworld\n'
        os.remove('data.txt')

    def test_text_file_read_line_by_line(self):
        idx_line = 1
        # The best way to read a file is to not read it at all.
        # Files provide an iterator that automatically reads line by line in for loops
        # and other contexts (this way to test is just to show verify the example, don't test
        # this way for real! not in a loop or conditionals):
        for line in open('test_data_types_file.txt'):
            if idx_line == 1:
                assert line == 'Hello\n'
                idx_line += 1
            else:
                assert line == 'world\n'

    # Binary files represent content as a special bytes string and allow you to access file content unaltered
    def test_binary_file_create_check_destroy(self):
        # https://docs.python.org/3.8/library/struct.html
        packed = struct.pack('>i4sh', 7, b'spam', 8)
        data_file = open('data.bin', 'wb')  # Output mode write binary
        data_file.write(packed)
        data_file.close()
        data = open('data.bin', 'rb').read()
        # Sequence of bytes
        assert list(data) == [0, 0, 0, 7, 115, 112, 97, 109, 0, 8]
        assert struct.unpack('>i4sh', data) == (7, b'spam', 8)
        os.remove('data.bin')

# Other file-like tools includes pipes, FIFOs, sockets, keyed-access files, persistent object shelves,
# descriptor-based files, relational and object-oriented database interfaces, and more.
