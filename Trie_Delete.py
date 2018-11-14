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

    def _deleteHelper(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
