# Trie Datastructure
class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()


# insert in Trie
    def insertString(self,word):# Time:O(m) and space: O(m)
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfString = True
        print("Successfully inserted")
# Search in Trie
    def searchInTrie(self,word):# Time:O(m) and space: O(1)
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endOfString

# delete in Trie
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

        






newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Api")
newTrie.insertString('Apil')

print(newTrie.searchInTrie("Apple"))
print(newTrie.searchInTrie("April"))
print(newTrie.searchInTrie("Api"))
