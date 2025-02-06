def palindrome(s):
    if s[::-1] ==s:
        return True
    else:
        return False
    

s="radar"
s="hello"
print(palindrome(s))