def buddyStrings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    if s == goal:
        # Check if s has any repeated characters
        return len(set(s)) < len(s)

    mismatched_pairs = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            mismatched_pairs.append((s[i], goal[i]))
            if len(mismatched_pairs) > 2:
                return False

    return len(mismatched_pairs) == 2 and mismatched_pairs[0] == mismatched_pairs[1][::-1]


# drive code
s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)  # Output: True
