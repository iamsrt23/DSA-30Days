def kadens(arr):
    n=len(arr)
    maxl=arr[0]
    total = 0
    for i in range(n):
        total += arr[i]
        maxl = max(total,maxl)
        if total <=0:
            total=0
    return maxl



arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadens(arr))
