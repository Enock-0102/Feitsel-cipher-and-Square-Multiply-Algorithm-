def square_and_multiply(x, b, n):
    y = 1
    z = x
    binary_b = bin(b)[2:][::-1]  # Convert b to binary and reverse it
    for bit in binary_b:
        if bit == '1':
            y = (y * z) % n
        z = (z * z) % n
    return y

# Example usage
x = 5
b = 3
n = 13
result = square_and_multiply(x, b, n)
print(result)
