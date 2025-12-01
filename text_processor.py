import formatting as formatter
import encoding as en
import decoding as de

def process_text():
    print("\n=== Text Processing ===")
    print("Enter text (press Enter twice to finish):")
    
    lines = []
    while True:
        line = input()
        if line == "":  # Empty line means user pressed Enter twice
            break
        lines.append(line)
    
    text = '\n'.join(lines)
    
    # Check if probability is correct
    try:
        p_input = input("Enter error probability p (0.0-1.0): ")
        if "," in p_input:
            p = float(p_input.replace(',', '.'))
        else:
            p = float(p_input)
    except ValueError:
        print("Error: Invalid probability value")
        return

    split_vectors, added_zeros = formatter.splitBinary(formatter.stringToBinary(text).split())

    without_coding(split_vectors, added_zeros, p)
    with_coding(split_vectors, added_zeros, p)

def without_coding(split_vectors, added_zeros, p):
    print("\n--- Without coding ---")
    
    received = []
    for vekt in split_vectors:
        vekt_list = [int(d) for d in str(vekt)]
        received_vect = en.transmit(vekt_list, p)
        received.append(received_vect)
    
    result = formatter.binaryToString(received, added_zeros)
    print("Decoded text without coding:")
    print(f"'{result}'")
    return result

def with_coding(split_vectors, added_zeros, p):
    print("\n--- With coding ---")
    
    decoded_list = []
    
    for vekt in split_vectors:
        vekt_list = [int(d) for d in str(vekt)]
        
        # Encode
        encoded_vector = en.encode(vekt_list)
        
        # Transmit
        received_vector= en.transmit(encoded_vector, p)
        
        # Decode
        decoded_vector = de.decode(received_vector)
        decoded_list.append(decoded_vector)
    
    result = formatter.binaryToString(decoded_list, added_zeros)
    print("Decoded text with coding:")
    print(f"'{result}'")
    return result