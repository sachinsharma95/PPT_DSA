def sorted_squares(nums):
    # Square each element and store in a new array
    squared_nums = [num ** 2 for num in nums]

    # Sort the squared array in non-decreasing order
    squared_nums.sort()

    return squared_nums

# Example 1:
nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result)  # Output: [0, 1, 9, 16, 100]
