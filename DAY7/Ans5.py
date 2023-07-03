def reverse_groups(s, k):
    # Convert the string to a list of characters for easier manipulation
    s = list(s)

    for i in range(0, len(s), 2 * k):
        # Calculate the start and end indices of each group of 2k characters
        start, end = i, min(i + k - 1, len(s) - 1)

        # Reverse the first k characters of the group
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    # Join the list of characters back into a string and return the result
    return "".join(s)

# Example usage:
s = "abcdefg"
k = 2
print(reverse_groups(s, k))  # Output: "bacdfeg"
