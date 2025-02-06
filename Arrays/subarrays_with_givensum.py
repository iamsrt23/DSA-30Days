def subarraysum(arr,target):
    n=len(arr)
    prefix_sum={}
    current_sum=0
    result =[]
    for i in range(n):
        current_sum +=arr[i]

        if current_sum == target:
            result.append(arr[:i +1])
        if current_sum - target in prefix_sum:
            start = prefix_sum[current_sum-target]
            result.append(arr[start+1:i+1])
        prefix_sum[current_sum] =i
    return result





arr = [1,2,3,7,5]
target = 12
print(subarraysum(arr,target))