#https://leetcode.com/problems/set-matrix-zeroes/submissions/

"""
take first row and column of the matrix as the array for checking whether the particular 
column or row has the value 0 or not.Since matrix[0][0] are overlapping.Therefore take 
separate variable col0(say) to check if the 0th column has 0 or not and use matrix[0][0] 
to check if the 0th row has 0 or not.Now traverse from last element to the first element 
and check if matrix[i][0]==0 || matrix[0][j]==0 and if true set matrix[i][j]=0,else continue.

 While traversing for the second time the first row and column will be computed first, 
 which will affect the values of further elements that’s why we traversing in the reverse direction.
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col0 = 1
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = 0
                
            for j in range(1, len(matrix[i])):
                if (matrix[i][j] == 0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[i])-1, 0, -1):
                if(matrix[0][j] == 0 or matrix[i][0] == 0):
                    matrix[i][j] = 0
                    
            if col0 == 0:
                matrix[i][0] = 0
