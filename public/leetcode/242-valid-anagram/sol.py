from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # words with different length is not anagrams
        
        freq = [0] * (ord('z') - ord('a'))
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for f in freq:
            if f != 0:
                return False
            
        return True

    
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "car"))
                
