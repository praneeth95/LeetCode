class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l=0
        r=len(A)-1
        while l<r:
            while A[l] % 2 ==0 and l<r:
                l+=1
            while A[r] % 2 ==1 and l<r:
                r-=1
            A[l],A[r]=A[r],A[l]
        return A
        