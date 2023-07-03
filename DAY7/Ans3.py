"""
Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

**Example 1:**

**Input:** num1 = "11", num2 = "123"

**Output:**

"134"

"""



# Solution 

def add_str(num1,num2 ):
    result = int(num1)+int(num2)  # converting string to int
    # converting int to string ans returning to the function

    return str(result)


# driver code and callig the fucntion

num1 = 11
num2 =123
print(add_str(num1,num2))
