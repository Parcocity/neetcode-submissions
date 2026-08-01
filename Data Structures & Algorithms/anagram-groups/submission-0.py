class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagrams(str1: str, str2: str) -> bool:
            dict1 = dict()
            for letter in str1:
                if letter not in dict1:
                    dict1[letter] = 1
                dict1[letter] += 1
            dict2 = dict()
            for letter in str2:
                if letter not in dict2:
                    dict2[letter] = 1
                dict2[letter] += 1
            
            return dict1 == dict2
        
        output = []
        for element in strs:
            isAnagram = False
            for group in output:
                isAnagram = isAnagrams(group[0], element)
                if isAnagram:
                    group.append(element)
                    break
            if not isAnagram:
                output.append([element])
        
        return output
            

                
                










        