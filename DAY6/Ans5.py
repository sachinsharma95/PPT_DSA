def min_product_sum(nums1, nums2):
    nums1.sort()  # Sort nums1 in ascending order
    nums2.sort(reverse=True)  # Sort nums2 in descending order

    min_product = sum(nums1[i] * nums2[i] for i in range(len(nums1)))
    return min_product

# Test example
nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
output = min_product_sum(nums1, nums2)
print(output)  # Output: 40
