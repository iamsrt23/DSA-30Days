def rev_order_words(s):
    s = s.split(" ")
    i,j=0,len(s)-1
    while i<j:
        s[i],s[j] = s[j],s[i]
        i +=1
        j -=1
    return " ".join(s)




s = "abc"
print(rev_order_words(s))