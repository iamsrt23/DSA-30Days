def largest_element(arr):
    n=len(arr)
    largest_num=arr[0]

    for i in range(1,n):
        if arr[i] > largest_num:
            largest_num = arr[i]
    return largest_num





arr=[1,8,7,3,4]
print(largest_element(arr))