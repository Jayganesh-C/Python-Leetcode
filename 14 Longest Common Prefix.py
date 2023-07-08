class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        
        base = strs[0]

        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or base[i] != word[i]:
                    return base[0:i]
        return base