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
        splitList: Padded vectors of length 12
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