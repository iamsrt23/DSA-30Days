def frequency_of_string(s):
    hashd={}
    for char in s:
        if char not in hashd:
            hashd[char] =1
        else:
            hashd[char] +=1
    return hashd


s="geekforgeeks"
print(frequency_of_string(s))