class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        firRow=False
        firCol=False
        for i in range(0,n):
            for j in range(0,len(matrix[0])):
                if(matrix[i][j]==0):
                    if(i==0):
                        firRow=True
                    if(j==0):
                        firCol=True
                
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1,n):
            for j in range(1,len(matrix[0])):
                if (matrix[i][0]==0) or (matrix[0][j]==0):
                    matrix[i][j]=0

        if firRow==True:
            for i in range(0,len(matrix[0])):
                matrix[0][i]=0   

        if firCol==True:
            for i in range(0,len(matrix)):
                matrix[i][0]=0                                

        