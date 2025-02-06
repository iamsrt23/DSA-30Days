def is_balanced(s):

    stack = []

    matching_parentheses = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        
        elif char in matching_parentheses.keys():
            if not stack or stack[-1] != matching_parentheses[char]:
                return False
        stack.pop()

    return len(stack) == 0


        

# Testing the function
if __name__ == "__main__":
    test_strings = [
        "()",            # Balanced
        "({[]})",        # Balanced
        "({[})",         # Not balanced
        "((()))",        # Balanced
        "(()",           # Not balanced
        "(",             # Not balanced
        "]",             # Not balanced
        "{[()()]}",      # Balanced
    ]

    for s in test_strings:
        print(f"String: {s}, Balanced: {is_balanced(s)}")