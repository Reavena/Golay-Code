import functions as f
import data as d


def extend_to_24_bits(codeword):
    """
    Extend the codeword to 24 bits by appending a bit to make the total number of 1s odd.

    Args:
        codeword: Input binary vector of length 23.

    Returns:
        Extended binary vector of length 24.
        
    Raises:
        ValueError: If the input codeword is not of length 23.
    """
    # Check if the length of the codeword is 23
    if len(codeword) != 23:
        raise ValueError("Input codeword must be of length 23.")


    num_ones = sum(codeword)

    if num_ones % 2 == 0:
        extended_bit = 1
    else:
        extended_bit = 0

    # Append the bit to the codeword
    [extended_codeword] = [codeword + [extended_bit]]

    return extended_codeword

def find_errors(w):
    """
    This function calculates the syndrome of the received word and attempts to find an error pattern.
    Following the standard  decoding algorithm for the extended Golay code.

    Args:
        w: Received extended word (binary vector of length 24).

    Returns:
        Error pattern vector of length 24 if errors are found.
        Returns None if errors cannot be determined and retransmission is needed.
    """

    # 1: Compute the syndrome s = wH 
    s = f.multiply_matrices([w] , d.H)[0] 

    # 2: If wt(s) ≤ 3, then u = [s, 0]
    if  sum(s) <= 3: 
        u1 = s
        u2 = [0]*12
        u = u1 + u2
        return u
    
    # 3: If wt(s + b_i) ≤ 2 for some row b_i of B, then u = [s + b_i, e_i]
    for i in range(len(d.B12)):
        s_plus_b_i = f.add_matrices([s], [d.B12[i]])[0]        

        if sum(s_plus_b_i) <= 2:          
            u1 = s_plus_b_i
            u2 = [0]*12
            u2[i] = 1                        

            u = u1 + u2
            return u
    
    # 4: Compute the second syndrome sB mod 2
    sB = f.multiply_matrices([s] , d.B12)[0]

    # 5: If wt(sB) ≤ 3, then u = [0, sB]
    if  sum(sB) <= 3:
        u1 = [0]*12
        u2 = sB
        u = u1+ u2
        return u
    
    # 6: If wt(sB + b_i) ≤ 2 for some row b_i of B, then u = [e_i, sB + b_i]
    for i in range(len(d.B12)):
        s_plus_b_i = f.add_matrices([sB], [d.B12[i]])[0]


        if sum(s_plus_b_i) <= 2:       
            u1 = [0]*12 
            u2 = s_plus_b_i
            u1[i] = 1                        

            u = u1 + u2
            return u   

    # 7: If u is not yet determined then request retransmission
    return None

def decode(codeword):
    """
    Decodes a received codeword using the extended Golay code error correction algorithm.

    This function extends the codeword to 24 bits, finds and corrects errors if possible,
    and returns the first 12 bits of the corrected codeword.

    Args:
        Received codeword (binary vector of length 23).

    Returns:
        Decoded 12-bit binary vector if successful.
        Returns None if decoding fails and retransmission is needed.
    """
    w = extend_to_24_bits(codeword)
    # print("Extended vector:", w)

    u = find_errors(w)
    if u is None:
        return None

    v = f.add_matrices([w] , [u])[0]

    #  print("Corrected vector:", v)
    return v[:12]