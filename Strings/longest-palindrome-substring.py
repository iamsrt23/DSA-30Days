def longest_palindrome_substring(s):
    if not s:
        return ""
    
    # middle
    def expand_corners(left,right):
        if left>=0 and right<len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return s[left+1:right]
    
    longest = ""

    for i in range(len(s)):
        odd_palindrome= expand_corners(i,i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        even_palindrome = expand_corners(i,i+1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

print(longest_palindrome_substring("babad"))  # "bab" or "aba"
print(longest_palindrome_substring("cbbd"))  # "bb"