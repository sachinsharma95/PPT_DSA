class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def str2tree(s: str) -> TreeNode:
    if not s:
        return None

    # Find the value of the root node
    i = 0
    while i < len(s) and (s[i].isdigit() or s[i] == '-'):
        i += 1
    value = int(s[:i])
    root = TreeNode(value)

    # Find the left and right substrings representing the left and right subtrees
    left_start = i
    left_end = find_matching_parenthesis(s, left_start)
    root.left = str2tree(s[left_start + 1 : left_end])

    if left_end + 1 < len(s):
        right_start = left_end + 1
        right_end = find_matching_parenthesis(s, right_start)
        root.right = str2tree(s[right_start + 1 : right_end])

    return root

def find_matching_parenthesis(s: str, start: int) -> int:
    stack = []
    for i in range(start, len(s)):
        if s[i] == '(':
            stack.append('(')
        elif s[i] == ')':
            stack.pop()
            if not stack:
                return i
    return -1


# driver code
s = "4(2(3)(1))(6(5))"
root = str2tree(s)

# Helper function to convert the binary tree to a list for easier visualization
def tree_to_list(root):
    if not root:
        return []
    return [root.val] + tree_to_list(root.left) + tree_to_list(root.right)

result = tree_to_list(root)
print(result)  # Output: [4, 2, 6, 3, 1, 5]
