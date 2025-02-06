def Anagramsearch(text, pattern):
    n = len(text)
    m = len(pattern)
    
    # Edge case: if pattern is longer than text, no match is possible
    if m > n:
        return False
    
    # Initialize hash maps for text window and pattern
    t_hash = {}
    p_hash = {}

    # Fill initial hash maps with the first m characters
    for i in range(m):
        t_hash[text[i]] = t_hash.get(text[i], 0) + 1
        p_hash[pattern[i]] = p_hash.get(pattern[i], 0) + 1
    
    # Function to check if the current window matches the pattern
    def is_anagram():
        return t_hash == p_hash
    
    # Check the initial window
    if is_anagram():
        return True
    
    # Sliding window: slide over the rest of the text
    for i in range(m, n):
        # Add the current character (extend the window)
        t_hash[text[i]] = t_hash.get(text[i], 0) + 1
        
        # Remove the character that is sliding out of the window
        t_hash[text[i - m]] -= 1
        if t_hash[text[i - m]] == 0:
            del t_hash[text[i - m]]  # Remove it to keep the map clean
        
        # Check if the current window matches the pattern
        if is_anagram():
            return True

    return False  # No anagram found

# Example usage
text = "geeksforgeeks"
pattern = "frog"
print(Anagramsearch(text, pattern))  # Output: True
