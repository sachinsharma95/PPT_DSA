
# Question2 
"""

Given a string num which represents an integer, return true *if* num *is a strobogrammatic number.

A strobogrammatic numberis a number that looks the same when rotated 180 degrees (looked at upside down).

**Example 1:**

**Input:** num = "69"

**Output:**

true

"""
# solution 


def is_strobogrammatic(num):
    # Define a dictionary for the strobogrammatic pairs
    strob_pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    # Initialize pointers at the beginning and end of the number
    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in strob_pairs or num[right] not in strob_pairs:
            return False

        # Check if the pair is a strobogrammatic pair
        if strob_pairs[num[left]] != num[right]:
            return False

        # Move the pointers inward
        left += 1
        right -= 1

    return True

# drover code and the given Example

num = "69"
print(is_strobogrammatic(num))  # Output: True
