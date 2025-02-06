def longest_sub_string(s):
    left = max_length = 0
    hash_map = set()

    for right in range(len(s)):
        while s[right] in hash_map:
            hash_map.remove(s[left])
            left +=1
        hash_map.add(s[right])
        max_length=max(max_length,right-left+1)
    return max_length

s = "abcabcbb"
print(longest_sub_string(s))