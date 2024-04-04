#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """A method that determines if a given data set represents
    a valid UTF-8 encoding.
    """

    """ i = 0
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

    return True """

    num_bytes_to_follow = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if num_bytes_to_follow:
            if byte >> 6 != 0b10:
                return False
            num_bytes_to_follow -= 1
        else:
            # Determine the number of bytes to follow based on the leading bits
            if byte >> 7 == 0:
                continue  # Single-byte character
            elif byte >> 5 == 0b110:
                num_bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                num_bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False  # Invalid leading bits

    return num_bytes_to_follow == 0
