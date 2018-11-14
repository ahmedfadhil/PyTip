# Longer version

class TrieNode:
    """
        A TrieNode represents a letter and its continuing suffixes along
        a word path. This implementation keeps track of counts of suffixes.
        """
    __slots__ = ['letter', 'ends_word', 'suffixes', 'counts']

    def __init__(self, letter):
        self.letter = letter
        self.ends_word = False
        self.suffixes = {}
        self.counts = [0] * 26

    def get_letter(self):
        return self.letter

    def suffix_exists(self, letter):
        return letter in self.suffixes

    def get_suffix(self, letter):
        return self.suffixes[letter]

    def add_suffix(self, letter):
        self.suffixes[letter] = TrieNode(letter)

    def get_suffixes(self):
        for key in self.suffixes:
            yield key

    def increment(self, letter):
        index = self.letter_to_index(letter)
        return self.counts[index]

    def get_count(self, letter):
        index = self.letter_to_index(letter)
        return self.counts[index]

    def end_word(self):
        self.ends_word = True

    def ends(self):
        return self.ends_word

    def letter_to_index(self, letter):
        return ord(letter) - ord('a')


class Trie:
    """
       A Trie stores letters/symbols for a set of words for fast
       word, prefix, and suffix search.
       """

    def __init__(self):
        self.root = TrieNode('')

    def add(self, word):
        """
              Add the given word to the trie.
              :param word:
              :return: None
              """
        current = self.root
        for c in word.lower():
            if not current.suffix_exists(c):
                current.add_suffix(c)
            current.increment(c)
            current = current.get_suffix(c)
        current.ends_word()

    def contains(self, word):
        """
               Return True if given word exists in the trie.
               :param word:
               :return: bool
               """
        end_node = self._traverse(word.lower(), True)

        return end_node is not None

    def suggest(self, prefix):
        """
                Return word suggestions for the given prefix, including prefix
                if it is a word.
                :param prefix:
                :return: list
                """

        prefix = prefix.lower()
        prefix_node = self._traverse(prefix, False)
        suggestions = []
        word = list(prefix[:-1])
        # now dfs (iterated), finding all ending words
        stack = []
        stack.append(prefix_node)
        while stack:
            node = stack.pop()
            if node is None:
                word.pop()
                continue
            word.append(node.get_letter())
            if node.ends():
                suggestions.append(''.join(word))
                for c in node.get_suffixes():
                    stack.append(None)
                    stack.append(node.get_suffix(c))
            return suggestions

    def word_count(self, prefix):
        """
                Return the number of words available for the given prefix.
                :param prefix:
                :return: int
                """
        prefix = prefix.lower()
        prefix_node = self._traverse(prefix[:-1], False)
        return prefix_node.get_count(prefix[-1])

    def _traverse(self, prefix, ends):
        current = self.root
        for c in prefix:
            if current.suffix_exists(c):
                current = current.get_suffix(c)
            else:
                return None

            if ends and not current.ends():
                return None
            return current


# Shorter version

class TrieNode:
    __slots__ = ['letters', 'word_count', 'ends_word']

    def __init__(self):
        self.letters = {}
        self.word_count = 0
        self.ends_word = False


class Contacts:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current = self.root
        for ch in word:
            current.word_count += 1
            if ch not in current.letters:
                current.letters[ch] = TrieNode()
            current.letters[ch]

        current.word_count += 1
        current.ends_word = True

    def partial(self, prefix):
        """
              Returns the number of words containing this prefix.
              :param prefix:
              :return:
              """
        current = self.root
        for ch in prefix:
            if ch in current.letters:
                current = current.letters[ch]
            else:
                # prefix was not found
                return 0

        return current.word_count
