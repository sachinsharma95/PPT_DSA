
def findOriginalArray(changed):

		if len(changed) % 2 != 0:
			return []

		changed = sorted(changed)

		result = []
		d = {}

		for i in changed:
			if i not in d:
				d[i] = 1
			else:
				d[i] = d[i] + 1

		for num in changed:
			double  = num * 2

			if num in d and double in d:

				if num == 0 and d[num] >= 2:
					d[num] = d[num] - 2
					result.append(num)

				elif num > 0 and d[num] and d[double]:
					d[num] = d[num] - 1
					d[double] = d[double] - 1

					result.append(num)

		if len(changed) // 2 == len(result):
			return result
		else:
			return []

# Example 1:
changed = [1, 3, 4, 2, 6, 8]
output = findOriginalArray(changed)
print(output)  # Output: [1, 3, 4]
