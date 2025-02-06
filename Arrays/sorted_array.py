def sorted_array(arr):
    n = len(arr)

    for i in range(n):
        if arr[i] > arr[i+1]:
            return False
        return True



arr = [1,2,3,4,5]
arr= [5,3,2,1]

print(sorted_array(arr))