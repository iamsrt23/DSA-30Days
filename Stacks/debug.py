def sumClosest(arr, target):
        # code here
        
    n=len(arr)
    i,j = 0,n-1
    closet_sum=float('inf')
    closet_diff = float("inf")
    arr.sort()
        
        
    while i<j:
        current_sum = arr[i] + arr[j]
        diff = abs(current_sum-target)
            
        if diff<closet_diff:
            current_sum = closet_sum
            closet_diff = current_sum
                
        if current_sum<target:
            i+=1
        elif current_sum>target:
            j -=1
        else:
            return current_sum
    return closet_sum
        
        
print(sumClosest([10,30,20,5],25))