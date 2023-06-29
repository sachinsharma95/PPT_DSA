def sorted_squares(nums):
    result = []

    for num in nums:
        result.append(num * num)

    result.sort()

    return result


# driver code

nums = [-4, -1, 0, 3, 10]

result = sorted_squares(nums) # function call

print(result)
