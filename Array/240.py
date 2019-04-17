class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #从左下角或者右上角开始查找，这里是右上角开始查找,这里的陷阱的必须要先判断一下matrix是否符合要求
        if not matrix:
            return False
        m = 0
        n = len(matrix[0])-1
        while n >= 0 and m < len(matrix):
            if matrix[m][n] > target:
                n = n - 1
            elif matrix[m][n] < target:
                m = m + 1
            else:
                return True
        return False