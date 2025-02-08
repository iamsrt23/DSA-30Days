def combination_sum_II(candiates,target):
  result = []
  candiates.sort()

  def backtrack(start,path,total):
    if total == target:
      result.append(path[:])
      return
    if total>target:
      return
    
    prev = -1
    for i in range(start,len(candiates)):
      if candiates[i] == prev:
        continue

      path.append(candiates[i])
      backtrack(i+1,path,total+candiates[i])
      path.pop()
      prev = candiates[i]
  backtrack(0,[],0)
  return result
print(combination_sum_II([10,1,2,7,6,1,5], 8))