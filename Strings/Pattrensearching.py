# Rabin Karp Algortihm

def pattrensearching(s1,s2):
    n=len(s1)
    m=len(s2)
    

    for i in range(n-m):
        for j in range(m):
            if s1[j] != s2[i+j]:
                break
            if j==m:
                return i+""
            if j==0:
                i+=1
            else:
                i +=j
    return -1
    
   

s1="geeksforgeeks"
s2="eks"
print(pattrensearching(s1,s2))