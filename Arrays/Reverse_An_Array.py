def reversearray(arr):

    i,j = 0, len(arr)-1

    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i +=1
        j -=1

    return arr

    





arr=[1,2,3,4,5]
print(reversearray(arr))