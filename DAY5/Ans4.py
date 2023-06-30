def find_missing_elements(nums1, nums2):
    # Convert both arrays to sets
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)

    # Find the distinct elements in nums1 that are not present in nums2
    answer1 = list(set_nums1 - set_nums2)

    # Find the distinct elements in nums2 that are not present in nums1
    answer2 = list(set_nums2 - set_nums1)

    return [answer1, answer2]

# Example 1:
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = find_missing_elements(nums1, nums2)
print(result)  # Output: [[1, 3], [4, 6]]
