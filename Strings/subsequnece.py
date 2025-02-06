def subsequence(s1,s2):
    i,j =0,0
    while i<len(s1) and j<len(s2):
        if s1[i] ==s2[j]:
        
            j +=1
  
        i+=1

    return j == len(s2)


s1="ABCDE"
s2="AED"

print(subsequence(s1,s2))
    