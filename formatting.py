import numpy as np
import random

def findDifferences(original, modified):
    """
    Find differences between original and modified vectors.

    Args:
        original: Original binary vector
        modified: Modified binary vector

    Returns:
        Array of indices where elements don't match
    """
    orig_array = np.array(original).flatten()
    mod_array = np.array(modified).flatten()
    
    return np.where(orig_array != mod_array)[0].tolist()

def stringToBinary(text):
    """
    Convert text string to binary code.

    Args:
        text: Input text string

    Returns:
        Binary values of characters separated by spaces
    """
    bin = ' '.join(format(ord(x), 'b') for x in text) 
    return bin

def splitBinary(text):
    """
    Pad each character's binary vector with zeros to make required length (12).

    Args:
        text: Binary values of characters separated by spaces

    Returns:
        splitList: Padded vectors of length 12
        addedZeros: Counts of added zeros for each vector
    """
    splitList = []
    addedZeros = []

    for binary_value in text:
        padded = binary_value + "0" * (12 - len(binary_value))
        addedZeros.append(12 - len(binary_value))
        splitList.append(int(padded))

    return splitList, addedZeros

def binaryToString(binaryVectors, addedZeros):
    """
    Convert binary vectors back to ASCII characters.

    Args:
        binaryVectors: Padded binary vectors
        addedZeros: Counts of added zeros for each vector

    Returns:
        Decoded text string
    """
    
    vectors = []

    # If vectors are length 23 (encoded), take only first 12 bits
    if len(binaryVectors[0]) == 23:
        vectors = [vec[:12] for vec in binaryVectors]
    else:
        vectors = binaryVectors


    string = []
    for vec, zeros in zip(vectors, addedZeros):
        #Remove padding zeros
        cutZeros = vec[:len(vec) - zeros]  
        # Convert list of bits to string
        bit_string = "".join(map(str, cutZeros))  
        # Convert binary string to integer
        char_int = int(bit_string, 2)  
        # Convert integer to ASCII character and add to list
        string.append(chr(char_int))

    # Combine all characters into final string
    return "".join(string)


def formatBinaryPicture(binaryVectors, addedZeros, height, width):
    """
    Format binary vectors for image reconstruction.

    Args:
        binaryVectors: Binary vectors to format
        addedZeros: Counts of added zeros for each vector
        height: Number of rows in original image
        width: Number of columns in original image

    Returns:
        Formatted list of coordinates for image reconstruction
    """
    receivedVectors = []
    intVect = []

    # If vectors are length 23 (encoded), take only first 12 bits
    if len(binaryVectors[0]) == 23:
        for j in range(len(binaryVectors)):
            receivedVectors.append(binaryVectors[j][0:12])
    # If vectors are already length 12, use as is
    elif len(binaryVectors[0]) == 12:
        receivedVectors = binaryVectors

    # Convert binary vectors to integers
    for i in range(len(receivedVectors)):
        # Remove the padded zeros
        cutZeros = receivedVectors[i][0:len(receivedVectors[i]) - addedZeros[i]]
        
        if len(cutZeros) == 0:
            joinedInt = 0
        else:
            s = [str(bit) for bit in cutZeros] 
            joinedInt = int("".join(s), 2) 
        intVect.append(joinedInt)

    
    # Make from 1d to 2d list
    imageRows = [] # 2d list with rows of the image
    for i in range(height):
        #Calculates the start and end indices in the 1d list (intVect) for the current row.
        start = i * width
        end = start + width
        row = intVect[start:end]
        
        imageRows.append(row)
    
    return imageRows