
def countTriangles(arr):
        # code here
    arr.sort()
    result = 0
        
    for i in range(2,len(arr)):
        left,right = 0,i-1
            
        while left<right:
            if arr[left]+arr[right]>arr[i]:
                result += right-left
                    
                right -=1
            else:
                left +=1
                    
    return result
    


arr = [4,6,3,7]
        
print(countTriangles(arr))