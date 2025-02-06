def reverse_string(s):
    stack = []

    for char in s:
        stack.append(char)

    reverse_string = ""

    while stack:
        reverse_string += stack.pop()
    
    return reverse_string


print(reverse_string("RAVITEJA"))