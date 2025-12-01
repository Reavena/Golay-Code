import random
import encoding as en
import decoding as de
import functions as f
import data as d

def flip_bits(vector, num_errors):
    """Flip num_errors bits randomly in the vector."""
    vector = vector.copy()
    indices = random.sample(range(len(vector)), num_errors)
    for idx in indices:
        vector[idx] = 1 - vector[idx]  # flip 0 <-> 1
    return vector

def run_experiment(num_trials=10, max_errors=3):
    failures = 0

    for trial in range(1, num_trials + 1):
        # Generate random 12-bit vector
        original = [random.randint(0, 1) for _ in range(12)]

        # Encode using your Golay encoder
        codeword = en.encode(original)  # returns list of 23 bits

        # Introduce random errors (0 to max_errors)
        num_errors = random.randint(0, max_errors)
        received = flip_bits(codeword, num_errors)

        # Decode
        decoded = de.decode(received)

        # Check if decoding was successful
        success = decoded == original
        if not success:
            failures += 1
            print(f"Trial {trial}: FAILED")
            print(f"Original: {original}")
            print(f"Received: {received}")
            print(f"Decoded:  {decoded}")
            print(f"Errors introduced: {num_errors}\n")
        else:
            print(f"Trial {trial}: success (errors={num_errors})")

    print(f"\nExperiment complete. Total failures: {failures} out of {num_trials}")

if __name__ == "__main__":
    run_experiment()
