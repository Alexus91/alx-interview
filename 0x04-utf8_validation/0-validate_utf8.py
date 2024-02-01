#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """ Function to check if a byte starts with '10' """
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):

        if (data[i] & 0b10000000) == 0:
            length = 1
        elif (data[i] & 0b11100000) == 0b11000000:
            length = 2
        elif (data[i] & 0b11110000) == 0b11100000:
            length = 3
        elif (data[i] & 0b11111000) == 0b11110000:
            length = 4
        else:
            return False

        for j in range(i + 1, i + length):
            if j >= len(data) or not is_continuation(data[j]):
                return False
        i += length

    return True
