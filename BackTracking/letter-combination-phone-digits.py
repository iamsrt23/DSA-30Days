def lettercombinations(digits):
  if not digits:
    return []
  phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
  result = []

  def backtracking(index,path):
    if index == len(digits):
      result.append("".join(path))
      return
    
    letters = phone_map[digits[index]]

    for letter in letters:
      path.append(letter)
      backtracking(index+1,path)
      path.pop()

  backtracking(0,[])
  return result

print(lettercombinations('234'))

