class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            answer=False
        else:
            while num %4==0:
                num=num/4
            if num==1:
                answer=True
            else:
                answer=False
        return answer