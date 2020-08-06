class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final=[]
        for num in nums:
            num = abs(num)

            if nums[num - 1] >0:
                nums[num - 1] *= -1
            else:
                final.append(num)
        return final
        