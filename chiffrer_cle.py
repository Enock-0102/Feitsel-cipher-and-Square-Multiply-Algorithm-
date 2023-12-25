def feistel_cipher(block, permutation, key1, key2):
    # Permutation
    permuted_block = [block[i-1] for i in permutation]
    # Split into two 4-bit blocks
    left_block = permuted_block[:4]
    right_block = permuted_block[4:]
    
    # First round
    temp = right_block
    right_block = [left_block[i] ^ key1[i] for i in range(4)]
    left_block = [temp[i] ^ (right_block[i] | key1[i]) for i in range(4)]
    
    # Second round
    temp = right_block
    right_block = [left_block[i] ^ key2[i] for i in range(4)]
    left_block = [temp[i] ^ (right_block[i] | key2[i]) for i in range(4)]
    
    # Concatenate and apply inverse permutation
    output_block = left_block + right_block
    inverse_permutation = [permuted_block.index(i)+1 for i in range(1, 9)]
    encrypted_block = [output_block[i-1] for i in inverse_permutation]
    
    return encrypted_block

# Example usage
block = [1, 0, 1, 0, 0, 1, 1, 0]
permutation = [4, 6, 0, 2, 7, 3, 1, 5]
key1 = [1, 0, 1, 0]
key2 = [0, 1, 1, 0]

encrypted_result = feistel_cipher(block, permutation, key1, key2)
print(encrypted_result)
