def is_valid(s):
    hash_map = {')': '(', '}': '{', ']': '['}
    stack=[]

    for char in s:
        if char in hash_map:
            top_element = stack.pop() if stack else '#'

            if hash_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True