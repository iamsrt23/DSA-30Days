def is_valid_palindrome(s):
    left = 0
    right = len(s)-1

    while left <=right:
        # skip non-alphanumeric numbers
        if not s[left].isalnum():
            left +=1
        elif not s[right].isalnum():
            right -=1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -=1
    return True

print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_valid_palindrome("race a car"))  # False