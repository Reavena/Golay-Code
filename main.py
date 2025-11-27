import numpy as np
import data as data
import encoding as en
import decoding as de

# Example codeword (12-bit)
codeword = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], dtype=int)

# User-defined error probability
p = 0

print("Original codeword:", codeword)
encoded = en.encode (codeword, p)
print("Result of errored_vector @ G:", encoded)

# Decode the result
decoded_word = de.decoding(encoded)

if decoded_word is not None:
    print("Decoded word:", decoded_word)
else:
    print("Decoding failed. Retransmission requested. Encoding again...")
    encoded = en.encode(codeword, p)
    print("Re-encoded codeword:", encoded)
    decoded_word = de.decoding(encoded)
