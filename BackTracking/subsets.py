def subsets(nums):
  result = []

  def backtracking(start,path):
    result.append(path[:])

    for i in range(start,len(nums)):
      path.append(nums[i])
      backtracking(i+1,path)
      path.pop()
    
  backtracking(0,[])
  return result
print(subsets([1, 2, 3]))