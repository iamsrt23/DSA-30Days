def post_fix(expression):

    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))

        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == "+":
                result = operand1 + operand2
        
            
            elif char == "-":
                result = operand1 - operand2
            
            elif char == "*":
                result = operand1 * operand2

            
            elif char == "/":
                result = operand1 / operand2
            
            stack.append(result)

    return stack.pop()


if __name__ == "__main__":
    # Example postfix expressions
    postfix_exprs = [
        "23*5+",        # (2 * 3) + 5 = 11
        "352*+9-",      # (3 + (5 * 2)) - 9 = 4
        "12+34+*",      # (1 + 2) * (3 + 4) = 21
        "23+5*8-",      # (2 + 3) * 5 - 8 = 7
        "56+34+*2/"     # ((5 + 6) * (3 + 4)) / 2 = 63
    ]

    for expr in postfix_exprs:
        print(f"Postfix Expression: {expr}, Result: {post_fix(expr)}")