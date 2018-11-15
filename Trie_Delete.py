# Python program for delete operation
# in a Trie
class TrieNode(object):
    """Trie node class"""

    def __init__(self):
        self.children = [None] * 26
        # non zero if leaf
        self.value = 0

    def leafNode(self):
        """check if node is leaf node or not"""
        return self.value != 0

    def isItFreeNode(self):
        """
        if node have no children then it is free
        if node have children return False, else True
        :return:
        """
        for c in self.children:
            if c:
                return False
            return True


class Trie(object):
    """
    Trie data structure class
    """

    def __init__(self):
        self.root = self.getNode()
        self.count = 0

    def getNode(self):
        return TrieNode()

    def _index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        length = len(key)
        pCrawler = self.root
        self.count += 1
        for level in range(length):
            index = self._index(key[level])
            if pCrawler.children[index]:
                pCrawler = pCrawler.children[index]
            else:
                pCrawler.children[index] = self.getNode()
                pCrawler = pCrawler.children[index]
        pCrawler.value = self.count

    def search(self, key):
        '''
               Search key in the trie
               Returns true if key presents in trie, else false
               '''
        length = len(key)
        pCrawler = self.root
        for level in range(length):
            index = self._index(key[level])
            if not pCrawler.children[index]:
                return False

            pCrawler = pCrawler.children[index]
        return pCrawler != None and pCrawler.value != 0

    def _deleteHelper(self, pNode, key, level, length):
        '''
                Helper function for deleting key from trie
                '''
        if pNode:
            #             Base case
            if level == length:
                if pNode.value:
                    pNode.value = 0
                return pNode.isItFreeNode()
            # recursive case
            else:
                index = self._index(key[level])
                if self._deleteHelper(pNode.children[index], key, level + 1, length):
                    # last node marked,delete it
                    del pNode.children[index]
                    # recursively climb up and delete
                    # eligible nodes
                    return (not pNode.leafNode() and pNode.isItFreeNode())
        return False

    def deleteKey(self, key):
        """Delete key from trie"""
        length = len(key)
        if length > 0:
            self._deleteHelper(self.root, key, 0, length)


def main():
    keys = ["she", "sells", "sea", "shore", "the", "by", "sheer"]
    trie = Trie()
    for key in keys:
        trie.insert(key)
    trie.deleteKey(keys[0])
    print("{} {}".format(keys[0], "Present in trie" if trie.search(keys[0]) else "Not present in trie"))
    print("{} {}".format(keys[6], "Present in trie" if trie.search(keys[6]) else "Not present in trie"))


if __name__ == '__main__':
    main()
