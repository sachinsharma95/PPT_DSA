def solve_rec(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0

    if s1[i] == s2[j]:
        return ord(s1[i]) + solve_rec(s1, s2, i + 1, j + 1)
    else:
        return max(solve_rec(s1, s2, i + 1, j), solve_rec(s1, s2, i, j + 1))

def minimum_delete_sum(s1, s2):
    sum = 0
    for char in s1:
        sum += ord(char)
    for char in s2:
        sum += ord(char)
    return sum - (2 * solve_rec(s1, s2, 0, 0))

# Driver code
s1 = "sea"
s2 = "eat"
result = minimum_delete_sum(s1, s2)
print(result)  # Output: 231
