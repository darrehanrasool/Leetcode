"""
Problem: Implement Trie (Prefix Tree) (LeetCode #208)
Standard Trie with TrieNode dictionary
Time Complexity: O(L) per operation
Space Complexity: O(N * L)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    print("✅ All Implement Trie tests passed!")
