def reversearray(arr,i,j):

    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j -=1




def rotate_k_pos(arr,k):
    n=len(arr)
    k=k%n
    reversearray(arr,0,k-1)
    reversearray(arr,k,n-1)
    reversearray(arr,0,n-1)
    return arr






arr = [1, 2, 3, 4, 5, 6]
k=2

print(rotate_k_pos(arr,k))