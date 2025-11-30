import numpy as np
from PIL import Image
import formatting as formatter
import encoding as en
import decoding as de

def process_image():
    print("\n=== Image Processing ===")

    # Ask for filename
    filename = input("Enter image filename: ")

    # Check probability
    try:
        p_input = input("Enter error probability p: ")
        if "," in p_input:
            p = float(p_input.replace(',', '.'))
        else:
            p = float(p_input)
    except ValueError:
        print("Error: Invalid probability value")
        return

    # Load and process image
    try:
        load = Image.open(filename).convert('L')
        data = np.array(load)

        print(f"Image loaded: {filename}")
        print(f"Image size: {data.shape}")

        # Show original image
        print("\nOriginal image:")
        load.show()

        pictureArrayBinary = []
        arrayBinary = []

        for i in range(len(data)):
            row = []
            for j in range(len(data[i])):
                a = bin(data[i][j])[2:]
                row.append(a)
                arrayBinary.append(a)
            pictureArrayBinary.append(row)

        len1 = len(pictureArrayBinary)
        len2 = len(pictureArrayBinary[0])
        padded_vectors, added_zeros = formatter.splitBinary(arrayBinary)

        # Process without coding
        process_without_coding(padded_vectors, added_zeros, p, len1, len2, formatter)

        # Process with coding
        process_with_coding(padded_vectors, added_zeros, p, len1, len2, formatter)

    except Exception as e:
        print(f"Error: {e}")

def process_without_coding(padded_vectors, added_zeros, p, len1, len2, formatter):
    print("\n--- Without coding ---")

    received = []
    for vekt in padded_vectors:
        vekt_list = [int(d) for d in str(vekt)]
        received_vect = en.transmit(np.array(vekt_list, dtype=int), p)
        received.append(received_vect)

    array = np.array(formatter.formatBinaryForPicture(received, added_zeros, len1, len2), dtype=np.uint8)
    pil_image = Image.fromarray(array)
    pil_image.save("image_no_code.bmp")
    print("Saved: image_no_code.bmp")
    pil_image.show()

def process_with_coding(padded_vectors, added_zeros, p, len1, len2, formatter):
    print("\n--- With coding ---")

    encoded_list = []
    received_list = []
    decoded_list = []

    for vekt in padded_vectors:
        vekt_list = [int(d) for d in str(vekt)]

        # Pad to 12 bits if needed
        if vekt == 0:
            vekt_list.extend([0,0,0,0,0,0,0,0,0,0,0])

        # Encode
        encoded_vector = en.encode(np.array(vekt_list, dtype=int))
        encoded_list.append(encoded_vector)

        # Transmit
        received_vector = en.transmit(encoded_vector, p)
        received_list.append(received_vector)

        # Decode
        decoded_vector = de.decode(received_vector)
        decoded_list.append(decoded_vector)

    array = np.array(formatter.formatBinaryForPicture(decoded_list, added_zeros, len1, len2), dtype=np.uint8)
    pil_image = Image.fromarray(array)
    pil_image.save("image_with_code.bmp")
    print("Saved: image_with_code.bmp")
    pil_image.show()
