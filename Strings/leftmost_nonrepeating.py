def leftnon_repeating(s):
    n= len(s)

    hashd={}

    for i in range(n):
        if s[i] not in hashd:
            hashd[s[i]] =1
        else:
            hashd[s[i]] +=1

    for i in range(n):
        if hashd[s[i]] ==1:
            return i
    return -1

s="geeksforgeeks"
print(leftnon_repeating(s))