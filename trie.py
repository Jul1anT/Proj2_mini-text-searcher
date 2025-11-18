"""
Trie (Prefix Tree) implementation for word autocompletion.
Tree data structure where each node represents a character.
"""

class TrieNode:
    """Trie node that stores children and marks end of word."""
    def __init__(self):
        self.children = {}  # Dictionary of characters to child nodes
        self.is_end_of_word = False  # Marks if valid word ends here


class Trie:
    """
    Prefix tree for efficient search and autocompletion.
    Complexity: O(m) where m is the word length.
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Inserts a word into the Trie."""
        word = word.lower()
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word):
        """Searches if a complete word exists in the Trie."""
        word = word.lower()
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """Checks if any word with the given prefix exists."""
        prefix = prefix.lower()
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
    
    def autocomplete(self, prefix, max_results=10):
        """
        Returns list of words starting with the prefix.
        Uses DFS to traverse all branches from the prefix node.
        """
        prefix = prefix.lower()
        node = self.root
        
        # Navigate to the prefix node
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # DFS to find all complete words
        results = []
        self._dfs_collect(node, prefix, results, max_results)
        return results
    
    def _dfs_collect(self, node, current_word, results, max_results):
        """Traverses the tree collecting complete words."""
        if len(results) >= max_results:
            return
        
        if node.is_end_of_word:
            results.append(current_word)
        
        for char, child_node in sorted(node.children.items()):
            self._dfs_collect(child_node, current_word + char, results, max_results)
    
    def get_all_words(self):
        """Returns all words stored in the Trie."""
        results = []
        self._dfs_collect(self.root, "", results, float('inf'))
        return results
