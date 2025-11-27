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
    res = ' '.join(format(ord(x), 'b') for x in text)
    return res

def splitBinary(text):
    """
    Pad each character's binary vector with zeros to make required length (12).

    Args:
        text: Binary values of characters separated by spaces

    Returns:
        padded_vectors: Padded vectors of length 12
        addedZeros: Counts of added zeros for each vector
    """
    splitList = []
    addedZeros = []

    for binary_value in text:
            integer = binary_value
            for _ in range(12 - len(binary_value)):
                integer = integer + "0"
            addedZeros.append(12 - len(binary_value))
            splitList.append(int(integer))
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
    ascii_string = ""
    receivedVectors = []

    # If vectors are length 23 (encoded), take only first 12 bits
    if len(binaryVectors[0]) == 23:
        for j in range(len(binaryVectors)):
            receivedVectors.append(binaryVectors[j][0:12])
    # If vectors are already length 12, use as is
    elif len(binaryVectors[0]) == 12:
        receivedVectors = binaryVectors

    # Convert each binary vector back to ASCII character
    for i in range(len(receivedVectors)):
        # Remove the padded zeros
        cutZeros = receivedVectors[i][0:len(receivedVectors[i]) - addedZeros[i]]
        
        s = [str(i) for i in cutZeros] 
        joinedInt = int("".join(s), 2) 

        ascii_character = chr(joinedInt)
        ascii_string += ascii_character
    return ascii_string

def formatBinaryForPicture(binaryVectors, addedZeros, height, width):
    """
    Format binary vectors for image reconstruction.

    Args:
        binaryVectors: Binary vectors to format
        addedZeros: Counts of added zeros for each vector
        len1: Number of rows in original image
        len2: Number of columns in original image

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

    # Reshape into 2D array according to image dimensions
    # Make sure we have exactly height * width elements
    total_pixels_needed = height * width
    
    if len(intVect) < total_pixels_needed:
        # Pad with zeros if we don't have enough pixels
        intVect.extend([0] * (total_pixels_needed - len(intVect)))
    elif len(intVect) > total_pixels_needed:
        # Truncate if we have too many pixels
        intVect = intVect[:total_pixels_needed]
    
    # Reshape to exact dimensions
    finalList = []
    for i in range(height):
        start_idx = i * width
        end_idx = start_idx + width
        row = intVect[start_idx:end_idx]
        finalList.append(row)
    
    return finalList