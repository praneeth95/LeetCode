class Solution(object):
    def titleToNumber(self, s):
        """
            :type s: str
            :rtype: int
        """
        res = 0
        for char in s:
             x = ord(char) - ord('A') + 1
             res = res * 26 + x
        return res

