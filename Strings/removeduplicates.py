def removeduplicates(s):
    hashd={}
    lst=""

    for char in s:
        if char not in hashd:
            hashd[char] =1
            lst +=char
    return lst


s="aabbcc"
print(removeduplicates(s))