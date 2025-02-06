class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end = False  # Flag to mark the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize the root node

    # Insert a word into the trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create a new node if not present
            node = node.children[char]  # Move to the next node
        node.is_end = True  # Mark the last node as the end of a word

    # Search for a word in the trie
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # Word does not exist in trie
            node = node.children[char]
        return node.is_end  # Return True if word exists

    # Check if any word starts with a given prefix
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # Prefix exists

    # Delete a word from the trie
    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end:
                    return False  # Word does not exist
                node.is_end = False  # Unmark the end of the word
                return len(node.children) == 0  # If no children, delete node
            
            char = word[depth]
            if char not in node.children:
                return False  # Word does not exist

            should_delete = _delete(node.children[char], word, depth + 1)
            if should_delete:
                del node.children[char]  # Delete the node if it's no longer needed
                return len(node.children) == 0
            return False
        
        _delete(self.root, word, 0)

    # Display all words in the Trie
    def display(self):
        result = []
        def _dfs(node, prefix):
            if node.is_end:
                result.append(prefix)  # Add word to result list
            for char, child in node.children.items():
                _dfs(child, prefix + char)
        
        _dfs(self.root, "")
        return result

trie = Trie()

# Insert words
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("ball")

# Search words
print(trie.search("apple"))  # Output: True
print(trie.search("bat"))    # Output: True
print(trie.search("batman")) # Output: False

# Check prefix
print(trie.starts_with("app")) # Output: True
print(trie.starts_with("bat")) # Output: True
print(trie.starts_with("bal")) # Output: True
print(trie.starts_with("bad")) # Output: False

# Delete a word
trie.delete("bat")
print(trie.search("bat"))   # Output: False

# Display all words
print(trie.display())  # Output: ['apple', 'app', 'ball']