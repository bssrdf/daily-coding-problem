#I think, at the most, `n-1` moves should be sufficient. 



class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)//2
        self.count = n
        roots = [i for i in range(n)]
        def find(i):
            while roots[i] != i:
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i 
        def union(i, j):
            x, y = find(i), find(j) 
            if x != y:
                roots[x] = y
                self.count -= 1
        for i in range(n):
            a = row[2*i]
            b = row[2*i + 1]
            union(a, b)
        return n - self.count

if __name__=="__main__":
    print(Solution().minSwapsCouples([0, 1, 0, 1]))