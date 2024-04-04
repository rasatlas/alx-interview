#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ A method that determines if a given data set represents
    a valid UTF-8 encoding.
    """
    i = 0
    while i < len(data):
        # Count the number of bytes in the current character
        num_bytes = 0
        mask = 0b10000000
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        # Check if the number of bytes is within the valid range
        if num_bytes < 1 or num_bytes > 4:
            return False

        # Check continuation bytes
        for j in range(1, num_bytes):
            if i + j >= len(data) or (data[i + j] >> 6) != 0b10:
                return False

        i += num_bytes

    return True
