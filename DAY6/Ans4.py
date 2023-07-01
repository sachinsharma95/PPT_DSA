def find_max_length(nums):
    max_length = 0
    sum_map = {0: -1}  # Initialize the sum_map with running sum 0 and index -1

    running_sum = 0
    for i in range(len(nums)):
        # Update the running sum based on the value at index i (1 or 0)
        running_sum += 1 if nums[i] == 1 else -1

        if running_sum in sum_map:
            # Calculate the length of the current subarray
            current_length = i - sum_map[running_sum]
            max_length = max(max_length, current_length)
        else:
            # Store the index of the running sum in the hashmap
            sum_map[running_sum] = i

    return max_length

# Test example
nums = [0, 1]
output = find_max_length(nums)
print(output)  # Output: 2
