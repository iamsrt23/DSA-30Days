def characterreplacement(s,k):
    hash_map = {}
    left = max_length = 0
    most_occurence = 0

    for right in range(len(s)):
        if s[right] not in hash_map:
            hash_map[s[right]] = 1
        else:
            hash_map[s[right]] += 1

        most_occurence = max(most_occurence,hash_map[s[right]])
     # If too many replacements are needed, shrink the window
        if (right-left+1)-most_occurence > k:
            hash_map[s[left]] -=1 # Reduce frequency of leftmost char
            left +=1  # Shrink window from the left

        max_length=max(max_length,right-left+1)
    return max_length


