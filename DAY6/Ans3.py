def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False

    # Find the peak element
    peak_idx = 0
    while peak_idx + 1 < n and arr[peak_idx] < arr[peak_idx + 1]:
        peak_idx += 1

    # Check if peak exists and is not at the start or end of the array
    if peak_idx == 0 or peak_idx == n - 1:
        return False

    # Check the ascending part of the array
    for i in range(peak_idx):
        if arr[i] >= arr[i + 1]:
            return False

    # Check the descending part of the array
    for i in range(peak_idx, n - 1):
        if arr[i] <= arr[i + 1]:
            return False

    return True

# Test example
arr = [2, 1]
output = valid_mountain_array(arr)
print(output)  # Output: False
