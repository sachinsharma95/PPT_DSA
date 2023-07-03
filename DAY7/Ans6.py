def can_shift_string(s, goal):
    if len(s) != len(goal):
        return False

    s_double = s + s

    return goal in s_double

# Example usage: in the driver code 
s = "abcde"
goal = "cdeab"
print(can_shift_string(s, goal))  # Output: True
