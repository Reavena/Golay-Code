import numpy as np
from PIL import Image
import formatting as formatter
import encoding as en
import decoding as de
import time


def process_image():
    print("\n=== Image Processing ===")

    # Ask for filename
    filename = input("Enter image filename: ")

    # Check probability
    try:
        p_input = input("Enter error probability p (0.0-1.0) : ")
        if "," in p_input:
            p = float(p_input.replace(',', '.'))
        else:
            p = float(p_input)
    except ValueError:
        print("Error: Invalid probability value")
        return

    # Load and process image
    try:
        load = Image.open(filename).convert('L') #Grayscale
        data = np.array(load)

        print(f"Image loaded: {filename}")
        print(f"Image size: {data.shape}")

        
        # Show original image
        print("\nOriginal image:")
        load.show()


        arrayBinary = []
        #Converts each pixel value to a binary string (without the '0b' prefix).
        #arrayBinary is a 1D list containing all binary strings in a single list.

        for i in range(len(data)):
            row = []
            for j in range(len(data[i])):
                a = bin(data[i][j])[2:]
                row.append(a)
                arrayBinary.append(a)

        rows = data.shape[0]  # Number of rows
        cols = data.shape[1]  # Number of columns
        split_vectors, added_zeros = formatter.splitBinary(arrayBinary)

        
        process_without_coding(split_vectors, added_zeros, p, rows, cols)
        process_with_coding(split_vectors, added_zeros, p, rows, cols)

    except Exception as e:
        print(f"Error: {e}")

def process_without_coding(split_vectors, added_zeros, p, rows, cols):
    print("\n--- Without coding ---")
    start_time = time.time()

    received = []
    for vekt in split_vectors:
        vekt_list = [int(d) for d in str(vekt)]
        received_vect = en.transmit(np.array(vekt_list, dtype=int), p)
        received.append(received_vect)

    array = np.array(formatter.formatBinaryPicture(received, added_zeros, rows, cols), dtype=np.uint8)
    pil_image = Image.fromarray(array)
    pil_image.save("image_no_code.bmp")
    print("Saved: image_no_code.bmp")
    pil_image.show()

    processing_time = time.time() - start_time
    print(f"Processing time: {processing_time:.2f} seconds")

def process_with_coding(split_vectors, added_zeros, p, rows, cols):
    print("\n--- With coding ---")
    start_time = time.time()

    encoded_list = []
    received_list = []
    decoded_list = []

    for vekt in split_vectors:
        vekt_list = [int(d) for d in str(vekt)]

        # Encode
        encoded_vector = en.encode(np.array(vekt_list, dtype=int))
        encoded_list.append(encoded_vector)

        # Transmit
        received_vector = en.transmit(encoded_vector, p)
        received_list.append(received_vector)

        # Decode
        decoded_vector = de.decode(received_vector)
        decoded_list.append(decoded_vector)

    array = np.array(formatter.formatBinaryPicture(decoded_list, added_zeros, rows, cols), dtype=np.uint8)
    pil_image = Image.fromarray(array)
    pil_image.save("image_with_code.bmp")
    print("Saved: image_with_code.bmp")
    pil_image.show()

    processing_time = time.time() - start_time
    print(f"Processing time: {processing_time:.2f} seconds")
