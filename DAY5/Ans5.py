def distance_value(arr1, arr2, d):
    count = 0
    for num1 in arr1:
        has_close_element = False
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                has_close_element = True
                break
        if not has_close_element:
            count += 1
    return count

# Example 1:
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
result = distance_value(arr1, arr2, d)
print(result)  # Output: 2
