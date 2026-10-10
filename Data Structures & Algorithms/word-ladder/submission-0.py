class Solution:
    # because three is a guarantee that the words will be of same length,
    # we can compute the difference between them by just comparing them
    # character by character
    # Time Complexity: O(s) where s is the length of the word
    # Space Complexity: O(1)
    def wordDiff(self, word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return diff

    # to compute the adj list we will:
    # - init negih to [] for each word
    # - one for loop checking the difference between beginWord and each word in wordList
    # - one for loop checking the difference between each word in wordList against each other
    # Time Complexity: O(n^2 * s) where n is the length of the wordList and s the length of the words
    # Space Complexity: O(n^2 + n * s)
    def toAdj(self, beginWord, wordList):
        adj = {word: [] for word in wordList}
        adj[beginWord] = []

        for word in wordList:
            if self.wordDiff(beginWord, word) == 1:
                adj[beginWord].append(word)
                adj[word].append(beginWord)

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.wordDiff(wordList[i], wordList[j]) == 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])

        return adj

    # Time Complexity: O(n^2 * s) where n is the length of the wordList and s the length of the words
    # Space Complexity: O(n^2 + n * s)
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        adj = self.toAdj(beginWord, wordList)
        q = deque()
        q.append(beginWord)
        seen = set()
        seen.add(beginWord)
        distance = 1

        while q:
            qLen = len(q)
            for _ in range(qLen):
                w = q.popleft()

                if w == endWord:
                    return distance

                for neigh in adj[w]:
                    if neigh not in seen:
                        seen.add(neigh)
                        q.append(neigh)
                
            distance += 1
        
        return 0
                
                
