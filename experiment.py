import random
import matplotlib.pyplot as plt
import encoding as en
import decoding as de

def generate_random_vectors(num_vectors, length=12):
    """Generate random binary vectors of given length."""
    return [[random.randint(0, 1) for _ in range(length)] for _ in range(num_vectors)]

def test_success_rate(p, num_vectors=10000):
    """Test the success rate of error correction for a given p."""
    vectors = generate_random_vectors(num_vectors)

    # Without coding: success if no errors in first 12 bits
    success_without_code = 0
    for orig in vectors:
        transmitted = en.transmit(orig, p)
        if orig == transmitted:  # Compare the entire vector
            success_without_code += 1

    # With coding: encode, transmit, decode, and compare
    success_with_code = 0
    for orig in vectors:
        encoded = en.encode(orig)
        transmitted = en.transmit(encoded, p)
        decoded = de.decode(transmitted)
        if decoded is not None and decoded == orig:
            success_with_code += 1

    return success_without_code / num_vectors * 100, success_with_code / num_vectors * 100

def run_experiment():
    """Run the experiment for p from 0 to 0.5 in 0.05 intervals."""
    p_values = [i * 0.05 for i in range(11)]
    success_without_code = []
    success_with_code = []

    for p in p_values:
        without, with_code = test_success_rate(p)
        success_without_code.append(without)
        success_with_code.append(with_code)
        print(f"p = {p:.2f}: Without code = {without:.2f}%, With code = {with_code:.2f}%")

    plot_results(p_values, success_without_code, success_with_code)

def plot_results(p_values, success_without_code, success_with_code):
    """Plot the success rates."""
    plt.plot(p_values, success_without_code, label="Be kodo", marker='o')
    plt.plot(p_values, success_with_code, label="Su kodu", marker='o')
    plt.xlabel("Klaidos tikimybė p")
    plt.ylabel("Sėkmingai atstatytų vektorių (%)")
    plt.title("Dekodavimo tikslumas priklausomai nuo p (10,000 testų)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_experiment()
