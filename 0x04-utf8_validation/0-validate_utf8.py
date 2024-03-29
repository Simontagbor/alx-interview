#!/usr/bin/python3

""" A module for validating Unicode encodding """


def validUTF8(data):
    """ validate utf-8 encoding for a given data

    Arg:
        data(any) - data to be validated

    Returns:
            bool - true if data is utf-8 encoded.
    """
    n_bytes = 0
    for num in data:
        bin_rep = format(num, '#010b')[-8:]
        if n_bytes == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        n_bytes -= 1
    return n_bytes == 0
