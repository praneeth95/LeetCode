class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^0-9A-Za-z]+', '', s)
        s = s.lower()
        reversed_s=s[::-1]
        return s==reversed_s