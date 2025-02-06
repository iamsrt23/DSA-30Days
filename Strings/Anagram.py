def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    hash_map={}

    for i in range(len(s1)):
       hash_map[ord(s1[i])-ord('a')] =hash_map.get(ord(s1[i]) - ord('a'), 0) + 1
       hash_map[ord(s2[i])-ord('a')] =hash_map.get(ord(s2[i]) - ord('a'), 0) - 1
    
    for value in hash_map.values():
        if value == 0:
            return True



 





s1="listen"
s2="silent"

print(anagram(s1,s2))