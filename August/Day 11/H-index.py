class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        
        for index,citation in enumerate(citations):
            if index>=citation:
                return index
        return len(citations)
        