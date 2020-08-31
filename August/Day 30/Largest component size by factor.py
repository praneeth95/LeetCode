class Solution:
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ma = max(A)
        N = len(A)
        m = list(range(ma + 1))
        for a in A:
            for k in range(2, int(math.sqrt(a)) + 1):
                if a % k == 0:
                    self.u(m, a, k)
                    self.u(m, a, a // k)
        count = collections.defaultdict(int)
        for a in A:
            count[self.f(m, a)] += 1
        return max(count.values())
        
    def f(self, m, a):
        while m[a] != a:
            m[a] = m[m[a]]
            a = m[a]
        return a
    
    def u(self, m, a, b):
        if m[a] == m[b]: return
        pa = self.f(m, a)
        pb = self.f(m, b)
        m[pa] = pb
