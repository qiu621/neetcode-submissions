class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n

        while low < high:
            mid = (low + high) // 2
            r, c = (mid // n), (mid % n)
            if matrix[r][c] >= target:
                high = mid
            else:
                low = mid + 1
        return low < (m*n) and matrix[low // n][low % n] ==target
        