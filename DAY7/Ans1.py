def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    char_mapping = {}
    mapped_chars = set()

    for i in range(len(s)):
        char_s, char_t = s[i], t[i]

        if char_s in char_mapping:
            if char_mapping[char_s] != char_t:
                return False
        else:
            if char_t in mapped_chars:
                return False
            char_mapping[char_s] = char_t
            mapped_chars.add(char_t)

    return True

# Example usage:
s = "egg"
t = "add"
print(is_isomorphic(s, t))  # Output: True
