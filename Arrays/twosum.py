def twosum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i] + arr[j] == target:
                return i,j





arr=[2,7,11,15]
target=18
print(twosum(arr,target))