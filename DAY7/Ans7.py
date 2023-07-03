def backspace_compare(s, t):
    def process_string(string):
        stack = []
        for char in string:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

    return process_string(s) == process_string(t)

# Example usage in the driver code 
s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))  # Output: True
