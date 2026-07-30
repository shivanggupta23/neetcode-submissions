class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            
        for row in range(n):
            left=0
            right=n-1
            while left<right:
                matrix[row][left],matrix[row][right]=matrix[row][right],matrix[row][left]
                left+=1
                right-=1
              