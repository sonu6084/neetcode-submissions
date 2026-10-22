class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix),len(matrix[0])
        top, bot = 0,Rows-1

        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = top + 1
            elif target < matrix[row][0]:
                bot = bot - 1
            else:
                break
        
        if top > bot:
            return False

        l,r = 0,Cols-1
        row = (top+bot)//2
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                
                r = mid - 1
        return False