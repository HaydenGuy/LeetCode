class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                node = self.root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_end = True

            def longestCommonPrefix(self):
                node = self.root
                prefix = ""
                while len(node.children) == 1 and not node.is_end:
                    char = list(node.children.keys())[0]
                    prefix += char
                    node = node.children[char]
                return prefix


        if not strs:
            return ""
        
        trie = Trie()
        for word in strs:
            trie.insert(word)
        
        return trie.longestCommonPrefix()
