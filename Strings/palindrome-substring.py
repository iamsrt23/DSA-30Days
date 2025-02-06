def palindromicsubstring(s):
    def expand_corners(left,right):
        substring = []

        while left>=0 and right<len(s) and s[left] == s[right]:
            substring.append(s[left:right+1])
            left -=1
            right +=1
        return substring
    
    result = []

    for i in range(len(s)):
        result.extend(expand_corners(i,i))
        result.extend(expand_corners(i,i+1))
    return result

print(palindromicsubstring("aab"))  # Output: ['a', 'a', 'b', 'aa']
print(palindromicsubstring("abcba")) # Output: ['a', 'b', 'c', 'b', 'a', 'bcb', 'abcba']
print(palindromicsubstring("aab") ) # Output: ['a', 'a', 'b', 'aa']
print(palindromicsubstring("abcba"))  # Output: ['a', 'b', 'c', 'b', 'a', 'bcb', 'abcba']
