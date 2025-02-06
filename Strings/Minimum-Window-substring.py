def minimumwindow(s,t):
    if not s or not t:
        return ""
    
    t_freq = {}

    for c in t:
        if c not in t_freq:
            t_freq[c] = 1
        else:
            t_freq[c] +=1
    max_freq={}
    min_length= float('inf')
    min_window=""
    left = 0
    formed = 0
    required = len(t_freq)

    for right in range(len(s)):
        char = s[right]

        if char  not in max_freq:
            max_freq[char] =1
        else:
            max_freq[char] +=1

        if char in t_freq and max_freq[char] == t_freq[char]:
            formed +=1
        
        while left<=right and formed==required:
            if right-left+1 < min_length:
                min_length = right-left+1
                min_window=s[left:right+1]
            
            left_char = s[left]
            max_freq[left_char] -=1

            if left_char in t_freq and max_freq[left_char] < t_freq[left_char]:
                formed -=1
            left +=1
        right +=1
    return min_window

print(minimumwindow("ADOBECODEBANC", "ABC"))