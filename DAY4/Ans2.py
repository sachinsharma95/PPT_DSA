def find_disjoint_elements(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
  
    result = [list(set1 - set2), list(set2 - set1)]
    
    return result



nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

result = find_disjoint_elements(nums1, nums2)
print(result)



