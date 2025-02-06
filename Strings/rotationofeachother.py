# we can get clockwise and anticlock wise get same answer

def rotate(s1,s2):
    if len(s1) != len(s2):
        return False
    
    for i in range(len(s1)):
        s1 = s1[2:] + s1[:2]
        if s1==s2:
            return True
        
        else:
            return False


s1="ABAB"
s2="ABBA"
print(rotate(s1,s2))