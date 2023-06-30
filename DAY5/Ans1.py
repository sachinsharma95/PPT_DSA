def convert_1d_to_2d(original, m, n):
    total_elements = m * n
    if len(original) != total_elements:
        return []

    return [original[i*n:(i+1)*n] for i in range(m)]

# Example 1:
original = [1, 2, 3, 4]
m = 2
n = 2
result = convert_1d_to_2d(original, m, n)
print(result)
