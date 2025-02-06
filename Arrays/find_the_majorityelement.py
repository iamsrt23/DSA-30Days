def majority_element(arr):
    n=len(arr)
    hashd={}
    

    for i in range(n):
        if arr[i] not in hashd:
            hashd[arr[i]] =1
        else:
            hashd[arr[i]] +=1

        if hashd[arr[i]] > n//2:
            return arr[i]
    







arr=[3, 3, 4, 2, 4, 4, 2, 4, 4]

print(majority_element(arr))