class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode()
                node = node.children[char]
        node.isEnd = True



    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        stack = [(self.root,word)]

        while stack:
            node, word = stack.pop()

            if not word:
                if node.isEnd:
                    return True

            elif word[0] in node.children:
                temp = node.children[word[0]]
                stack.append((temp,word[1:]))

            elif word[0] == '.':
                for temp in node.children.values():
                    stack.append((temp,word[1:]))
        return False        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)