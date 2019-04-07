class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {word: i for i, word in enumerate(words)}
        re = []
        
        for word in d:
            n = len(word)
            for i in range(n + 1):
                l, r = word[:i], word[i:]
                if l == l[::-1]:
                    if r[::-1] in d and r[::-1] != word:
                        re.append([d[r[::-1]], d[word]])
                if i != n and r == r[::-1]:
                    if l[::-1] in d and l[::-1] != word:
                        re.append([d[word], d[l[::-1]]])
                        
        return re