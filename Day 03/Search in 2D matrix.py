#https://leetcode.com/problems/search-a-2d-matrix/submissions/

"""
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

#Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        front = 0;
        m = len(matrix)
        n = len(matrix[0])
        back = m*n - 1
        
        res = False
        while (front <= back):
            mid = front + (back - front)//2
            i = mid//n
            j = mid - n*i
            if (matrix[i][j] == target):
                res = True
                break
            elif (matrix[i][j] > target):
                back = mid - 1
            else:
                front = mid+1
             
        return res
