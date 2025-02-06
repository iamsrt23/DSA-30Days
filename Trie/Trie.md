# Trie

A Trie is a Tree-based datastructure that organizes information in a hierarchy.

**Properties:**

- It is typically used to store or search strings in a space and time efficient way.
- Any node in trie can store non repetitive mutliple characters
- Every node stores link of the next character of the string
- Every Node keeps track of ‘end of string’

![Screenshot 2025-01-28 at 5.02.15 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.02.15_PM.png)

**AIR:**

![Screenshot 2025-01-28 at 5.03.44 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.03.44_PM.png)

**AIT:**

![Screenshot 2025-01-28 at 5.04.23 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.04.23_PM.png)

**BAR:**

![Screenshot 2025-01-28 at 5.04.56 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.04.56_PM.png)

**BIL:**

![Screenshot 2025-01-28 at 5.05.43 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.05.43_PM.png)

**BM**

![Screenshot 2025-01-28 at 5.06.19 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.06.19_PM.png)

**Why Trie Datastructure:**

To solve many problems in efficient way

- Spelling checker
- Auto completion

**Common Operations:**

- Creation of Trie
    - create blank hole
    - Intialize Trie() class
    
    ![Screenshot 2025-01-28 at 5.10.28 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.10.28_PM.png)
    

```
# Trie Datastructure
class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

newTrie = Trie()
```

- Insertion in Trie
    - Tire is Blank
    
    ![Screenshot 2025-01-28 at 5.15.24 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.15.24_PM.png)
    
    - New string’s Prefix is common to another strings prefix
    
    **API**
    
    ![Screenshot 2025-01-28 at 5.16.58 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.16.58_PM.png)
    
    - New String Prefix is already present as complete string
    
    **APIS**
    
    ![Screenshot 2025-01-28 at 5.18.23 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.18.23_PM.png)
    
    - String to be inserted is already presented in Trie {picture same as above for APIS}

```python
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

newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Api")
newTrie.insertString('Apil')

```

- Search for a string in Trie
    - String does not exist in Trie
    
    ```python
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
    
    newTrie = Trie()
    newTrie.insertString("App")
    newTrie.insertString("Api")
    newTrie.insertString('Apil')
    
    print(newTrie.searchInTrie("Apple"))
    print(newTrie.searchInTrie("April"))
    print(newTrie.searchInTrie("Api"))
    ```
    

- Deletion from Trie
    - Some Other prefix of string is same as the one that we want to delete.(API,APPLE)
    
    ![Screenshot 2025-01-28 at 5.37.17 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.37.17_PM.png)
    
    - The string is a prefix of another string(API,APIS)
    
    ![Screenshot 2025-01-28 at 5.41.13 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.41.13_PM.png)
    
    - Other String is a prefix of this String.(APIS,AP)
    
    ![Screenshot 2025-01-28 at 5.43.13 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.43.13_PM.png)
    
    - Not any Node depends on this string(K)
    
    ![Screenshot 2025-01-28 at 5.45.03 PM.png](Trie%2018963324436c80e1af5fea93e8b8c395/Screenshot_2025-01-28_at_5.45.03_PM.png)