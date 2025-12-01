import formatting as formatter
import encoding as en
import decoding as de

def process_vector():
    
    print("\n=== Vector Processing ===")
    vector_str = input("Enter vector (12 bits): ")
    vector_str = vector_str.replace(" ", "")
    p = float(input("Enter error probability p (0.0-1.0): "))
    
    if len(vector_str) != 12 or not all(c in '01' for c in vector_str):
        print("Error: Vector must be 12 bits long and contain only 0s and 1s")
        return
    
    vector = [int(bit) for bit in vector_str]
    print(f"\nOriginal vector: {vector}")
    
    # Encoding (no errors during encoding)
    encoded_vector = en.encode(vector)
    print(f"Encoded vector:  {encoded_vector}")
    
    # Transmission through channel
    received_vector = en.transmit(encoded_vector, p)
    print(f"Received vector: {received_vector}")
    
    # Error detection
    errors = [i for i, (a, b) in enumerate(zip(encoded_vector, received_vector)) if a != b]

    print(f"Number of errors: {len(errors)}")
    print(f"Error positions: {errors}")
    
    # User editing option
    print("\nDo you want to edit the received vector? (y/n)")
    if input().strip().lower() == 'y':
        print("Enter new vector (23 bits): ")
        edited_str = input().replace(" ", "").replace(",", "")  # Remove all spaces and commas
        if len(edited_str) == 23 and all(c in '01' for c in edited_str):
            received_vector = [int(bit) for bit in edited_str]
            print(f"Edited vector: {received_vector}")
            # Recalculate errors
            errors = [i for i, (a, b) in enumerate(zip(encoded_vector, received_vector)) if a != b]
            print(f"New error count: {len(errors)}")
        else:
            print("Error: Invalid vector format")
    
    # Decoding
    decoded_vector = de.decode(received_vector)
    if decoded_vector is not None:
        print(f"Decoded vector: {decoded_vector}")
        success = decoded_vector == vector
        print(f"Decoding success: {success}")
    else:
        print("Decoding failed - retransmission required")