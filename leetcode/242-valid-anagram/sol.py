from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # words with different length is not anagrams
        
        counter_s = defaultdict(lambda: 0)
        counter_t = defaultdict(lambda: 0)
        for i in range(len(s)):
            counter_s[s[i]] += 1
            counter_t[t[i]] += 1
        
        return counter_s == counter_t
    
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "car"))
                
