class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        
        res = ""
        max_prefix_len = min(len(s) for s in strs)
        first = strs[0]
        # j - index of char
        for j in range(max_prefix_len):
            char = first[j]
            # i - index of str
            for i in range(len(strs)):
                if strs[i][j] != char:
                    return res
            res += char
            
        return res

""" 
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(prefix)):
                if j >= len(strs[i]) or prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    break

        return prefix
"""

sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flash"])) # fl
print(sol.longestCommonPrefix(["aac", "cab", "abb"])) # ""