def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Get input from user
n_terms = int(input("Enter the number of terms: "))
fib_seq = fibonacci_sequence(n_terms)
print("Fibonacci sequence up to", n_terms, "terms:", fib_seq)