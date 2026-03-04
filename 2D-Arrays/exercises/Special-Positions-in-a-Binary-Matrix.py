from collections import defaultdict
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        col_count = defaultdict(int)
        row_count = defaultdict(int)

        
        for i in range(m): # i = row_index
            for j in range(n): # j = column index
                if mat[i][j] != 1:
                    continue
                row_count[i] += 1
                col_count[j] += 1
        
        count = 0
        for i in range(m): # i = row_index
            for j in range(n): # j = column index
                if mat[i][j] != 1:
                    continue

                if row_count[i] <= 1 and col_count[j] <= 1:
                    count += 1
        
        return count
