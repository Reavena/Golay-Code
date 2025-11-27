import numpy as np
import data as d

def binary_symmetric_channel(vector, p):
    """
    Simulate a binary symmetric channel with error probability p.

    Args:
        vector: Input binary vector (numpy array)
        p: Error probability (0 <= p <= 1).

    Returns:
        Errored vector after passing through the channel.
    """
    errors = np.random.rand(len(vector)) < p
    print("Errors:", errors, errors.sum())
    errored_vector = np.logical_xor(vector, errors).astype(int)
    return errored_vector

def encode(vector, p):
    """
    Encode by passing the vector through a binary symmetric channel with error probability p,
    then multiply the errored vector by the generator matrix G.

    Args:
        vector: Input binary vector (len 12)
        G: Generator matrix (numpy array).
        p: Error probability (0 <= p <= 1).

    Returns:
        Result of the errored vector multiplied by G (mod 2 for binary).
    """

    if len(vector) > 12:
        raise ValueError("Input vector must be of length 12 or less.")

    if len(vector) < 12:
        vector = np.pad(vector, (0, 12 - len(vector)), 'constant')

    errored_vector = binary_symmetric_channel(vector, p)
    print("Errored vector:   ", errored_vector)
    result = (errored_vector @ d.G) % 2

    return result
