import numpy as np
import data as d

def transmit(vector, p):
    """
    Simulate a binary symmetric channel with error probability p.
    """
    errors = np.random.rand(len(vector)) < p
    errored_vector = np.logical_xor(vector, errors).astype(int)
    return errored_vector

def encode(vector):
    """
    Encode a 12-bit vector using Golay code (no transmission)
    """
    if len(vector) > 12:
        raise ValueError(f"Input vector must be of length 12 or less. Got length: {len(vector)}")

    if len(vector) < 12:
        vector = np.pad(vector, (0, 12 - len(vector)), 'constant')

    codeword = (vector @ d.G) % 2
    return codeword
