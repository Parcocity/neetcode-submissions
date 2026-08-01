class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = ['a', 'e', 'i', 'o', 'u']
        count = [0]
        for i in range(0, len(words)):
            word = words[i]
            length = len(word)
            if word[0] in vowel and word[length-1] in vowel:
                words[i] = 1
                count.append(count[i]+1)
            else:
                words[i] = 0
                count.append(count[i])
        output = []
        for query in queries:
            output.append(count[query[1]+1]-count[query[0]])
        return output
        
