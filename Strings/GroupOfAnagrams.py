def groupofAnagrams(strs):
    if len(strs) ==0:
        return []
    anagram_map={}

    for s in strs:
        count = [0]*26

        for char in s:
            count[ord(char)-ord('a')] +=1
        key = tuple(count)

        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(s)
    return list(anagram_map.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupofAnagrams(strs))