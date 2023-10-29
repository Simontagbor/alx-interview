#!/bin/usr/python3

""" A module for validating Unicode encodding """


def validUTF8(data):
    """ validate utf-8 encoding for a given data

    Arg:
        data(any) - data to be validated

    Returns:
            bool - true if data is utf-8 encoded.
    """
    bytes_left = 0

    for byte in data:
        byte_bin = format(byte, '08b')

        if bytes_left == 0:
            if byte_bin.startswith('0'):
                bytes_left = 0
            elif byte_bin.startswith('110'):
                bytes_left = 1
            elif byte_bin.startswith('1110'):
                bytes_left = 2
            elif byte_bin.startswith('11110'):
                bytes_left = 3
            else:
                return False
        else:
            if not byte_bin.startswith('10'):
                return False
            bytes_left -= 1

    return bytes_left == 0
