
import data as d
import random as rand
import functions as f

def transmit(vector, p):
    """
    Simulate a binary symmetric channel with error probability p.
    
    Args:
        vector: Original binary vector. 
        p: Error probability for each bit (0 ≤ p ≤ 1)

    Returns:
        The transmitted vector with errors introduced.
    """
    errored_vector = []
    for bit in vector:
        # Introduce an error with probability p
        if rand.random() < p:
            errored_vector.append(1 - bit)  # flip bit
        else:
            errored_vector.append(bit)
    return errored_vector

def encode(vector):
    """
    Encodes a 12-bit binary vector using the Golay code generator matrix.

    This function pads the input vector with zeros if it is shorter than 12 bits,
    then multiplies it by the generator matrix G to produce a codeword.

    Args:
        Input binary vector of length 12 or less.

    Returns:
        Encoded codeword of length 23.

    Raises:
        ValueError: If the input vector is longer than 12 bits.
    """
    if len(vector) != 12:
        raise ValueError(f"Input vector must be of length 12. Got length: {len(vector)}")


    codeword = f.multiply_matrices([vector], d.G) [0]
    return codeword
