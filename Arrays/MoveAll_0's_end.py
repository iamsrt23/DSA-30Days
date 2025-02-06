def movezerostoend(arr):
    n=len(arr)
    index=0

    for i in range(n):
        if arr[i] !=0:
            arr[index],arr[i] = arr[i],arr[index]
            index +=1
    return arr




arr= [0,1,0,3,12]

print(movezerostoend(arr))