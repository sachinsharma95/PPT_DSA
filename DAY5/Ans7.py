def find_min_in_rotated_array(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # If the mid element is greater than the rightmost element,
        # then the inflection point must be in the right half of the array
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # If the mid element is less than or equal to the rightmost element,
            # then the inflection point must be in the left half of the array
            right = mid

    return nums[left]

# Example 1:
# driver code
nums = [3, 4, 5, 1, 2]
output = find_min_in_rotated_array(nums)
print(output)  # Output: 1
