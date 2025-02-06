def second_largest(arr):
    n= len(arr)
    large = second_large= arr[0]

    for i in range(1,n):
        if arr[i] > large:
            # Here we are swapping large with arr[i] and secondlarge with large
            second_large,large = large,arr[i]
        # The condition here is large is not equal to arr[i] and arr[i] must be greater than secondlarge
        elif arr[i] != large and second_large<arr[i]:
            second_large=arr[i]
    return second_large





arr = [12,35,1,10,34,36,1]

print(second_largest(arr))