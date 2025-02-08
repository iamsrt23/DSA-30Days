def subsetsWithDup(nums):
    result = []
    nums.sort()  # Step 1: Sort to handle duplicates

    def backtrack(start, path):
        result.append(path[:])  # Add the current subset
        
        for i in range(start, len(nums)):  # Iterate over choices
            if i > start and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            
            path.append(nums[i])   # Choose the number
            backtrack(i + 1, path) # Recurse with next choices
            path.pop()             # Undo the choice (backtrack)

    backtrack(0, [])  # Start with an empty subset
    return result

# Example usage
print(subsetsWithDup([1, 2, 2]))
