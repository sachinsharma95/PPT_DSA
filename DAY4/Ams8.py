def shuffle_array(nums, n):
    x = nums[:n]
    y = nums[n:]

    result = []

    for i in range(n):
        result.append(x[i])
        result.append(y[i])

    return result


# driver code
nums = [2, 5, 1, 3, 4, 7]
n = 3

result = shuffle_array(nums, n)
print(result)
