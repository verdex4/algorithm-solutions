from typing import List
from collections import Counter

class Solution:
    def groupAnagramsBruteForce(self, strs: List[str]) -> List[List[str]]:
        """Solution with time complexity O(n^2), n = len(strs)"""
        counters = [] # counters list
        for s in strs: # each string - new counter
            counter = Counter(s)
            counters.append(counter)

        classes = [[] for _ in range(len(counters))] # anagram equivalent classes
        cls_representatives = [] # or unique counters
        first_empty = 0 # index of first emply list in classes 

        for s, cntr in zip(strs, counters):
            is_found = False # have we seen this type of counter before
            for i, rep in enumerate(cls_representatives):
                if cntr == rep: 
                    is_found = True
                    classes[i].append(s) # representative index is the same as classes index
                    break
            if not is_found:
                # adding new element in empty place
                cls_representatives.append(cntr)
                classes[first_empty].append(s)
                first_empty += 1
        
        res = []
        for i in range(first_empty): # classes[first_empty] = [], first_empty <= len(classes)
            res.append(classes[i])

        return res
    
    def groupAnagramsMyBest(self, strs: List[str]) -> List[List[str]]:
        """Solution with time complexity O(n * m), n = len(strs), m = max(len(strs[i]))"""
        classes = {} # map of classes - representative: [elements in class]
        for s in strs: # O(n)
            counter = Counter(s) # O(m)
            counter = dict(sorted(counter.items())) # sorting by keys - O(1)
            rep = "".join(counter) # string representation, O(1)

            if rep not in classes: # O(1)
                classes[rep] = [s] # adding new class
            else:
                classes[rep].append(s) # adding s to existing class
            
        return list(classes.values())
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Solution with time complexity O(n * m), n = len(strs), m = max(len(strs[i]))"""
        classes = {}
        for s in strs:
            freq_list = [0] * 26
            for let in s:
                idx = ord(let) - ord('a')
                freq_list[idx] += 1
            representative = tuple(freq_list)
            classes.setdefault(representative, []).append(s)
        
        return list(classes.values())

sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs))

strs = ["stop","pots","reed","","tops","deer","opts",""]
print(sol.groupAnagrams(strs))
